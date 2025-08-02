import hashlib
import json
import pyfiglet
from colorama import init, Fore

init(autoreset=True)



ascii_banner = pyfiglet.figlet_format("HASH AUTENTIFICATION")
print(Fore.LIGHTRED_EX + ascii_banner)



def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


def register(username, password):
 try:
    with open("users.json", 'r') as file:
       users = json.load(file)
 except FileNotFoundError:
    users = {}

 if username in users:
    print(Fore.LIGHTWHITE_EX + "This user already exists")
    return
 
 hashed = hash_password(password)
 users[username] = hashed

 with open("users.json", 'w') as file:
    json.dump(users, file)

 print(Fore.LIGHTBLUE_EX + "Registraition successfully completed")
   

def login(username, password):
  try:
    with open("users.json", 'r') as file:
       users = json.load(file)
  except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "No registered users")
    return
 
  if username not in users:
    print(Fore.LIGHTRED_EX + "User is not found")
    return
 
  hashed = hash_password(password)
  if users[username] == hashed:
   print(Fore.LIGHTCYAN_EX + "Successful login")
  else:
   print(Fore.LIGHTWHITE_EX + "Wrong password")
   
  
def main():
  while True:
    print(Fore.LIGHTRED_EX + "\n1. Registration\n2. Login\n3. Exit")
    choise = input(Fore.LIGHTBLUE_EX + "Choose: ")

    if choise == "1":
      u = input(Fore.LIGHTRED_EX + "Username: ")
      p = input(Fore.LIGHTRED_EX + "Password: ")
      register(u, p)

    elif choise == "2":
      u = input(Fore.LIGHTRED_EX + "Username: ")
      p = input(Fore.LIGHTRED_EX + "Password: ")
      login(u, p)

    elif choise == "3": 
      ascii_banner1 = pyfiglet.figlet_format('Goodbye')
      print(Fore.BLUE + ascii_banner1)
      break

    else:
      print(Fore.LIGHTRED_EX + "Wrong dialig")

main()
      
      



