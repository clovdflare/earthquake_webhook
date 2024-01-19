import requests,json,pytz,time
from websocket import WebSocket
from datetime import datetime as dt

webhook_url="discordのwebhookのurl"

magnitude = {"-1": "Unknown","10": "震度1","20": "震度2","30": "震度3","40": "震度4","50": "震度5弱","55": "震度5強","60": "震度6弱","65": "震度6強","70": "震度7"}
def earthquake():
     wssession=WebSocket()
     wssession.connect("wss://api.p2pquake.net/v2/ws")
     session=requests.Session()
     while True:
        jsondata=json.loads(wssession.recv())
        if jsondata["code"]==551:
            tsunami_status=jsondata["earthquake"]["domesticTsunami"]
            if tsunami_status=="None":
                tsunami="この地震による津波の心配は恐らく無いです"
            else:
                tsunami="この地震による津波の可能性があります、逃げてください"
            print(session.post(webhook_url,json={"content":"地震速報","username":"AIchanEarthQuakeNews","embeds":[{"title":f'{jsondata["earthquake"]["hypocenter"]["name"]}の地震速報📳',"description":f'<震源、深さなど>\n{jsondata["earthquake"]["hypocenter"]["name"]} M{jsondata["earthquake"]["hypocenter"]["magnitude"]} 震度{mt[str(jsondata["earthquake"]["maxScale"])]}\n・震源の深さ : {jsondata["earthquake"]["hypocenter"]["depth"]}km\n・発生時刻 : {jsondata["earthquake"]["time"]}\n\n緯度:{jsondata["earthquake"]["hypocenter"]["latitude"]}\n経度:{jsondata["earthquake"]["hypocenter"]}\n震度{magnitude[str(jsondata["earthquake"]["maxScale"])]}を**{jsondata["earthquake"]["hypocenter"]["name"]}}**で観測済。\n**{tsunami}**'}]},headers={"content-type":"application/json"}))

earthquake()