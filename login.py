savedusername = "Precious"
savedpassword = "Adjeley@16"
numberoftries = 3
 
while numberoftries != 0 :
    usernameinput =  input("Please enter your username: ")
    passwordinput =  input("Please enter your password: ")

    if (usernameinput == savedusername) and (passwordinput == savedpassword):
        print(f"Welcome Miss {savedusername}")
        break
    else:
        print("Sorry please try again")
        numberoftries = numberoftries - 1
print("Please contact your administrator")