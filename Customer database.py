# creates an empty list
names =[]
# iterates through the loop to receive customer's information
while True:
    # receives input for customer's name
    name = input("Your name please:")
    # program leaves the loop with user enters 'Done'
    if name == "Done".lower():
        break
    # user continues to enter their customer's telephone number and email address
    else:
        number = input("Tel No:")
        Email = input("Email Address:")
    # input is stored as key, value pairs in a dictionary
    result = {"Name":  name,
              "Tel":  number,
              "Email":  Email
              }
    # input result is stored in the empty list
    names.append(result)
    print()
# an empty list is created
list2 = []
#the initial variable is set to 1
i = 1
# iterating through a loop as long as i is less than or equal to length of the names listed
while i <= len(names):
    # input of each person is assigned under a number
    numbers = "Customer" + str(i)
    # 'label' of each customer is stored in the empty list
    list2.append(numbers)
    # i is incremented by 1
    i += 1
# each customer's label is attached to the information that was provided about them and stored in a dictionary
dic3 = dict(zip(list2, names))
# nested dictionary created above is printed
print(dic3)
# the statement below is printed
print("Do you want to search for a customer's information?")
# two options are provided in relation to the preceding question
print("1:Yes \n 2:No")
# user inputs their preferred option
ans = input("Input your answer")
# user enters the name of the customer whose information they are searching for if they choose 1
if ans == "1":
    Names = input("Whose info do you want to search for?")
    # iterates through the nested dictionary
    for val in dic3.values():
        # prints out the information of the customer if the name inputted is found in the dictionary and program ends
        if Names in val.values():
            print(val)
            break
    # subsequent message is printed if the name inputted is not found in the dictionary
    else:
        print("No record found")
# program also ends if the user does not want to look up any person's information in the database
elif ans == "2":
    print()
























