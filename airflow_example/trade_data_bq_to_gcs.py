## Import Libraries
import datetime
from time import strftime
from airflow import DAG
from airflow.contrib.operators import bigquery_to_gcs, bigquery_operator, gcs_to_gcs
from airflow.operators import dummy_operator

## Setup Default Arguments
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
current_date = strftime('%Y_%m_%d_%H_%M_%S')
yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y_%m_%d_%H_%M_%S')
current_bucket = "gs://efx-adp-api-demo/trade_agg_{0}.csv".format(current_date)

default_args = {
    'owner': 'jc-dot-burnworth-at-slalom-dot-com',
    'start_date': yesterday,
    'depends_on_past': False,
    'email': ['jc.burnworth@slalom.com'],
    'email_on_success': True,
    'email_on_failure': False,
    'email_on_retry': False
}

## Main DAG & Workflow
dag = DAG(dag_id='trade_data_dump',
          default_args=default_args,
          schedule_interval='@daily')

## Dummies
start = dummy_operator.DummyOperator(
    task_id='start',
    trigger_rule='all_success',
    dag=dag
)

end = dummy_operator.DummyOperator(
    task_id='end',
    trigger_rule='all_success',
    dag=dag
)

## Move old trade_agg folder to old folder in same bucket - Not working for some reason
archive_old_data = gcs_to_gcs.GoogleCloudStorageToGoogleCloudStorageOperator(
    task_id='archive_old_files',
    source_bucket='efx-adp-api-demo',
    source_object='/*.csv',
    destination_bucket='efx-adp-api-demo',
    destination_object='archive/',
    move_object=True,
    dag=dag)

## Update current account table
load_account_current = bigquery_operator.BigQueryOperator(
    task_id='load_account_current',
    sql="""SELECT
            acct.Account_Number AS Account_Number
            ,acct.Account_Type AS Account_Type
            ,acct.Account_Name AS Account_Name
            ,acct.Account_Address AS Account_Address
            ,acct.City AS Account_City
            ,acct.State_Code AS State_Code
            ,acct.FA_Code AS FA_Code
            FROM
            gcp_flex_etl.account acct
            INNER JOIN (SELECT
                        acct1.Account_Number
                        ,MAX(acct1.Date) AS Max_Date
                        FROM
                        gcp_flex_etl.account acct1
                        GROUP BY
                        acct1.Account_Number) Max_Date ON (Max_Date.Account_Number = acct.Account_Number
                                                           AND Max_Date.Max_Date = acct.Date)""",
    use_legacy_sql=True,
    destination_dataset_table='gcp_flex_etl.account_current',
    write_disposition='WRITE_TRUNCATE',
    create_disposition='CREATE_IF_NEEDED',
    allow_large_results=True,
    dag=dag)

## Update current financial advisor table
load_financial_advisor_current = bigquery_operator.BigQueryOperator(
    task_id='load_financial_advisor_current',
    sql="""SELECT
            emp.Employee_Number AS Employee_Number
            ,emp.FA_Code AS FA_Code
            ,CONCAT(emp.First_Name,' ',emp.Last_Name) AS FA_Name
            ,emp.Department_Code AS Department_Code
            FROM
            gcp_flex_etl.employee emp
            INNER JOIN (SELECT
                        emp1.FA_Code
                        ,MAX(emp1.Date) AS Max_Date
                        FROM
                        gcp_flex_etl.employee emp1
                        GROUP BY
                        emp1.FA_Code) Max_Date ON (Max_Date.FA_Code = emp.FA_Code
                                                   AND Max_Date.Max_Date = emp.Date)""",
    use_legacy_sql=True,
    destination_dataset_table='gcp_flex_etl.financial_advisor_current',
    write_disposition='WRITE_TRUNCATE',
    create_disposition='CREATE_IF_NEEDED',
    allow_large_results=True,
    dag=dag)

## Update trade_agg_table
load_trade_agg = bigquery_operator.BigQueryOperator(
    task_id='load_trade_agg',
    sql="""SELECT
            -- Trade Information
            trd.Account_Number AS Account_Number
            ,trd.Buy_Sell AS Buy_Sell
            ,trd.Security_Type AS Security_Type_Child
            ,trd.Security_Type_2 AS Security_Type_Parent
            ,trd.Sector AS Sector
            ,trd.Trade_Date AS Trade_Date
            -- Trade Aggregates
            ,COUNT(trd.trade_id) AS Trade_Count
            ,SUM(trd.Quantity) AS Quantity
            ,SUM(trd.Gross_Amount) AS Gross_Amount
            ,SUM(trd.Other_Fees) AS Fees
            -- Account Information
            ,acct.Account_Type AS Account_Type
            ,acct.Account_Name AS Account_Name
            -- Financial Advisor Information
            ,emp.FA_Code AS FA_Code
            ,emp.FA_Name AS FA_Name
            -- Department
            ,dpt.Department_Name AS Dept_Name
            ,dpt.Department_City AS Dept_City
            ,dpt.Department_State AS Dept_State
            FROM
            gcp_flex_etl.trade trd
            -- Current Account Data
            INNER JOIN gcp_flex_etl.account_current acct ON (acct.Account_Number = trd.Account_Number)
            -- Current Financial Advisor
            INNER JOIN gcp_flex_etl.financial_advisor_current emp ON (emp.FA_Code = acct.FA_Code)
            -- Department
            INNER JOIN gcp_flex_etl.department dpt ON (dpt.Department_Code = emp.Department_Code)
            WHERE
            SUBSTRING(trd.Trade_Date,7,10) = '2020'
            GROUP BY
            -- Trade Information
            Account_Number
            ,Buy_Sell
            ,Security_Type_Child
            ,Security_Type_Parent
            ,Sector
            ,Trade_Date
            -- Account Information
            ,Account_Type
            ,Account_Name
            -- Financial Advisor Information
            ,FA_Code
            ,FA_Name
            -- Department
            ,Dept_Name
            ,Dept_City
            ,Dept_State""",
    use_legacy_sql=True,
    destination_dataset_table='gcp_flex_etl.trade_agg',
    write_disposition='WRITE_TRUNCATE',
    create_disposition='CREATE_IF_NEEDED',
    allow_large_results=True,
    dag=dag)

## Export trade_agg table to GCS
export_trade_agg_table = bigquery_to_gcs.BigQueryToCloudStorageOperator(
    task_id='export_trade_agg_table',
    source_project_dataset_table='gcp_flex_etl.trade_agg',
    destination_cloud_storage_uris=[current_bucket],
    export_format='CSV',
    dag=dag)

start >> archive_old_data >> load_account_current >> load_trade_agg >> export_trade_agg_table >> end
start >> archive_old_data >> load_financial_advisor_current >> load_trade_agg >> export_trade_agg_table >> end