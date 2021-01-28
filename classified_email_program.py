"""
classified_email_program.py

This program is designed to check the text of an email for classified words or phrases.

The core function(censor_email_text) does the following: 
If  classified words/phrases are found it flags the email as 'True', and censors the classified words/phrases.
If no classified words/phrases are found, the email is flagged as 'False' and the email text is unaltered.

"""
import re
from typing import List, Dict, Tuple
from builtins import str


def censor_email_text(email_text: str, classified_words: List[str])-> Dict[str, Tuple[bool, list, str]]:
    """
     Return a dictionary that contains the T/F flag and censored/uncensored email text. 
     Parameters:
     email_text: string that is the text of the email that needs to be checked and censored
     classified_words: List of words/phrases to check for censoring in email_text
    """
    result = {'flag': False, 'email': email_text}
    classified_regex = re.compile('|' .join(classified_words), re.IGNORECASE)
    if classified_regex.search(email_text):
        result['flag']=True
        result['email']= classified_regex.sub('*****', email_text)
    return result

def sanitize_user_words(user_words: str)-> List[str]:
    """ 
    Return a list of words to check for in the email.
    Parameters:
    user_words: string of user words that needs to be split and stripped of white space
    """

    split_words = user_words.split('#')
    sanitized_words = [x.strip() for x in split_words]
    return sanitized_words

def create_menu_with_options()->Dict[str, str]:
    """ Return a menu for use by menu interaction functions. """
    menu = {}
    menu['1'] = " Display preloaded sample text."
    menu['2'] = " Run censor function with preloaded sample text and new user provided classified words."
    menu['3'] = " Run censor function with new user provided text and new user provided classified words."
    menu['4'] = " Exit program."
    return menu

sample = """Four score and seven years ago our fathers brought forth on this continent, 
a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. 
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so 
dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a 
portion of that field, as a final resting place for those who here gave their lives that that nation might live. 
It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate
-- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, 
have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what 
we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to 
the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated 
to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which 
they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain 
-- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, 
for the people, shall not perish from the earth. Abraham Lincoln November 19, 1863"""

def process_user_menu_input(ans:str)->bool:
    """ 
    Process user input to execute specified function or break loop.
    Parameters:
    ans: string from user used to determin operation 
    """
    user_classified = []
    user_text = ""
    if ans == '1':
        print(sample)
        
    elif ans == '2':
        user_classified = sanitize_user_words(input("Please enter the words you wish to check for, separated by a #: "))
        result = censor_email_text(sample, user_classified)
        [print(category,': ', result[category]) for category in result]
        
    elif ans == '3':
        user_text = input("Please submit the email text you wish to check: ")
        user_classified = sanitize_user_words(input("Please enter the words you wish to check for, separated by a #:"))
        result = censor_email_text(user_text, user_classified)
        [print(category,': ', result[category]) for category in result]

    elif ans == '4':
        print("Thank you, goodbye!")
        return False

    else:
        print("Please make a valid selection, thank you.")

    show_menu()

def show_menu():
    """ Display menu to user with options. """
    menu = create_menu_with_options()
    end_flag = True

    while end_flag:
        print()
        [print(option, menu[option]) for option in menu]
        print()
        ans = str(input("Please enter a number to make a selection: "))
        end_flag = process_user_menu_input(ans)

if __name__ == '__main__':
    show_menu() 
