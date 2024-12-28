import json



def register_attendee_remove(events):
  event_name = input("Enter event name to register for: ")
  if event_name in events:
    attendee_name = input("Enter attendee name: ")
    events[event_name]['attendees'].remove(attendee_name)
    print(f"{attendee_name} registered for {event_name}")
  else:
    print(f"Event '{event_name}' not found.")


def register_attendee(events):
  event_name = input("Enter event name to register for: ")
  if event_name in events:
    attendee_name = input("Enter attendee name: ")
    events[event_name]['attendees'].append(attendee_name)
    print(f"{attendee_name} registered for {event_name}")
  else:
    print(f"Event '{event_name}' not found.")



def generate_summary(events):
  print("Event Summary:")
  for event_name, details in events.items():
    print(f"- {event_name}")
    print(f"  Date: {details['date']}")
    print(f"  Location: {details['location']}")
    print()



def load_from_file(filename):
  try:
    with open(filename, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return {}

def save_to_file(events, filename):

  with open(filename, 'w') as file:
    json.dump(events, file, indent=2)

# Initialize events dictionary
events = {}

# Load events from file (if exists)
events = load_from_file('events.json')


def dispaly_clint():
    while True:
        ask_student = input("+++++ event student system++++++\n"
                            "+++to attend to event click(1)+++\n"
                            "## to remove yourself from attend click(2)\n"
                            "+++to Display the events click(3)\n"
                            "save file(5) \n"
                    
                            "log out (4)\n")

        if ask_student == "1":
            register_attendee(events)


        if ask_student == "2":
            register_attendee_remove(events)




        elif ask_student == "5":
            save_to_file(events, 'events.json')



        elif ask_student == "3":
            generate_summary(events)

        elif ask_student == "4":
            print("goodbye....")
            break

