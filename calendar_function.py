import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


# def main():
#
#   creds = None
#
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#       creds = flow.run_local_server(port=0)
#
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())
#   #this prints out the next 10 events and what day they are on to the console
#
#   #This makes a test event onto my own calendar
#   try:
#     service = build("calendar", "v3", credentials=creds)
#
#     event = {
#       "summary": "Test",
#       "description": "",
#       "location": "Somewhere",
#       "colorId": 6,
#       "start": {
#         "dateTime": "2025-05-10T22:00:00+02:00",
#         "timeZone": "Europe/Berlin",
#       },
#       "end": {
#         "dateTime": "2025-05-10T22:10:00+02:00",
#         "timeZone": "Europe/Berlin",
#       }
#     }
#
#     event = service.events().insert(calendarId="primary", body=event).execute()
#
#     print(f"Event created {event.get('htmlLink')}")
#
#   except HttpError as error:
#     print(f"An error occurred: {error}")


def calendar_handler(user_input, message):
  creds = get_stored_credentials()

  args = user_input.strip().split(" ", 1)
  if not args:
    return "Invalid format. Please use: /calendar [add <name of the event> / list <number of events>]"

  count = int(args[-1])
  command = args[0].lower()

  if command == "add":
    pass
  elif command == "list":
    return get_events(creds, count)

def get_stored_credentials() -> Credentials:
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      raise Exception("No valid credentials found. Please authenticate.")
  return creds

def get_events(creds: Credentials, events_num: int = 5):
  try:
    service = build("calendar", "v3", credentials=creds)
    now = datetime.datetime.now().isoformat() + "Z"
    print(f"Getting the upcoming {events_num} events")
    events_result = (service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults=events_num,
            singleEvents=True,
            orderBy="startTime",
        ).execute()
    )
    events = events_result.get("items", [])

    if not events:
      return ["No upcoming events found."]
    events_str = [f"{event['start'].get('dateTime', event['start'].get('date'))} — {event.get('summary', 'No Title')}" for event in events ]
    return "\n".join(events_str)

  except HttpError as error:
    return[f"An error occurred: {error}"]