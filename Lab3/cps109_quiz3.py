#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 3: Password Changer

def charChecker(string, list):
    for char in list:
        if char in string:
            return True
    return False

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

lCaseChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

uCaseChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]

print("Input your new password:")
passw = input()

print("Confirm your password:")
confirmPassw = input()
if passw != confirmPassw:
    print("Passwords do not match!")
    exit()

elif len(passw) < 8:
    print("Password not complex enough!")
    exit()
elif charChecker(passw, num) == False:
    print("Password not complex enough!")
    exit()
elif charChecker(passw, lCaseChars) == False:
    print("Password not complex enough!")
    exit()
elif charChecker(passw, uCaseChars) == False:
    print("Password not complex enough!")
    exit()
else:
    print("Password changed successfully!")
