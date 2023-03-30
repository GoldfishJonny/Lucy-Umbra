import discord
import os
class Login:

    def __init__(self):
        # Make the root directory Lucy-Umbra
        parent = os.getcwd()
        print(parent)
        # Get the path to the files folder
        try:
            self.files = os.mkdir(parent + "/files")
        except:
            pass

    def fileSearch(self):
        try: 
            print("Searching for Token...")
            login = open(self.files, "r")
            for line in login:
                token = line
            login.close()
            return token

        except:
            print("There is no Token saved.")
            print("Please enter your BOT TOKEN.")
            token = input("Token: ")
            login = open("files/login.txt", "x")
            login.write(token)
            login.close()
            return token
        
    
    def login(self):
        token = self.fileSearch()
        intents = discord.Intents.all()
        intents.message_content = True
        client = discord.Client(intents=intents)
        client.run(token)


