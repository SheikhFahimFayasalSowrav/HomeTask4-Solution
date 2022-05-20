'''
You have deposited 20,000 BDT in bank for a compound interest of 5% per year.
Which means, after one year your balance will be your principal + profit.
For the next year (principal + profit) will be counted as your new principal and
profit will be calculated on your new principal. And this will go on. What will be
your money after 4 years.
[Don’t use the formula C=P(1+r/100)n] [Use in-Place operator]
'''
#SOLUTION
C = 20000
# After 1st year:
C += C * 0.05
# After 2nd year:
C += C * 0.05
# After 3rd year:
C += C * 0.05
# After 4th year:
C += C * 0.05
print('After 4 years the amount will be: ',C)

'''
Take all the following inputs of a user: Name, Birth year, Nationality, 
University/College Name, Living Country, Male/Female, and Mobile number (11 digit). 
DO NOT USE ANY IF ELSE or Advance CODE

Then, give a output of his/her profile like following output 👇

Name: Inputted Name here
Age: *** years
Nationality: ** {Capital}
University/College: ***
Current Location: Inputted living country name
Mobile Number: +8801*********
Gender: True (if male), False (if female)
'''

Name= input('Enter Name: ')
birthyear = int(input('Enter birth year: '))
sNationality = input('Enter Nationality: ')
sUniversity = input('Enter University/College: ')
sCurLocation = input('Enter Current Location: ')
sMobileNumber = input('Enter Mobile Number: +88')
sGender = input('Gender: male or female:').lower()

print('--------------------------------------------')

print('Name: '+ sName)
print('Age:', 2022-birthyear, 'years old')
print('Nationality: '+ sNationality.upper())
print('University: '+ sUniversity)
print('Current Location: '+ sCurLocation)
print('Mobile Number: +88'+ sMobileNumber[0:11])
print('Gender: ', 'male' == sGender)

