# Import the csv module
import csv

# Import the json module
import json

# Create an empty list of users whose passwords have been compromised
compromised_users = []

# Open up the passwords.csv file as a password_file object
with open('passwords.csv') as password_file:
  # Pass the password_file object holder to the CSV reader for parsing
  password_csv = csv.DictReader(password_file)
  # Iterate through each of the lines in the CSV
  for row in password_csv:
  # Save each row of the CSV in a tempoaray variable
    password_row = row
  # Add each username to the list of compromised_users
    compromised_users.append(password_row['Username'])
  # Printing to check the compromised usernames were added
  print(compromised_users)

  # Start a new with block, opening a file called compromised_users.txt in write mode and save the file object as compromised_user_file
  with open('compromised_users.txt', 'w') as compromised_user_file:
    # Iterate over each of your compromised_users
    for compromised_user in compromised_users:
      # Write the username of each compromised_user in compromised_users to compromised_user_file
      compromised_user_file.write(compromised_user)

  # Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message
  with open('boss_message.json', 'w') as boss_message:
    # Create a Python dictionary object within your with statement that relays a boss message called boss_message_dict
    boss_message_dict = {
      # Give the dictionary a "recipient" key with a value "The Boss"
      'recipient': 'The Boss',
      # Give the dictionary a "message" key with the value "Mission Success"
      'message': 'Mission Success'
    }
    # Write out the Python data object boss_message_dict to the file object boss_message using json.dump()
    json.dump(boss_message_dict, boss_message)

    # Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj
    with open('new_passwords.csv', 'w') as new_passwords_obj:
    # Save Slash Null's signature as a multiline string to the slash_null_sig variable
      slash_null_sig =  """
       _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

       """
       # Write slash_null_sig to new_passwords_obj
      new_passwords_obj.write(slash_null_sig)

