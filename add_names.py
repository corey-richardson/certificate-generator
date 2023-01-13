# add_names.py
# asks for 3 seperate inputs
# formats and writes to new line of csv file
# outputs confirmation message

# ctrl+c / keyboard interrupt to stop

with open("information.csv","a") as info_file:
    while True:
        name = input("child first name: ")
        guardian_name = input("guardian full name: ")
        email = input("email: ")
        to_write = f"\n{name.title()},{guardian_name.title()},{email.lower()}"
        info_file.write(to_write)
        print("added " + to_write)