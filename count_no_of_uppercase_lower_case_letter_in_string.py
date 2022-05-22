#Count Total numbers of upper case and lower case characters in input string
string = input('Please enter the string: ')
upper_case= 0
lower_case = 0
     
for char in string:
 if char.isupper():
    upper_case+=1
 elif char.islower():
    lower_case+=1
        
print (" Total Upper case characters  : ", upper_case)
print ("Total Lower case Characters : ", lower_case)