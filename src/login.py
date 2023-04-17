import discord
import os
class Login:

    def __init__(self):
        # Make the root directory Lucy-Umbra
        parent = os.getcwd()
        print(parent)
        # Get the path to the files folder
        self.client = None
        try:
            self.files = os.mkdir(parent + "/files")
        except:
            pass

    def fileSearch(self):
        try: 
            print("Searching for Token...")
            login = open("files/login.txt", "r")
            print("Token found.")
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
    

    # def nameSearch(self):
    #     try:
    #         print("Searching for Name...")
    #         name = open("files/name.txt", "r")
    #         print("Name found.")
    #         for line in name:
    #             name = line
    #         name.close()
    #         return name

    #     except:
    #         print("There is no Name saved.")
    #         print("Accessing name.")
    #         name = self.client.user 
    #         print(name)
    #         name = open("files/name.txt", "x")
    #         name.write(name)
    #         name.close()
    #         return name
    
    def login(self):
        token = self.fileSearch()
        intents = discord.Intents.all()
        intents.message_content = True
        self.client = discord.Client(intents=intents)
        self.client.run(token)
        # print("name")
        # name = self.nameSearch()
        


