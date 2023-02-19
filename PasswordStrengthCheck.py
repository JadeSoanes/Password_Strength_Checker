#import the relevant packages

import hashlib
from urllib.request import urlopen
import random

#create a handfulf of functions at the start to use in the main code

#a list of potential changes to the password to improve it
improvement_list = ("TIP: Try adding a number in the middle.", "TIP: Try a list of three random words instead.", "TIP: Consider adding special characters to your password.", "TIP: Avoid using personal information in a password.", "TIP: Avoid common sequences like '123' or '111'.", "How about making a password using the first letter of a sentence you will remember?", "TIP: Try making your password longer, longer passwords tend to be more secure.")
#create function called 'readworldlist()' to read url files

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile

#hash function makes the password as a parameter and returns to us a 'hash' of the password

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

#brute force fuction goes through the list of passwords and hashes each of them - it then compares the
#hash of the password that has been inputted into the hash of each password on the list
#output will print whether or not password is easy to guess or not. If it is it will suggest a random improvement

def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print(" This is not a strong password \n Consider changing your password, it is very common and easy to guess!\n", random.choice(improvement_list))
            # If the password is found then it will terminate the script here
            exit()

#creating the variable and storing list of passwords from a variable url

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = input("Welcome to the password strength checker, enter your password to discover how strong it is... ")
actual_password_hash = hash(actual_password)
 
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')


# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("This password is not one of the 12,000 most common passwords so is likely to be harder to be harder to crack. Congratulations! \n However always be viligant and do not share your password with anyone!")
 