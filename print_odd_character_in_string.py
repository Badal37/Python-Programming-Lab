#find the characters at an odd position in string input by User.
string = input("Enter the string : ")
 
outputString = ''
 
for i in range(len(string)):
    if(i % 2 == 0):
        outputString = outputString + string[i]
         

print("String after odd charcater :", outputString)