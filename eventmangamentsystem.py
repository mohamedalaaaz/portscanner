import json
import hashlib

import dd
import clint

# File to store user data
USER_FILE = "admin.json"

USER_STUDENT="student.json"
filename = 'admin.json'




def hash_password_stUdent(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to load users from the JSON file
def load_users_student():
    try:
        with open(USER_STUDENT, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save users to the JSON file
def save_users_student(users):
    with open(USER_STUDENT, "w") as file:
        json.dump(users, file, indent=4)


# Function to register a new user
def register_user_student(username, password):
    users = load_users_student()

    # Check if the username already exists
    if any(user["username"] == username for user in users):
        print("Username already exists!")
        return False

    # Add the new user
    hashed_password = hash_password_stUdent(password)
    users.append({"username": username, "password": hashed_password})
    save_users_student(users)
    print("User registered successfully!")
    return True


# Function to authenticate a user
def login_user_student(username, password):
    users = load_users_student()
    hashed_password = hash_password_stUdent(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            print("Login successful!")
            return True
    print("Invalid username or password!")
    return False




################################################admin




def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to load users from the JSON file
def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save users to the JSON file
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Function to register a new user
def register_user(username, password):
    users = load_users()

    # Check if the username already exists
    if any(user["username"] == username for user in users):
        print("Username already exists!")
        return False

    # Add the new user
    hashed_password = hash_password(password)
    users.append({"username": username, "password": hashed_password})
    save_users(users)
    print("User registered successfully!")
    return True


# Function to authenticate a user
def login_user(username, password):
    users = load_users()
    hashed_password = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            print("Login successful!")
            return True
    print("Invalid username or password!")
    return False



###############################################3333













while True:

  ask_user1 = input("===========Welcome EVENT USER INTERFACE =======\n"
                    "admin  click :1 \n"
                    "student click :2\n"
                    "log out :3 \n")
  if ask_user1 == "1":
      while True:
          choice = input("++++++admin++++\n"
                         "register click :1 \n"
                         "login :2\n"
                         "log out :3 \n")
          if choice == "1":
              username = input("Enter username: ")
              password = input("Enter password: ")
              register_user(username,password)
              print("Register been add ...{}".format(username))


          elif choice == "2":
              username1 = input("Enter username: ")
              password2 = input("Enter password: ")
              if login_user(username1, password2) == True:
                  dd.display()





          elif choice == "3":
              print("Exiting...")
              break
          else:
              print("Invalid choice! Please try again.")



  elif ask_user1 == "2":
      while True:
          choice = input("+++++clint manage system++++\n"
                         "register clint click :1 \n"
                         "login  clint:2\n"
                         "log out clint:3 \n")
          if choice == "1":
              username_student = input("Enter username: ")
              password_student = input("Enter password: ")
              register_user_student(username_student, password_student)


          elif choice == "2":
              username_student2 = input("Enter username: ")
              password_student2 = input("Enter password: ")
              if login_user_student(username_student2,password_student2)==True:
                  clint.dispaly_clint()













          elif choice == "3":
              print("Exiting...")
              break
          else:
              print("Invalid choice! Please try again.")




  elif ask_user1 == "3" :
    break
