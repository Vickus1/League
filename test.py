import os
import requests
import json

GLOBAL_ENDPOINT = "https://global.api.pvp.net"
REGION_ENDPOINT = "https://na.api.pvp.net"
global API_KEY
API_KEY = 'RGAPI-740a8a8d-4997-4bec-98cb-d45feb9ba6ee'
global region
region = 'na'

def deldict(r, key):
    del r[key]
    return r

def findChamp():
    champlist = "/api/lol/static-data/{region}/v1.2/champion"
    champlist = champlist.format(region = region)
    payload = {'api_key' : API_KEY}
    r = requests.get(GLOBAL_ENDPOINT+champlist, payload)
    js = r.json()
    deldict(js, 'version')
    deldict(js, 'type')
    listofChamp = list()
    for chond in js.values():
        for champID in chond.values():
            listofChamp.append({champID['id']:champID['name']})
    return listofChamp

def ChampSelect(idchamp):
    listofChamp = findChamp()

    for list in listofChamp:
        try:
            champ = list[idchamp]
        except KeyError:
            pass
    return champ

def freetoplaychamps(apikey, region):
    getchamp = "/api/lol/{region}/v1.2/champion"
    getchamp = getchamp.format(region= region)
    data = {'freeToPlay' : 'true',
            'api_key' : apikey}

    r = requests.get(REGION_ENDPOINT+getchamp, data)
    print (r.status_code)
    js = r.json()
    print (js)
    length = len(js['champions'])
    champnamelist = list()
    print ('Loading ....')
    for id in range(length):
        champid = js['champions'][id]["id"]
        champname = ChampSelect(champid)
        #print (champname)
        champnamelist.append(champname)
    for lists in champnamelist:
        print (lists)

def getSummonerID():
    print ("Please enter the summoner's name :")
    summonerName = input()
    extension = "/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}"
    extension = extension.format(region = region, summonerNames = summonerName)
    data = {'api_key' : API_KEY}
    r = requests.get(REGION_ENDPOINT+extension, data)
    js = r.json()
    try:
        summID = js[summonerName]['id']
        print (summID)
    except KeyError:
        print ('The summoner you are trying to look for does not exist')
        return
    return js[summonerName]['id']

#findChamp(API_KEY, region)
freetoplaychamps(API_KEY, region)
#getSummonerID()
