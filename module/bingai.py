import os
import random
import sys
import time
import re
import requests
from bs4 import BeautifulSoup as par

def get_images(prompt):
    BING_URL = os.getenv("BING_URL", "https://www.bing.com")
    error_timeout = "Your request has timed out."
    error_redirect = "Redirect failed"
    error_blocked_prompt = ("Your prompt has been blocked by Bing. Try to change any bad words and try again.")
    error_being_reviewed_prompt = "Your prompt is being reviewed by Bing. Try to change any sensitive words and try again."
    error_unsupported_lang = "\nthis language is currently not supported by bing"
    ses: requests.Session = requests.Session()
    ses.headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language": "en-US,en;q=0.9","cache-control": "max-age=0","content-type": "application/x-www-form-urlencoded","referrer": "https://www.bing.com/images/create/","origin": "https://www.bing.com","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63","x-forwarded-for": f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"}
    cok="MUID=24E171CCAD23651D13A0624AAC2F64AE;SRCHD=AF=NOFORM;SRCHUID=V=2&GUID=BF8F86F4C7D6461192F9B98AB277E306&dmnchg=1;PPLState=1;_UR=cdxcls=0&QS=0&TQS=0;MUIDB=24E171CCAD23651D13A0624AAC2F64AE;ANON=A=889941B83D6BBECC0F66A715FFFFFFFF&E=1cf1&W=1;NAP=V=1.9&E=1c97&C=JrioqGaWfeMqmCGs6k7wwNrJ6lI89CDjV4OF0bxVk96u7YAg51IN1Q&W=1;GI_FRE_COOKIE=gi_fre=3;_RwBf=mta=0&rc=20&rb=20&gb=0&rg=0&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=1&l=2023-11-21T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=sapphire&c=true&t=5438&s=2023-09-28T11:14:55.7905620+00:00&ts=2023-11-22T07:55:08.2558684+00:00&rwred=0&wls=2&wlb=0&lka=0&lkt=0&aad=0&TH=&e=jcCvmh_c9J2NGggMc03l2DrvUAYQ5fjQV6PQdJvWUXj4nlpOJN64BASYnTKiaSssGLouvLnlNYXP_AD_2CvgUA&A=889941B83D6BBECC0F66A715FFFFFFFF;MMCASM=ID=D6C7BED0E96A4D1BA48CAFD8DDAFFFC3;_HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMS0zMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyLCJUb2JicyI6MH0=;_EDGE_S=SID=16494CFA7E4061C511325F247F3460B7;_SS=SID=16494CFA7E4061C511325F247F3460B7;_clck=11idkre%7C2%7Cfha%7C0%7C1421;CSRFCookie=341b09c5-7954-427d-8c8f-d803d3a9e6f6;SRCHUSR=DOB=20230908&T=1696090431000&POEX=W;_U=1UponapzQjAUCsqsm8pPBgdwQ1uu69eJWa1Hl1AFPpSfGrTArhlcckkF8VBdV3KDSjT8do2Ll-eWWGoE0U37YIgPCsUoVBVn44qqezncutqpoM8cT8FLUgaaTMS_sdeP0g6G6i-2OWfUfCYf3DxXjDqVimGqssADvE65TkjuKyEp3KHTzmr9M6T7dXWfWNuLzERbQD8SseB95BRvKLVL8tA;WLS=C=7993ea5bf7068659&N=;WLID=+I5NxOjoubmdkQq/qG/MBm3IBIxyTw67NMgVZ07/Im3nc/t2/eDhfXmY9efHCwe18YZlRa8Hj0DaV+C7eQsXlFm4F/2UeIMghVEEVP/sQvU=;KievRPSSecAuth=FABCBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACM/8njyZPAXCAAQ4yEaUtms9lGPTpwaIbgtwEqocgSx8sCuEJQIJ85At8Pv97nUqHSaAn+qXB/Bq7tu01iO64patK56CyV/6jlB5pWjlSZ1SC+GBP6msVwJ1Pa63ztskURrLNKBtB3hsidGJgPBBZRNrhNazXNwR0TO719TPIGLuRDY7Lf1RpkmoraPeUe+r9W8dVn7wvPz+GxgvkbQInz0PP3fD8nvfdpeHe4mADeTHbU8NMhGvOsu6/tO4prjmx7n2whhn8QrwXtI6JyYEnYKI/gme1w5OP5OIJQdl9sSm5ZLalLi0erM0GFX360ZTw4bvkguj5Cb5e2uYB0Mpl4xHMGEwDkSfS4DphURLBvwX1S2PrzAW2+Dzmp4/viL4qCnwebe/AJhPV2n2u/Uh1ebuz4XfWGTUbyq2ww5nrSaZjALMyNhfhqS7LkStsX1EgGql31Ka5/jMHYi5foSXca+Ukxurbrm2CD5HLnv96eSZb4Y7dsX6Mfkojy3HUohiVjj6eIBM+gyNNW15yneiUkIxgLjBmO7TsuQiNd6wS1owHGr7lgzGx1OM7BhXBRosZRHBtHuTIWCO5MZEpYHxKJbNT7rtOGwSJIZDIV6KH0prYF77K1fGLpWGykQtPVwSk7V3eP9aX/uc/OF+Y2rLjP10W/llnUaSQLPsoxQY+vbc82VVqgSzsQI3WNPDfFUFtToEM1nAlW94615v5X3IVTfy1/lCTP+hS+IeI8RHicdJ4bb3tVNB4O/kUY1QykwBv7mLrYEs7A8/T9A14yYvRYaTeSTr+2QErRXOzdPFqu4H9X8BTfFUrjG0ZLlYiv7VAq7GCWL3j1jF6BMP79SuO+AM4buf6naAeClaDoedOYnuEiPe/CnjkIliLeIrjeUU8lN1/DBJ+hWxYhTM58ElKj4iJCGYGDDM9IB5dONrnpkZu13DrdUOCf4yzzTC2jYuDnlZfGy9WLEZGd0rZ2grUBMTIMmuooyE+s0jZuiZLV8HrSV3dEFo7FAJUHsevuqHqjicR79NaQoERp916iqkQoY/IWpcoZN9KLoRI7xl2r6i7opVme5zENKGDSq45Hkli+9OwFKJQLJwUqh7l4Cj28uJwa9Va4uyqCLa7/vPPX0LvwI4gRPS7OmvnqrI18VNGyGAXXQLYROKWgowHMNtWB3Tu19jMsnxV0Fz4zqq88yo9g+z2EfUfV13OeFl0oDcDjN4u+Ya99CMN4eQi2pZqh8k/8wEmXnB0aAZWN0IIVKQYzplzRQTbOZn8SbOPLkA0m/8Wn4DT+jsJsTVIwxWG4BQm0CYkQhlTjOUJ/HHFIyXwBEa3VD5719kmtH3mvTix0k/nlntB23Qm2XPMaqOrl6OsiNz1SWZTPm6FAA8ViSy0AVK8M3IMO/9R7h3DgVjtQ==;_clsk=1l3hxy3%7C1701736184420%7C2%7C0%7Cz.clarity.ms%2Fcollect;SRCHHPGUSR=SRCHLANG=id&IG=1E8DA67D9F284A3DA3CCF3B5F9805204&CW=432&CH=688&SCW=432&SCH=688&BRW=MW&BRH=MT&DPR=1.7&UTC=420&DM=0&PV=9.0.0&HV=1701736189&PRVCW=432&PRVCH=688&WTS=63837332978"
    ses.cookies.update({'cookie':cok})
    url_encoded_prompt = requests.utils.quote(prompt)
    payload = f"q={url_encoded_prompt}&qs=ds"
    url = f"{BING_URL}/images/create?q={url_encoded_prompt}&rt=4&FORM=GENCRE"
    response = ses.post(url,allow_redirects=False,data=payload,timeout=200)
    if "this prompt is being reviewed" in response.text.lower():
        return {'error':error_being_reviewed_prompt}
    if "this prompt has been blocked" in response.text.lower():
        return {'error':error_blocked_prompt}
    if ("we're working hard to offer image creator in more languages" in response.text.lower() ):
        return {'error':error_unsupported_lang}
    if response.status_code != 302:
        url = f"{BING_URL}/images/create?q={url_encoded_prompt}&rt=3&FORM=GENCRE"
        response = ses.post(url, allow_redirects=False, timeout=200)
        if response.status_code != 302:
            return {'error':302}
    redirect_url = response.headers["Location"].replace("&nfy=1", "")
    request_id = redirect_url.split("id=")[-1]
    ses.get(f"{BING_URL}{redirect_url}")
    polling_url = f"{BING_URL}/images/create/async/results/{request_id}?q={url_encoded_prompt}"
    start_wait = time.time()
    while True:
        response = ses.get(polling_url)
        if response.status_code != 200:
            return {'error':200}
        if not response.text or response.text.find("errorMessage") != -1:
            time.sleep(1)
            continue
        else:
            break
    image_links = re.findall(r'src="([^"]+)"', response.text)
    normal_image_links = [link.split("?w=")[0] for link in image_links if not "svg" in link.split("?w=")[0]]
    return {'author':'Muhammad Idris','result':normal_image_links}