
import json
from time import sleep
from pyscript import document, fetch

## remove load banner
__terminal__.resize(100,100)
xx=document.getElementById('load')
xx.remove()
bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'

commands=["help","learn","about","extensions","coffee","joke","crt","exit"]
extensions=["AutoRepeater", "Js Link Finder", "GAP", "Piper", "Reflection", "Hackverter"]
learn_list={"TomNomNom":"TomNomNomDotCom","NahamSec":"nahamsec","Jason Haddix":"jhaddix","IppSec":"ippsec","John Hammond":"_JohnHammond","LiveOverflow ":"LiveOverflow","g0lden":"g0lden1"}
headers={'Accept':'application/json'}
BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
wildcardsubdomains = set()

def banner():
    print("Hello World !! Welcome to the matrix, Enter help to check the available commands")

def help():
    print("Available Commands :")
    print("====================")
    print("""  
    help -- displays available commands
    crt -- Extract Subdomains from Crt.sh
    joke -- Get a dad joke from icanhazdadjoke
    extensions -- Prints My Burp Suit Exetnsions
    learn -- Twitter accounts you must follow ;)
    about -- About Me 
    exit -- Exit the app
""")
def extension():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} My current Burp Extensions are :")
    for i in extensions:
        print(i)
def learn():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Resources to get started :\n\t1.PortSwigger Academy : https://portswigger.net/web-security\n\t2.Hacker101 : https://hacker101.com")

    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Content Creators to check out :")
    for key in learn_list:
        print(f"\t{blue}{key} {green}=> {yellow}https://youtube.com/@{learn_list[key]}" )

def about():
    print(f"{red}About{reset}")
    print(f"{blue}================{reset}")
    print("Hi 👋! I am Rohit a.k.a rohsec. I am a full time BugBounty Hunter and HackerOne Ambassador. I like identifying vulnerabilities and helping organizations reinforce their defenses. I have ethically hacked and secured various big techs such as Sony, RedBull, BBC, Dutch Government etc.")
    print(f"\n{yellow}Follow me:{reset}\n https://twitter.com/rohsec")

def coffee():
    print("If you appreciate the work I do, consider supporting my work! Your small contribution can help me continue my work for the community.")
    print(f"\n{yellow}Buy Me a Coffee{reset} 🙌{yellow} :{reset}\nhttps:/buymeacoffee/rohsec")

async def jokes():
    print(f"{yellow}[ {bblue}+{yellow} ]{reset} Fetching a joke for you...")
    resp= await fetch("https://icanhazdadjoke.com/",headers=headers)
    if(resp.ok):
        respjson=json.loads(await resp.text())
        print(f"{respjson['joke']}")
    else:
        print("Opps !! Techincal error occured, maybe try after some time !")


def crtsh():
    BASE_URL = "https://crt.sh/?q={}&output=json"
    subdomains = set()
    wildcardsubdomains = set()
    domain=input(f"{blue}Enter a domain:{reset} ")
    if(domain!=""):
        try:
            print(f" {yellow}[ {bgreen}+{yellow} ]{reset} Fetching Domains...")
            subdomains.clear()
            wildcardsubdomains.clear()
            response = req.get(BASE_URL.format(domain), timeout=25)
            if response.ok:
                content = response.content.decode('UTF-8')
                jsondata = json.loads(content)
                for i in range(len(jsondata)):
                    name_value = jsondata[i]['name_value']
                    if name_value.find('\n'):
                        subname_value = name_value.split('\n')
                        for subname_value in subname_value:
                            if subname_value.find('*'):
                                if subname_value not in subdomains:
                                    subdomains.add(subname_value)
                            else:
                                if subname_value not in wildcardsubdomains:
                                    wildcardsubdomains.add(subname_value)
                print("Fetched Subdomains\n============", '\n'.join(sorted(subdomains)))
                print("WildCard Subdomains\n============", '\n'.join(sorted(wildcardsubdomains)))
        except:
            print("Opps!! Techincial error occured. Please run the command again")
    else:
        print(f"{yellow}[ {bred}!{yellow} ]{reset} Invalid input !!")


def exitapp():
    print("Thank you for stopping by !! You will be now redirected to my twitter, connect to get in touch :)")
    sleep(2)
    document.location="https://x.com/rohsec"

def choice():
    inp=input(f"{blue}({bred}rohsec㉿hackinsec{blue}){green}-{blue}[~{blue}]{bgreen}#{reset} ")
    if(inp in commands):
        if(inp =="help"):
            help()
        elif(inp == "extensions"):
            extension()
        elif(inp == "learn"):
            learn()
        elif(inp== "about"):
            about()
        elif(inp=="coffee"):
            coffee()
        elif(inp=="joke"):
            await jokes()
        elif(inp=="crt"):
            crtsh()  
        elif(inp=="exit"):
            exitapp()

    else:
        print("Command not found !! Run the help command to get a list of available commands")

async def main():
    banner()
    while True:
        await choice()

await main()
