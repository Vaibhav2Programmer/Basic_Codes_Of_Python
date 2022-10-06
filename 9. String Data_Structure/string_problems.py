#1. Program to check if the string is pallindrome or not.

''' Palindrome - string when written in reverse order also is same. ex. madam
first we convert the input string to lowercase or uppercase bcoz strings get compared according to ascii values so therefore it should
not give any wrong answer '''

mystr = "Apple"
mystr = mystr.upper()

revstr = reversed(mystr) # One way to do it

revstr1 = mystr[4::-1]
print(revstr1)

# print(mystr.split('A'))
# Now we convert into a list using list function or we can use split function which splits the string into a list

if list(mystr) == list(revstr1):
    print("It is a palindrome")
else:
    print("It is Not a Palindrome")

#2. Program to sort the words in alphabetical order

str1 = 'Vaibhav'

# str2 = sorted(str1)

str2 = str1.split()

str3 = sorted(str2)

for i in str2:
    print(i)