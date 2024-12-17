from os import system
from time import sleep
from datetime import datetime
from sys import stdout
try:
    from requests import get
except:
    system("pip3 install requests")
    system("python3 ads.py")









class color:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    false = '\033[0m'






def fetch_adsgram_data(a, b, c, bb):
    print (color.blue + " coded by @AirdropScript6")
    print (color.yellow + " Telegram : https://t.me/AirdropScript6")
    print (color.red + f" Count Of completed : {c}\n Balance : {bb}")
    url = f"https://api.adsgram.ai/adv?blockId={a}&tg_id={b}&tg_platform=android&platform=Linux+x86_64&language=en&is_premium=true&top_domain=timefarm.app"
    headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br, zstd", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,fa;q=0.7", "Cache-Control": "max-age=0", "Origin": "https://timefarm.app", "Referer": "https://timefarm.app/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Linux"'}
    response = get(url, headers=headers)
    if response.json()["banner"]["trackings"]:       
        t = datetime.now()
        print (color.blue + "[" + color.yellow + t.strftime('%H:%M:%S')+ color.blue + "]" + " " + color.underline + color.green + "Find Ads Wait To claim..." + color.false)
        for i in response.json()["banner"]["trackings"]:
            if i["name"] == "render":
                link = i["value"]
                q = get(link, headers=headers)
                sleep(4)
            if i["name"] == "show":
                link = i["value"]
                q = get(link, headers=headers)
                sleep(16)
            if i["name"] == "reward":
                link = i["value"]
                q = get(link, headers=headers)
                t = datetime.now()
                print (color.blue + "[" + color.yellow + t.strftime('%H:%M:%S')+ color.blue + "]" + " " + color.underline + color.green + "Successfully Claim 10,000 Point." + color.false)
        return True
    else:
        print (color.blue + "[" + color.yellow + t.strftime('%H:%M:%S')+ color.blue + "]" + " " + color.underline + color.red + "Error in Find Ads, Please Change Your iP (VpN) or wait 1 Day and Try Again." + color.false)
        return True











def main():
    c, bb = 0, 0
    system("clear")
    print (color.bold + """
░▀▀█░█▀█░▀█▀░█▀█
░▄▀░░█▀█░░█░░█░█
░▀▀▀░▀░▀░▀▀▀░▀░▀
╔══════════════════════════════════╗
║                                  ║
║  ZAIN ARAIN                      ║
║  AUTO SCRIPT MASTER              ║
║                                  ║
║  JOIN TELEGRAM CHANNEL NOW!      ║
║  https://t.me/AirdropScript6              ║
║  @AirdropScript6 - OFFICIAL      ║
║  CHANNEL                         ║
║                                  ║
║  FAST - RELIABLE - SECURE        ║
║  SCRIPTS EXPERT                  ║
║                                  ║
╚══════════════════════════════════╝\n""")
    print (color.yellow + " coded by @AirdropScript6")
    print (color.yellow + " Telegram : https://t.me/AirdropScript6")
    try:
        Pass = input(color.blue + "\nEnter the Password => " + color.purple)
        Uid = input(color.blue + "Enter the Your UserId Account => " + color.purple)
    except:
        main()
    a = "2994"
    b = "209684856"
    while True:
        system("clear")
        fetch_adsgram_data(a, b, c, bb)
        c += 1
        bb += 10000
        for i in range(420):
            stdout.write(color.bold + color.purple + f"           Loading... {i+1}/420\r")
            stdout.flush()
            sleep(1)








main()