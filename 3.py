import json
import requests
#логины через запятую cyberian,DmitriyH,Fefer_Ivan
logins = input().split(",")
linkToApi = "https://codeforces.com/api/user.status?handle=";

def getCount(login):
  try:
    myset = set()
    response = requests.get(linkToApi + login)
    dtoJson = json.loads(response.text)
    
    #return dtoJson["result"]
    for i in dtoJson["result"]:
      name = str(i["problem"]["contestId"]) + i["problem"]["index"]
      if(i["verdict"] == "OK"):
        myset.add(name)
      
    return len(myset)
  except:
    return "Error. Maybe user not found"

for nick in logins:
  print(nick, getCount(nick));
