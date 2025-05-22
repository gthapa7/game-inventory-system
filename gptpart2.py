# 1. Mark Even and Odd
# Determine if a number is even or odd.
# def odd_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(odd_even(5))
# Write a program to check if a number entered by the user is even or odd.
# def odd_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("enter the number that you want to check : "))
# print(odd_even(n))
# Print all even numbers from 1 to 50.

# l = []
# for i in range(0,51,2):
#     l.append(i)
# print(l)

# Check whether the last digit of a number is even or odd.
# def last_digit_odd_even(n):
#     last_digit = abs(n) % 10
#     if last_digit % 2 == 0:
#         return "the last digit is even"
#     else:
#         return "the last digit is odd"
#     #input from the user
# n = int(input("enter the number : "))
# print(last_digit_odd_even(n))


# Determine if the sum of two integers is even or odd.
# def determine(a,b):
#     sum = a + b
#     if sum % 2 == 0:
#         return "the number is even"
#     else:
#         return "the number is odd"
# a = int(input("enter the first numbers : "))
# b = int(input("enter the second number: "))
# print(determine(a, b))

# Check if the product of two numbers is even or odd.
# def determine_odd_even(a,b):
#     product = a * b
#     if product % 2 == 0:
#         return "the number is even"
#     else:
#         return "the number is odd"
# a = int(input("enter the first numbers : "))
# b = int(input("enter the second number: "))
# print(determine_odd_even(a, b))


# Ask the user for a number and print "Even" if it's even and "Odd" if it's odd.
# def determine_odd_even(a):
#     if a % 2 ==0:
#         return "even"
#     else:
#         return "odd"
# a = int(input("enter the first numbers : "))

# print(determine_odd_even(a))



# Check if a number is divisible by 2 but not by 4.
# number = int(input("enter the number :"))
# if number % 2 == 0 and number % 4 != 0:
#     print("the number is divisible by 2 and not by 4")
# else:
#     print("the number doesn't meet the condtion")

# Given a list of numbers, print which ones are even.
# lst = [1,2,3,4,5,6,7,8,9]
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         print(f" {lst[i]} : even")
#     else:
#         print(f"{lst[i]} : odd")

# Count the number of even and odd numbers in a list.
# lst = [1,2,3,4,5,6,7,8,9]
# count_even = 0
# count_odd = 0
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1

# print(count_even)
# print(count_odd)


# Create a function that returns “Even” or “Odd” for any given integer.
# def check_even_odd(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# n = int(input("enter your number : "))
# print(check_even_odd(n))


# 2. Check the Status of Integer
# Categorize a number as positive, negative, or zero.
# number = int(input("enter the number : "))

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("the number is zero")


# Write a program to check whether a number is positive, negative, or zero.
# number = int(input("enter the number : "))

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("the number is zero")


# Ask the user for a number and print its status.
# number = int(input("enter the number : "))
# if number > 0 and number % 2 == 0:
#     print('the number is positive and even')
# elif number > 0 and number % 2 != 0:
#     print("the number is positive and odd")
# else:
#     print("the number is not both positive and even or odd")

# Count how many numbers in a list are positive.
# lst = [1,3,-1,-35,-99,-4,-3,5,6,8,9,-2]
# positive = 0 
# negative = 0 
# for i in range(len(lst)):
#     if lst[i] > 0:
#         positive += 1
#     else:
#         negative += 1
# print(positive)
# print(negative)



# # Find the sum of all negative numbers in a list.
# lst = [1,2,-1,4,-3,8,-11,-5,6,7,14]
# sum = 0
# for i in range(len(lst)):
#     if lst[i] < 0:
#      sum += lst[i]
#     else:
#         "the number is positive"
# print(sum) 
# Replace all negative numbers in a list with zero.
# lst = [1,2,-1,4,-3,8,-11,-5,6,7,14]
# for i in range(len(lst)):
#    if lst[i] < 0:
#       lst[i] = 0
# print(lst)
   

# Check if a number is positive and even.

# number = int(input("enter the number : "))
# if number > 0 and number % 2 == 0:
#     print('the number is positive and even')
# elif number > 0 and number % 2 != 0:
#     print("the number is positive and odd")
# else:
#     print("the number is not both positive and even or odd")

# Print all positive numbers from a given list.
# lst = [1,2,-1,4,-3,8,-11,-5,6,7,14]
# positive_number = []
# negative_number = []
# for i in range(len(lst)):
#     if lst[i] > 0:
#         positive_number.append(lst[i])
#     else:
#         negative_number.append(lst[i])
# print(positive_number)
# print(negative_number)

# Check whether two numbers are both positive or both negative.
# a = int(input("enter first the number : "))
# b = int(input("enter second the number :"))

# if a > 0 and b > 0:
#     print("both number are positive")
# elif a < 0 and b < 0:
#     print("both numbers are negative")
# else:
#     print("the number is zero")


#  ####

# a = int(input("enter first the number : "))
# b = int(input("enter second the number :"))

# if a > 0 and b > 0:
#     print("both number are positive")
# elif a < 0 and b < 0:
#     print("both numbers are negative")

# elif a > 0 and b < 0:
#     print("first is positive and second is negative")
# elif a < 0 and b > 0:
#     print("first is negative and second is positive")
# else:
#     print("the number is zero")



# Categorize a list of integers into positives, negatives, and zeros.
# lst = [1,2,-1,4,-3,0,8,0,-11,-5,0,6,7,14]
# positive= []
# negative= []
# zeros = []
# for i in range(len(lst)):
#     if lst[i] > 0:
#         positive.append(lst[i])
#     elif lst[i] < 0:
#         negative.append(lst[i])
#     else:
#         zeros.append(lst[i])
# print(positive)
# print(negative)
# print(zeros)

# Ask the user to input 5 numbers and classify them accordingly.

# positive= []
# negative= []
# zeros = []
# for i in range(5):
#     num = int(input(f"enter the number {i + 1} : "))
#     if num > 0:
#         positive.append(num)
#     elif num < 0:
#         negative.append(num)
#     else:
#         zeros.append(num)
# print(positive)
# print(negative)
# print(zeros)



# 3. Trouble with Angry Friends
# Solve a situation with specific rules (more logical thinking required).
# friend1_angry = input("is friend1 is angry/ (yes/no) : ")
# friend2_angry = input("is friend2 is angry (yes/no) : ")

# if friend1_angry == "yes" and friend2_angry == "yes":
#     print("peace")
# else:
#     print("still angry")





# If two friends are angry, and you say sorry to both, print "Peace", otherwise print "Still angry".
# friend1_angry = input("is friend1 is angry/ (yes/no) : ")
# friend2_angry = input("is friend2 is angry (yes/no) : ")

# if friend1_angry == "yes" and friend2_angry == "yes":
#     print("peace")
# elif friend1_angry == "no" and friend2_angry == "no":
#     print("still angry")
# else:
#     print("don't know")



# Two people are angry if they don’t get the same number of chocolates. Write code to fix the issue.
# Ask how many chocolates are available
# total_chocolates = int(input("Enter total number of chocolates: "))

# # Divide the chocolates equally
# each = total_chocolates // 2
# remainder = total_chocolates % 2

# # Give equal chocolates to both
# print(f"Each person gets {each} chocolates.")

# # Check if there is an extra chocolate left
# if remainder != 0:
#     print("One extra chocolate is left. They might still argue!")
# else:
#     print("Perfect! No one's angry.")




# If person A says "hi" and person B replies "bye", print "Conflict".
# person_A = input("(hi/bye) : ")
# person_B = input("(hi/bye) : ")
# if person_A == "hi" and person_B == "bye":
#     print("Conflict")
# elif person_A == "hi" and person_B == "hi":
#     print("perfect! NO conflict")
# else:
#     print("happy")

# Check if three friends all got equal gifts; if not, print "Jealousy".

# first = int(input("enter the number of gift 1st got  : "))
# second = int(input("enter the number of gift 2nd got  : "))
# third = int(input("enter the number of gift 3rd got  : "))
# if first == second == third:
#     print("happy")
# else:
#     print("jealousy")
# Determine if someone can make peace between two angry friends based on a condition.
# Condition: If one friend has a mood score below 5 (angry), but the other has a score above 7 (calm enough), print "You can help them reconcile!"
# Otherwise, print "Better not interfere."


# friend1_mood = int(input("enter the mood score based on 0 tp 10 : "))
# friend2_mood = int(input("enter the mood score based on 0 to 10 : "))
# if friend1_mood > 5 and friend2_mood < 7:
#     print("you can help them")
# elif friend1_mood < 5 and friend2_mood > 7:
#     print("you can help them")
# else:
#     print("better not interfere")

# Each friend has a temper level; if it crosses 7, they get angry. Print who’s angry.
# friendA = int(input("enter the temper level 0 to 10 of A : "))
# friendB = int(input("enter the temper of B level 0 to 10 : "))
# if friendA > 7 and friendB > 7:
#     print("all are angry")
# elif friendA > 7:
#     print(f"the angry one is friendA")
# elif friendB > 7:
#     print(f"the angry one is friend B")
# else:
#     print("all happy")
# Given moods (happy, angry, neutral) of 3 friends, print how many are angry.
# mood1 = input(" enter the mood (happy/angry/neutral) : ")
# mood2 = input(" enter the mood (happy/angry/neutral) : ")
# mood3 = input(" enter the mood (happy/angry/neutral) : ")

# count_of_angry = 0

# if mood1 == 'angry':
#     count_of_angry += 1
# if mood2 == 'angry':
#     count_of_angry += 1
# if mood3 == 'angry':
#     count_of_angry += 1

# print(count_of_angry)



# Create a function to calm down a friend if they are angry (mood = 'angry').
# def helper(status):
#     if status == 'angry':
#         return "we can help him"
#     else:
#         return "soory do not interfere"
# status = input("enter the status of your friend(angry/calm) : ")
# print(helper(status)) 



# # If one friend shouts, others get angry too. Simulate this in code.
# A = input("if he shouts (yes/no) : ")
# B = input("if he shouts (yes/no) : ")
# if A == 'yes':
#     print(" B got angry")
# if B == 'yes':
#     print('A gots angry')
# if A == 'no' and B == 'no':
#     print("fine")



# Make all friends happy using a loop and conditionals.
# friends = {
#     "Alice": "angry",
#     "Bob": "neutral",
#     "Charlie": "happy",
#     "Dina": "angry"
# }

# print("Making all friends happy...\n")

# for name, mood in friends.items():
#     if mood != "happy":
#         friends[name] = "happy"
#         print(f"{name} was {mood}, now is happy.")
#     else:
#         print(f"{name} is already happy.")

# print("\nFinal moods:")
# for name, mood in friends.items():
#     print(f"{name}: {mood}")




# 4. Check for Equal Occurrences of ‘cat’ and ‘hat’ in a String
# statement = 'do you see cat inside cat the hat. i saw cat wearing hat inside the hat'
# count_cat = statement.count('cat')
# count_hat = statement.count('hat')
# if count_cat == count_hat:
#     print(True)
# else:
#     print(False)
# Write a program to count ‘cat’ and ‘hat’ in a string.

# statement = 'do you see cat inside cat the hat. i saw cat wearing hat inside the hat'
# count_cat = statement.count('cat')
# count_hat = statement.count('hat')
# if count_cat == count_hat:
#     print(True)
# else:
#     print(False)
# Check if both appear the same number of times.
# statement = "i found cat inside my hat yesterday but today i put hat on the cat head"
# count_cat = statement.count('cat')
# count_hat = statement.count('hat')
# if count_cat == count_hat:
#     print(" yes same number of times both appeaared ")
# else:
#     print("no numbers of appearance is different")
# Case-insensitive check for equal number of 'cat' and 'hat'.
# statement = "i found Cat inside my hat yesterday  Hat but today i put Hat on  hat cat the cat head".lower()
# count_cat = statement.count("cat")
# count_hat = statement.count('hat')
# if count_cat == count_hat:
#     print(True)
# else:
#     print(False)

# Print "Balanced" if both appear the same times, else print "Unbalanced".
# statement = 'do you see cat inside cat the hat. i saw cat wearing hat inside the hat'
# count_cat = statement.count('cat')
# count_hat = statement.count('hat')
# if count_cat == count_hat:
#     print("balanced")
# else:
#     print("unbalanced")


# # Allow the user to input a string and perform the check.
# dialogue1 =  input("A enter what you want to say: ").lower()
# dialogue2 = input("B enter what you want to say: ").lower()

# combined = dialogue1 + " " + dialogue2
# count_hat = combined.count("hat")
# count_cat = combined.count("cat")

# if count_hat == count_cat:
#     print(True)
# else:
#     print(False)



# # Ignore punctuation when checking counts.
# import string  # To access punctuation characters

# dialogue1 = input("A, enter what you want to say: ").lower()
# dialogue2 = input("B, enter what you want to say: ").lower()

# # Combine dialogues
# combined = dialogue1 + " " + dialogue2

# # Remove punctuation
# for punct in string.punctuation:
#     combined = combined.replace(punct, "")

# # Count 'cat' and 'hat'
# count_cat = combined.count("cat")
# count_hat = combined.count("hat")

# # Compare counts
# if count_cat == count_hat:
#     print(True)
# else:
#     print(False)



# # Count how many words contain ‘cat’ and how many contain ‘hat’.
# import string

# dialogue1 = input("A, enter what you want to say: ").lower()
# dialogue2 = input("B, enter what you want to say: ").lower()

# combined = dialogue1 + " " + dialogue2

# for punct in string.punctuation:
#     combined = combined.replace(punct, "")

# count_cat_word =0
# count_hat_word = 0
 

# # Split into words
# words = combined.split()

# for word in words:
#     if 'cat' in word:
#         count_cat_word += 1
#     if 'hat' in word:
#         count_hat_word += 1






# Replace every occurrence of ‘cat’ with ‘dog’ only if they are equal in number.

# Create a function to check this condition.

# Extend it to work with any two words given by the user.

# 5. Conditional Boolean Evaluation
# Check if a number is both even and greater than 10.
# number = int(input("enter the number that you want to check : "))
# if number % 2 == 0 and number > 10:
#     print("the number is both even and greater than 10")
# else: 
#     print(False)
# Verify if a character is a vowel and is lowercase.

# vowel = 'aeiou'
# text = 'hello' 
# for char in text:
#     if char in vowel:
#         print("there is a vowel")
#     else:
#         print("sorry7")

# text = 'hello'
# vowel = 'aeiou'
# for char in text:
#     if char in vowel and char.islower():
#         print("the character is lowercase vowel.")
#         break
# Return True if the number is in range 10–50 and divisible by 5.
# number = int(input("enter the number : "))
# if 10<= number <=50 and number % 5 == 0:
#     print(" yes ")
# else:
#     print(" no ")

# Ask the user two yes/no questions, return True if both are yes.
# A = input(" say yes if you love me (yes/no) : ")
# B = input(" say no if you love me (yes/no) : ")
# if A == 'yes' and B == 'yes':
#     print(True)
# else:
#     print(False)

# Given two booleans, print a message based on their value.
# a = True
# b = False

# if a and b:
#     print(True)
# elif a or b:
#     print(False)
# else:
#     print("no")

# Use not to check if a number is not divisible by 3.,
# num = 10
# if num % 3 == 0:
#     print("the number is divisible by 3 ")
# else:
#     print("the number is not divisible by 3")
# Check if either of two inputs is positive.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > 0 or b > 0:
#     print("At least one number is positive.")
# else:
#     print("Neither number is positive.")

# # Combine and, or, and not in a meaningful condition.
# num = int(input(" enter the number : "))
# if (num > 0 and num % 2 == 0 and not num % 3 == 0) or num > 100:
#     print("the condition is true")
# else:
#     print("the condition is not true") 
# Create a function that returns True if a name starts with a capital letter and ends with a vowel.
def check_name(name):
    vowels = "aeiouAEIOU"
    if name[0].isupper() and name[-1] in vowels:
        return True
    else:
        return False



# Evaluate a complex condition with multiple comparisons.


# 6. Print Characters at Even Indices in a String
# Write a program that prints characters at even indices in a string.

# Ask the user for a string and print characters at even indices.

# Create a function to return a string of characters at even indices.

# Given a string, replace odd index characters with *.

# Count how many characters are at even positions.

# Print the ASCII values of characters at even indices.

# Remove characters at even positions and print the new string.

# Use slicing to get every second character.

# Modify only even-positioned characters to uppercase.

# Ask for a sentence and apply the above logic.

# 7. Print Numbers in Decreasing Order
# Print numbers from 10 to 1.

# Take a number n and print from n to 1.

# Print all even numbers from 100 to 0.

# Use a while loop to count down from 50 to 10.

# Print all multiples of 3 in reverse from 30 to 3.

# Print all characters of a string in reverse order.

# Take user input and print numbers in decreasing order till 1.

# Print numbers from 20 to 1 skipping every other number.

# Create a reverse countdown timer.

# Create a function that takes two integers and prints numbers from the first to the second in decreasing order.

# 8. Jumping Through While
# Print numbers from 1 to 10 using a while loop.

# Use a while loop to print even numbers from 2 to 20.

# Print “Jump!” every third number from 1 to 15.

# Use a while loop to find the sum of the first 10 natural numbers.

# Count how many steps until a number becomes 1 by subtracting 1 in each step.

# Keep asking the user for a number until they type -1.

# Use a while loop to find the factorial of a number.

# Repeat a message until the user types "stop".

# Use a while loop to guess a secret number.

# Create a loop that doubles a number until it is more than 100.

# 9. Zero Converter
# Convert all 0s in a list to 1s.

# Replace all zeros in a string with the letter “O”.

# Count how many zeros are in a list.

# Replace zeroes in a matrix with dashes.

# If a number is zero, print “Nothing”, else print the number.

# Create a function that takes a list and replaces 0 with a given value.

# Find the index of all zeroes in a list.

# Add 1 to all zero values in a list.

# Use a loop to turn all zeroes in a string to underscores.

# In a dictionary, replace values that are 0 with "empty"
