import requests
import re
import os

#qq:1628708538

def main(username,password):
    chusihua = requests.get('https://bbs.binmt.cc/misc.php?mod=mobile',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
    saltkey = re.findall('saltkey=(.*?);',str(chusihua.headers))[0]
    formhash = re.findall('formhash=(.*?)&amp',str(chusihua.text))[0]
    #print(formhash)
    data = "formhash=" + formhash + "&referer=https%3A%2F%2Fbbs.binmt.cc%2Fk_misign-sign.html&fastloginfield=username&cookietime=31104000&username=" + username + "&password=" + password + "&questionid=0&answer=&submit=true";
    headers = {'Cookie': 'cQWy_2132_saltkey=' + saltkey,'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    #print(headers)
    denlu = requests.post('https://bbs.binmt.cc/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=&handlekey=loginform&inajax=1',data=data.encode("utf-8"),headers=headers)
    #print(denlu.text)
    cQWy_2132_auth = re.findall('cQWy_2132_auth=(.*?);',str(denlu.headers))[0]
    #print(cQWy_2132_auth)
    headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36","Cookie": "cQWy_2132_saltkey=" + saltkey + ";cQWy_2132_auth=" + cQWy_2132_auth}
    huo = requests.get('https://bbs.binmt.cc/k_misign-sign.html',headers=headers)
    formhash = re.findall('formhash=(.*?)&amp',str(huo.text))[0]
    data = {"operation":"qiandao","formhash": formhash,"Cookie":"cQWy_2132_saltkey=" + saltkey + ";cQWy_2132_auth=" + cQWy_2132_auth}
    headers = {"Cookie":"cQWy_2132_saltkey=" + saltkey + ";cQWy_2132_auth=" + cQWy_2132_auth,"Referer":"https://bbs.binmt.cc/forum.php","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    qd1 = requests.post('https://bbs.binmt.cc/k_misign-sign.html',data=data,headers=headers)
    qd = requests.get('https://bbs.binmt.cc/k_misign-sign.html',data=data,headers=headers)
    if '排名' in qd.text:jinb = re.findall('积分奖励</h4>.*?></span>',qd.text,re.S)
        jingbi = re.findall('value="(.*?)"',str(jinb))[0]
        print(f"{re.findall('签到排名：.*? ',qd.text)[0]}  获得金币：{jingbi}")
     else:
        print('签到失败')


if __name__ == '__main__':
    #账号
    username = os.environ["username"]
    #密码
    password = os.environ["password"]
    try:
        main(username,password)
    except Exception as e:
        raise e

