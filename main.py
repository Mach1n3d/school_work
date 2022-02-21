# Just going to create a program to work with reading and writing an absolute file path.

import os
import time

# Gathering all the user's information.

print("Let's start with some of your personal information.")
time.sleep(1)

first_name = input("Could I please have your first name?: ").lower()
time.sleep(.5)

last_name = input("And your last name?: ").lower()
time.sleep(1)

name = (first_name + " " + last_name).title()

print(f"Thank you {first_name.title()}!\n")
time.sleep(1)

print("Now we will get your address, city, state, zip code, and finally your phone number.")

address = input("What is your Address?: ").lower()
time.sleep(1)

city = input("What is your City?: ").lower()
time.sleep(1)

state = input("What is your State?: ").lower()
time.sleep(1)

zip = input("What is your Zip Code?: ")
time.sleep(1)

phone_number = input("And finally, what is your phone number(xxx-xxx-xxxx)?: ")
time.sleep(1)

print("Now let's put your information together for you.")

# Creating a readable format that the user can read on screen,
# Creating a comma separated format to be saved to file

full_address = (f"\n{name}\n{address.title()}\n{city.title()}, {state.upper()} {zip}\n{phone_number}")
save_format = (f"{name}, {address.title()}, {city.title()}, {state.upper()}, {zip}, {phone_number}")

print(full_address)
time.sleep(1)

# Getting the file name and absolute path to write the file to.

file_name = input("What would you like to name the file to save this information?: ")
time.sleep(1)

file_path = input("What is the file path for where you would like to save this information?: ")
user_path = file_path + "/" + file_name + ".txt"
time.sleep(2)

# Checking to see if the file path already has a file saved by that name, or if it is a new file.

if os.getcwd() != user_path:
    print("Your file path does not exist, so we will create a new file for you at that location.")
    with open(user_path, "w") as file_name:
        file_name.write(save_format)

elif os.getcwd() == user_path:
    print("Your file path already contains a file with that name.")

# Reading the file we just wrote to file to make sure it saved correctly.

time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("All done!\nNow to check that it saved properly, we will load the saved file.")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
print("Your newly saved file will be displayed below")
time.sleep(1)


with open(user_path, "r") as file_name:
    data = file_name.readlines()



print(data)





