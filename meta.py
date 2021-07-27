import urllib.request, json 

ownerrank = "hypixel"
b = '1'
c = '2'
d = '3'
def getkarma():
    print('Enter username:')
    usernamekarma = input()

    with urllib.request.urlopen("https://api.slothpixel.me/api/players/" + usernamekarma) as url:
            data = json.loads(url.read().decode())
            print(data ["karma"])
def getrank():
    print('Enter username:')
    usernamerank = input()
    with urllib.request.urlopen("https://api.slothpixel.me/api/players/" + usernamerank) as url:
        data = json.loads(url.read().decode())
    if usernamerank == ownerrank: 
      print("OWNER")
    elif usernamerank != ownerrank:
      print(data["rank"])
def Skywars_stats():
    print('Select a stat')
    print('(1) Level')
    skywarsselection = input()
    if skywarsselection == b:
        print('Input Username')
        skywarslevelusername = input()
        with urllib.request.urlopen("https://api.slothpixel.me/api/players/" + skywarslevelusername) as url:
            data = json.loads(url.read().decode())
            print(data["stats"][0]["SkyWars"][0]["level"])






print('Select an option')
print('(1) User Karma')
print('(2) User Rank')
print('(3) Game options')
a = input()
if a == b:
    getkarma()
elif a == c:
    getrank()
elif a == d:
    print('What game')
    print('(1) Skywars')
    dselect = input()
    if dselect == b:
        Skywars_stats()
elif a != b:
    print("Wrong input")
#Fix error in getting skywars level 

