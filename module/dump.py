import requests
import random
import re
from bs4 import BeautifulSoup as par
def random_number(maxs):
    return "".join([ str(random.randrange(0,9)) for x in range(maxs) ])

def number(full,maxs,data,ses):
    if len(full) > maxs:return
    try:
       # ses = requests.Session()
        res2 = ses.post("https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0",data=data,timeout=5)
        print(par(res2.text,"html.parser").text)
        if not "/login/identify/?ctx=recover&amp;search_attempts=1&amp;alternate_search=0&amp;toggle_search_mode=1" in str(res2.text):
            full.append(data['email'])
    except Exception as e:
            print(e)
            res1 = requests.get("https://mbasic.facebook.com/login/identify/")
            inputs = re.findall('<input.*?/>',res1.text)
            data = { re.search('name="(.*?)"',x).group(1):re.search('value="(.*?)"',x).group(1) if "value" in x else data['email'] for x in inputs}
            res2 = requests.post("https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0",data=data,timeout=5)
            if not "/login/identify/?ctx=recover&amp;search_attempts=1&amp;alternate_search=0&amp;toggle_search_mode=1" in str(res2.text):
                full.append(data['email'])
