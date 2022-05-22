#find vowels in a string
input_string =input('Enter the string :')
vowels = "AaEeIiOoUu"
 
Vowel_found = [char for char in input_string if char in vowels] 
print('no of vowels found =',len(Vowel_found)) 
print('Vowels found = ',Vowel_found) 
      