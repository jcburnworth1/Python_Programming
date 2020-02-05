## Send Email example
import smtplib

## Create connection to gmail server
conn = smtplib.SMTP('smtp.gmail.com', port = 587)

## Show connection type
type(conn)

## Establish connection to gmail server
conn.ehlo()

## Start Encryption
conn.starttls()

## Login into gmail - This will get blocked if gmail 'Less Secure App Access' is off
## See google app specific password for safety instead of using 'Less Secure App Access'
conn.login(user='email',
           password='passs')

## Send an email
conn.sendmail(from_addr='jcburnworth1@gmail.com',
              to_addrs='laurencgoeddel@gmail.com',
              ## Format for subject and body
              msg='Subject: Test Email\n\nHi Lauren\nFrom my python app\nLove J')

conn.quit()