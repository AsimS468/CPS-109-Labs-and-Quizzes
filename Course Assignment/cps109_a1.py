'''
    Creating and remembering profiles for accounts can be very difficult especially when you have a poor memory. With this in mind, I've decided
to create a program that allows you to save your data for your different accounts securely on your device where you can safely access them. This
program should be able to allow a user to create a profile where they can add details to it such as username, email, and password. Since creating 
good, strong passwords can be very difficult and can require a lot of brain power, my program should be able to generate passwords of varying 
complexities.

    My program will have 3 parts. Firstly, set of functions that can generate passwords that are simple, medium, and complex so the user can have
a password best suited for them. These passwords will be generated using words found in a pre-existing txt file and data in a set of predefined
lists. Of course, the user can also use a pre-existing password if they wish. Second, there will be a set of functions that will also be used for
allowing the user to name the profile and add relevant details such as usernames and emails. Since not all accounts require a username or email, 
the program will set *null* for profiles with no usernames or emails. Lastly, the program should hav some functions for writing the data into a 
csv file. These functions should print the data in the csv file, delete a profile from the csv file, or create a profile in the csv file.  
    
'''

import csv
import random 


allChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]
specialChars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", 
                "[", "{", "]", "}", "\\", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", " "]



'''
Function for selecting a random number between 0-61236 and getting the corresponding word from the words.txt file.
* Used for selecting a random line from the words.txt file to get the word on that corresponding line.
* Modifies: this.
* Effects: randomly selects a number between 0-61236 and gets the corresponding word from the words.txt file

'''
def getRandWord():
    wordNum = random.randint(0, 61236) #Randomly selects a number between 0-61236 (there are 61237 words in the file)
    fileOfWords = open("words.txt", "r") #Open the words.txt file
    wordList = fileOfWords.readlines() #Convert the data in the words.txt file into a list
    return wordList[wordNum].strip() #Return the word at index wordNum, strip() function strips the newline from the word 

'''
Function for selecting a random number between 0-32.
* Used for selecting a random number to get the corresponding element from the specialChars list for tricky passwords.
* Modifies: this.
* Effects: randomly selects a number between 0-32.

'''
def getRandSpecChar():
    specCharNum = random.randint(0, 31) #Randomly selects a number between 0-31
    return specialChars[specCharNum] #Returns the character in the specialChars list at index specCharNum

'''
Function for selecting a random number between 0-9.
* Used for selecting a random single digit integer for the simple and tricky passwords.
* Modifies: this.
* Effects: randomly selects a number between 0-9.
     
'''
def getRandNum():
    return str(random.randint(0, 9)) #Return a randomly selected a number between 0-9 as a string

'''
Function for selecting a random number between 1-52.
* Used for selecting a random number to get the corresponding element from the allChars list for tricky passwords.
* Modifies: this.
* Effects: randomly selects a number between 1-52.

'''
def getRandLetter():
    letterNum = random.randint(0, 51) #Randomly selects a number between 0-51
    return allChars[letterNum] #Returns the character in the allChars list at index letterNum

'''
Function for generating a simple complexity password.
* Requires: 1-4 randomly generated numbers and 1-2 words from the words.txt file.
* Modifies: this.
* Effects: returns a string which includes 1-2 words from the words.txt file followed by 1-4 random integers.

'''
def simplePass():
    wordCount = random.randint(1, 2) #randomly selects a number between 1 and 2 to determine how many words will be used in the password
    numCount = random.randint(1, 4) #randomly selects a number between 1 and 4 to determine the number of digits used in the password
    passWords = "" #empty string for the words used in the password
    nums = "" #empty string for the number of digits used in the password

    for x in range(wordCount): #loop for getting a wordCount number of words
        passWords = passWords + getRandWord() 

    for i in range(numCount): #loop for getting a numCount number of digits
        nums = nums + getRandNum()
    
    simplePassword = passWords + nums #create a string that consists of all the words and all the digits

    if len(simplePassword) < 8: #If statement to make sure password is greater 8 characters
        return simplePass() #recursive call: re-runs the function if resulting string is under 8 characters
    else:
        return simplePassword #return the generated password

'''
Function for generating a medium complexity password.
* Requires: 1-4 randomly generated numbers, 1-3 randomly generated special characters, and 1-2 words from the words.txt file.
* Modifies: this.
* Effects: returns a string which begins with "_", followed by and 1-2 words from the words.txt file separated by "_", 1-3 randomly generated special characters,
  and 1-4 randomly generated numbers.

'''
def mediumPass():
    wordCount = random.randint(1, 2) #randomly selects a number between 1 and 2 to determine how many words will be used in the password
    specCharCount = random.randint(1, 3) #randomly selects a number between 1 and 3 to determine the number of special characters used in the password
    numCount = random.randint(1, 4) #randomly selects a number between 1 and 4 to determine the number of digits used in the password
    passWords = "" #empty string for the words used in the password
    specChars = "" #empty string for the special characters used in the password
    nums = "" #empty string for the number of digits used in the password

    for i in range(wordCount): #loop for getting a wordCount number of words separated by "_"
        passWords = passWords + getRandWord() + "_"

    for j in range(specCharCount): #loop for getting a specCharCount number of special characters
        specChars = specChars + getRandSpecChar() 

    for x in range(numCount): #loop for getting a numCount number of digits
        nums = nums + getRandNum()
    
    mediumPassword = passWords + specChars + nums #create a string that consists of all the words, special characters, and digits

    if len(mediumPassword) < 8: #If statement to make sure password is greater 8 characters
        return mediumPass() #recursive call: re-runs the function if resulting string is under 8 characters
    else:
        return mediumPassword #return the generated password

'''
Function for generating a complex password.
* Requires: 3-5 randomly generated characters, one underscore, 1-5 randomly generated numbers.
* Modifies: this.
* Effects: returns a string of 3-5 randomly generated characters, one underscore, 1-5 randomly generated numbers and is at least 8
  characters long.

'''
def complexPass():
    letters = "" #empty string for the letters used in the password
    numbers = "" #empty string for the numbers used in the password
    letterCount = random.randint(3, 5) #randomly selects a number between 3 and 5 to determine the number of letters in the password
    numCount = random.randint(1, 5) #randomly selects a number between 1 and 5 to determine the number of digits used in the password

    for i in range(letterCount): #loop for getting a letterCount number of letters
        letters = letters + getRandLetter()

    for x in range(numCount): #loop for getting a numCount number of digits
        numbers = numbers + getRandNum()

    complexPassword = letters + "_" + numbers

    if len(complexPassword) < 8: #If statement to make sure password is greater 8 characters
        return complexPass() #recursive call: re-runs the function if resulting string is under 8 characters
    else:
        return complexPassword #return the generated password

'''
Function for setting a password for a profile.
* Requires: a yes or no input, and either a numerical input or a string password.
* Modifies: this.
* Effects: returns a string that is either user inputted or generated.

'''
def setPass():
    password = "" #Create an empty string for a password
    print("Do you have a password in mind for this account?")
    passCheck = str(input("Input 'Yes' or 'No': ").lower()) 

    if passCheck != "yes" and passCheck != "no": #if statement to ensure the input is yes or no
        while True: #while loop will repeat until the input is yes or no
            passCheck = str(input("Invalid input! Input 'Yes' or 'No': ").lower())
            if passCheck == "yes" or passCheck == "no":
                break
            continue

    if passCheck == "yes": #if statement for if user wants to input their own password
        password = str(input("Input a password for this profile: "))
    else: #if user does not have their own password then the program will generate one
        i = ""
        print("Lets make a password for you!\nInput 1, 2, or 3.\n1. Simple Password\n2. Medium Password\n3. Complex Password")
        while True: #while loop to ensure the input is 1 2 or 3
            i = str(input())
            if i != "1" and i != "2" and i != "3":
                print("Invalid Password! \nInput 1, 2, or 3.\n1. Simple Password\n2. Medium Password\n3. Complex Password")
                continue
            elif i == "1": #if user inputs 1, call the simplePass() function
                password = simplePass()
                print("Your password is: " + password)
                break
            elif i == "2": #if user inputs 2, call the mediumPass() function
                password = mediumPass()
                print("Your password is: " + password)
                break
            elif i == "3":  #if user inputs 3, call the complexPass() function
                password = complexPass()
                print("Your password is: " + password)
                break
    return password 

'''
Function for setting a username for a profile.
* Requires: a yes or no input and a string input for a username.
* Modifies: this.
* Effects: returns either *null* or a user inputted string.

'''
def setUsername():
    username = "" #Create an empty string for a username
    print("Do you have a username for this account?")
    usernameCheck = str(input("Input 'Yes' or 'No': ").lower())

    if usernameCheck != "yes" and usernameCheck != "no": #if statement to ensure the input is yes or no
        while True: #while loop will repeat until the input is yes or no
            usernameCheck = str(input("Invalid input!\nInput 'Yes' or 'No': ").lower())
            if usernameCheck == "yes" or usernameCheck == "no":
                break
            continue

    if usernameCheck == "yes": #if input is yes, prompt the user to input their username
        username = str(input("Input a username for this profile: "))
    else:
        username = "*null*" #if input is no, set the username to *null*
    return username

'''
Function for setting an email for a profile.
* Requires: a yes or no input and a string input for a user name with at least one '@' and '.'.
* Modifies: this.
* Effects: returns either *null* or a user inputted string.

'''
def setEmail():
    email = "" #Create an empty string for an email
    print("Do you have an email for this account?")
    emailCheck = str(input("Input 'Yes' or 'No': ").lower())

    if emailCheck != "yes" and emailCheck != "no": #if statement to ensure the input is yes or no
        while True: #while loop will repeat until the input is yes or no
            emailCheck = str(input("Invalid input!\nInput 'Yes' or 'No': ").lower())
            if emailCheck == "yes" or emailCheck == "no":
                break
            continue

    #code to ensure an email is a valid email
    if emailCheck == "yes": #if input is yes, prompt the user to input their email
        email = str(input("Input your email for this profile: "))
        if (email.find("@") == -1) or (email.find(".") == -1): #if statement for if the inputted string does not have '@' or '.'
            while True: #continue looping through until the inputted string has '@' and '.'
                email = str(input("Invalid email address!\nEnter a valid email: "))
                if (email.find("@") == -1) or (email.find(".") == -1):
                    continue
                else:
                    break
    else: #set email to *null* if the user inputs no
        email = "*null*"
    return email

'''
Function for setting a profile name.
* Requires: a string input for a profile name.
* Modifies: this.
* Effects: returns a user inputted string.

'''
def setProfileName():
    profile = str(input("Input the account type for this profile: ")) #prompt user to input the name for a profile
    if profile == "": #if string is empty, inform the user that an empty string can not be inputted and prompt them to try again
        while True:
            profile = str(input("Account type cannot be empty!\nInput the account type for this profile: "))
            if len(profile) == 0:
                continue
            break
    return profile

'''
Function for reading the data in a csv file.
* Requires: a csv file.
* Effects: returns a 2d list.

'''
def csvReader(csvFile):
    with open(csvFile, mode='r') as file: #open a given csv file in reade mode
        csvRead = csv.reader(file) #read the csv
        csv2dList = list(csvRead) #convert the data in the csv into a 2d list
    return csv2dList

'''
Function for writing data in a csv file.
* Requires: a 2d list and a csv file.
* Modifies: csvFile.

'''
def csvWriter(csv2dList, csvFile):
    with open(csvFile, mode='w', newline='') as file: #open a given csv file in write mode
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv2dList) #write the data in the csv2dList into the csv file

'''
Function creating a profile.
* Requires: a 2d list.
* Modifies: csv2dList.
* Effects: returns a modified csv2dList.

'''
def createProfile(csv2dList):
    profile = [] #create an empty list for a profile
    name = setProfileName() #call the setProfileName() and set its output to 'name'
    username = setUsername() #call the setUsername() and set its output to 'username'
    email = setEmail() #call the setEmail() and set its output to 'email'
    password = setPass() #call the setPass() and set its output to 'password'
    
    profile.append(name) #add 'name' to the list
    profile.append(username) #add 'username' to the list
    profile.append(email) #add 'email' to the list
    profile.append(password) #add 'password' to the list

    csv2dList.append(profile) #add the list to a provided 2d list
    return csv2dList

'''
Function deleting a profile.
* Requires: a 2d list and an integer.
* Modifies: csv2dList.
* Effects: returns a modified csv2dList.

'''
def deleteProfile(csv2dList, n):
    csv2dList.remove(csv2dList[n]) #remove a sublist from a given 2d list at index n
    return csv2dList

'''
Function printing profiles.
* Requires: a 2d list.

'''
def printProfiles(csv2dList):
    profileNum = 0 #counter to assign a number to each sub list in a provided 2d list
    
    #program to output each sublist in their own line without the brackets
    for i in csv2dList: #loop through the list
        print(str(profileNum) + ". " + ", ".join(i)) #print the sublist without any brackets on a new line with a number at the start
        profileNum += 1 #increment the counter

''' Main Function of the program '''
def main():
    csvPath = 'profiles.csv' #set the csv path
    csvList = csvReader(csvPath) #read the csv
    while True: #while loop that will continue looping until the user ends the program
        print("\nWelcome to your Password Manager! What would you like do do?\n1. View your current profiles\n2. Create a new profile\n3. Delete a profile\n4. Exit program")
        mainMenuOption = str(input("Input 1, 2, 3, or 4: ")) #prompt the user to input 1, 2, 3 or 4

        if mainMenuOption != "1" and mainMenuOption != "2" and mainMenuOption != "3" and mainMenuOption != "4": #if statement to check if the user inputted 1, 2, 3, or 4
            while True: #if the user did not input a valid number, continue looping until they do
                mainMenuOption = str(input("Invalid input! Input 1, 2, or 3: "))
                if mainMenuOption == "1" or mainMenuOption == "2" or mainMenuOption == "3" or mainMenuOption == "4":
                    break
                continue
        elif mainMenuOption == "1": #option for viewing current profiles
            if len(csvList) == 1: #if statement to determine the csv file has any profiles
                print("You have no current profiles!") #if there are no profiles, inform the user
                continue #return to the main menu
            else: #if there are profiles, display them
                printProfiles(csvList)
                continue #return to the main menu
        elif mainMenuOption == "2": #option for creating a new profile
            createProfile(csvList) #call the createProfile() with the parameter csvList
            csvWriter(csvList, csvPath) #write the newly updated csvList to the csv file
            printProfiles(csvList) #display the newly updated csv file
            continue #return to the main menu
        elif mainMenuOption == "3": #option for deleting a profile
            if len(csvList) == 1: #if statement to determine the csv file has any profiles
                print("You have no current profiles!") #if there are no profiles, inform the user
                continue #return to the main menu
            else: #if there are profiles, continue through the deletion process
                profileNum = int(input("Input the number associated with the profile you want deleted: "))
                while True: #while loop to ensure the user inputs a valid number for a profile
                    if profileNum == 0:
                        profileNum = int(input("Invalid input! Input the number associated with the profile you want deleted: "))
                        continue
                    elif profileNum > len(csvList):
                        profileNum = int(input("No such profile exists! Input the number associated with the profile you want deleted: "))
                        continue
                    else: #if a valid number is inputted, delete that profile
                        csvList = deleteProfile(csvList, profileNum)
                        break
                csvWriter(csvList, csvPath) #update the csv file
                printProfiles(csvList) #print the newly updated csv file
                continue #return to the main menu
        elif mainMenuOption == "4": #option exiting the program
            print("Good bye!")
            break #exit the program

main() #run the main() function