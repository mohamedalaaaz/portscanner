import json


def delete_user_from_json(filename, username_to_delete):
  try:
    # Open the JSON file and load its data
    with open(filename, 'r') as file:
      user_data = json.load(file)

    # Loop through the list and find the entry with the matching username
    for i, user in enumerate(user_data):
      if user['username'] == username_to_delete:
        # Remove the user from the list
        del user_data[i]
        print(f"User '{username_to_delete}' has been deleted.")

        # Save the updated list back to the file
        with open(filename, 'w') as file:
          json.dump(user_data, file, indent=4)
        return user_data

    print(f"User '{username_to_delete}' not found.")
    return user_data

  except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
    return []



def add_event(events):

  name = input("Enter event name: ").lower()
  date = input("Enter event date (YYYY-MM-DD): ").lower()
  location = input("Enter event location: ").lower()
  events[name] = {'date': date, 'location': location, 'attendees': []}
  return events

def register_attendee(events):
  event_name = input("Enter event name to register for: ")
  if event_name in events:
    attendee_name = input("Enter attendee name: ")
    events[event_name]['attendees'].append(attendee_name)
    print(f"{attendee_name} registered for {event_name}")
  else:
    print(f"Event '{event_name}' not found.")

def display_attendees(events):
  event_name = input("Enter event name to view attendees: ")
  if event_name in events:
    print(f"Attendees for {event_name}:")
    for attendee in events[event_name]['attendees']:
      print(f"- {attendee}")
  else:
    print(f"Event '{event_name}' not found.")

def generate_summary(events):
  print("Event Summary:")
  for event_name, details in events.items():
    print(f"- {event_name}")
    print(f"  Date: {details['date']}")
    print(f"  Location: {details['location']}")
    print(f"  Attendees: {len(details['attendees'])}")
    print()

def save_to_file(events, filename):

  with open(filename, 'w') as file:
    json.dump(events, file, indent=2)

def load_from_file(filename):
  try:
    with open(filename, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return {}

# Initialize events dictionary
events = {}

# Load events from file (if exists)
events = load_from_file('events.json')
file_to_delete_event=1
filename = 'admin.json'
def display():
  global events
  while True:
    choice=input("\nEvent Management System\n"
    " ....Add Event click (1)\n"
    "... Register Attendee click (2)\n"
    "...Display Attendees click(3)\n"
   " ..Generate Summary(4)\n"
   " ..Save to File (5)\n"
    "..to delete admin click(6)\n"
     "to delete event click(7)\n"            
    "..Exit click (8)\n"
    )

    if choice == '1':
      events = add_event(events)
    elif choice == '2':
      register_attendee(events)
    elif choice == '3':
      display_attendees(events)
    elif choice == '4':
      generate_summary(events)
    elif choice == '5':
      save_to_file(events, 'events.json')
    elif choice == "6":
      user_to_delte=input("type name of user to delete")
      delete_user_from_json(filename,user_to_delte)

    elif choice == "7":
      enter=input("enter the name of event..")
      file_name_delete="events.json"
      with open(file_name_delete,"r") as file:
        dat=json.load(file)
        if enter in dat:
          del dat[enter]
      with open(file_name_delete,"w") as file:
        json.dump(dat,file,indent=4)
        print("subject delted {}".format(enter))




    elif choice == '8':
      break
    else:
      print("Invalid choice.")

