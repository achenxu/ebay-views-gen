import requests
from threading import Thread
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

requests.packages.urllib3.disable_warnings()

class Viewer(object):

    url = str(raw_input("What is the url of the item? :"))

    def view_item(self):
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }

        for i in range(50):
            try:
                r =  requests.get(self.url,headers=headers1,verify=False,timeout=5)
                if r.status_code == 200:
                    print (Fore.GREEN + "Viewed successfully")
                
            except Exception as e:
                print(e)


bots = []

for i in range(10):
    bot=Viewer()
    bots.append(bot)

threads = []
count = 1
for bot in bots:
    t = Thread(target=bot.view_item)
    threads.append(t)
    print(Fore.GREEN +" ** bot {} started  - MADE BY http://twitter.com/thebotsmith **".format(count))
    count += 1 
    t.start()

for t in threads:
    t.join()


print(Fore.GREEN + "ALL THREADS FINISHED SCRIPT READY TO EXIT")
exit = raw_input("Press any key to exit..")
