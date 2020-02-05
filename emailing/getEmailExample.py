## Get email example
import imapclient
import pyzmail

## Setup connection
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

## Authenticate
conn.login(username='email',
           password='password')

## Find an email folder
conn.select_folder(folder='INBOX', readonly=True)

## Search for emails
UIDs = conn.search(criteria=['*'])

## Get the email
raw_message = conn.fetch(messages=UIDs, data=['BODY[]', 'FLAGS'])

## Call pyzmail to parse the messsage
message = pyzmail.PyzMessage.factory(raw_message[29555][b'BODY[]'])

## Call various pyzmail functions
message.get_subject()
message.get_addresses('from')
message.get_address('to')

## Get the body of the email
message.text_part.get_payload().decode('UTF-8')
message.html_part.get_payload().decode('UTF-8')

## Close the connection
conn.logout()