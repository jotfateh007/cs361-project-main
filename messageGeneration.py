import random
import main
import time
import messageLogging
import preferences

def generateMessage(username):
    with open('messages.txt', 'r') as mFile:
        messages = mFile.readlines()
    messages = [message.strip() for message in messages]
    inMessage = random.choice(messages)
    personalizedData = preferences.get_user_preferences(username)
    if personalizedData:
        person_name = personalizedData['name']
        personalizedMessage = inMessage.replace("{name}", person_name)
        print("Here is your personalized message:\n" + personalizedMessage)
        messageLogging.log_user_history(username, personalizedMessage)
        print("Returning to home page...")
        time.sleep(1.5)
        main.home_page(username)
    else:
        print("Please go and enter preferences first!")
        print("Returning to homepage...")
        time.sleep(1)
        main.home_page(username)
        return

def generateEmailMessage(username):
    with open('messages.txt', 'r') as mFile:
        messages = mFile.readlines()
    messages = [message.strip() for message in messages]
    inMessage = random.choice(messages)
    personalizedData = preferences.get_user_preferences(username)
    person_name = personalizedData['name']
    personalizedMessage = inMessage.replace("{name}", person_name)
    return personalizedMessage
