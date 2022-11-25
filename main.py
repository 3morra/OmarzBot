from pyrogram import *
from pyrogram import Client, filters
import Data
#you must install medules to can run this files > pip / pip3 install pyrogram , pip / pip3 install deep_translator



app = Client("BotOmarSession" , Data.Api_Id , Data.Api_Hash )

@app.on_message(filters.text)
async def ra(client , e):
    # print(api_hash)

    meeessg = f"""
    تم تشغيل بوتك بنجاح
    """
    if e.text == "g":
        client.send_message("me", meeessg)



def o1():
    api_id = input("\033[1;92mEnter Your Api Id : \033[1;93m")
    api_hash = input("\033[1;92mEnter Your Api Hash : \033[1;93m")
    Tokeen = input("\033[1;92mEnter Your Token Bot : \033[1;93m")
    fl = open("Data.py", "a")
    fl.write(f"#Hi bro , you bot data saved here ! \nToken = '{Tokeen}' \nApi_Id = '{api_id}' \nApi_Hash = '{api_hash}' \n#By developer omar (@DEV3M0RA) , (toolsegy)")
    print("\033[1;91mDone save data in the file and run your bot ..\033[1;93m")
    pl = dict(root='plugins')
    bot = Client('BotOmarSession', api_id, api_hash, bot_token=Tokeen, plugins=pl)
    bot.run()

def o2():
    import Data
    pl = dict(root='plugins')
    bot = Client('BotOmarSession', Data.Api_Id, Data.Api_Hash, bot_token=Data.Token, plugins=pl)
    bot.run()

def Gello():
    print("you can use ( 1 , 2) to run your bot : ")
    op = input("enter your option : ")
    if op == "1" :
        o1()
    elif op == "2":
        o2()

Gello()

