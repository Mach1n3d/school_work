import time

print("Let's start with your name.")
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

full_address = (f"\n{address.title()}\n{city.title()}, {state.upper()} {zip}")
print(full_address)

phone =  input("And finally, what is your phone number(xxx-xxx-xxxx)?: ")
