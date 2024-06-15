import os
import base64
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

# Set up Gmail API access
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Create a Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Compose the email
message = MIMEText("This is the email body text")
message['to'] = 'akshayprasad.psm@gmail.com'
message['subject'] = 'Subject of the email'

# Convert the email message to base64
raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

# Send the email
try:
    message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
    print(f"Message sent. Message ID: {message['id']}")
except HttpError as error:
    print(f"An error occurred: {error}")
