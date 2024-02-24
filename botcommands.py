# Importing necessary modules
from info import *
import os

# Setting up variables for group ID and group URL
request_id = "requests group id here (the group that you want the bot to work in)"
group_url = "The url of the group that you want the bot to work in"

# Function to handle commands received by the bot
def command(m): 
    # Check if the received command is "/start"
    if m.text == "/start":
        # Reply with a message containing the group join link
        bot.reply_to(m, f"Hi, if you want to use me please join here: {group_url}")
        bot.send_message(m.chat.id, f"This bot is created by: {bot_creator}")
    # Check if the received command starts with "/request"
    if m.text.split()[0] =="/request":
        # Check if the user is in the correct group to make requests
        if m.chat.id == request_id:
            # Call the request function to process the request
            request(m)
        else:
            # Reply with a message asking the user to join the correct group
            bot.reply_to(m, f"Please join this group and use me there: {group_url}")

# Function to handle requests made by users in the designated group
def request(m):
    try:
        # Extract the URL from the user's message
        URL = m.text.split()[1]
        
        # Execute a script with the URL as an argument
        result = os.system(f'bash dump.sh {URL}')
        
        # Check the result of the script execution
        if result == 0:
            # Reply with a success message if the script executed successfully
            bot.reply_to(m, "Successfully requested the dump!")
        else:
            # Reply with an error message if something went wrong during script execution
            bot.reply_to(m, "Something went wrong")
    except:
        # Reply with a message indicating that a URL is needed for the request
        bot.send_message(m.chat.id, "I need a URL to work")
