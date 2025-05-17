import datetime
import os.path
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def create_event(user_input, message):

  creds = None

  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
      creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
      token.write(creds.to_json())



  try:
    match = re.match(r'\s+add\s+"(.+?)"\s+([\d\-T:]+)\s+([\d\-T:]+)', user_input)
    if match:
      title, start_time, end_time = match.groups()
    else:
      return "Invalid format. Please use: /calendar add <name of the event> <start of the event> <end of the event>"

    service = build("calendar", "v3", credentials=creds)

    event = {
      "summary": title,
      "start": {
        "dateTime": start_time + "+02:00",
        "timeZone": "Europe/Berlin",
      },
      "end": {
        "dateTime": end_time + "+02:00",
        "timeZone": "Europe/Berlin",
      }
    }

    event = service.events().insert(calendarId="primary", body=event).execute()

    return f"Event created:\n {event.get('htmlLink')}"

  except HttpError as error:
    return f"An error occurred while creating the event. :/\n Please try again later."


def calendar_handler(user_input, message):
  creds = get_stored_credentials()

  args = user_input.strip().split(" ", 1)
  if not args:
    return "Invalid format. Please use: /calendar [add <name of the event> <start of the event> <end of the event> / list <number of events>]"


  command = args[0].lower()

  if command == "add":
    return create_event(user_input, message)
  elif command == "list":
    count = int(args[-1])
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