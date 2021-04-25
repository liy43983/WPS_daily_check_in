invite_userids = [244668941]

import json, os, time
import requests


sids = [
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
#     "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]
mk = 0
my_sid = os.environ["SID"]
my_code = os.environ["CODE"]
my_bark = os.environ["BARK"]

def request_re(sid, invite_userid, rep = 30):
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    r = requests.post( invite_url, headers={ 'sid': sid }, data={ 'invite_userid': my_sid, "client_code": my_code, "client": "wechat" } )
    js = json.loads(r.content)
    if js['msg'] == 'tryLater' and rep > 0:
        rep -= 1
        time.sleep(10)
        r = request_re(sid, invite_userid, rep)
    return r

for i in invite_userids:
    for j in sids:
        try:
            r = request_re(j, i)
            js = json.loads(r.content)
            if js['result'] == 'ok':
                mk += 1
        except:pass
            
print('成功邀请%d位好友'%(mk))   

BARK_URL = my_bark
if BARK_URL:
    text = 'WPS邀请好友任务：成功邀请到%d位好友'%(mk)
    bark_url = BARK_URL[:-1] if BARK_URL.endswith('/') else BARK_URL
    requests.get(bark_url + '/%s'%(text))
