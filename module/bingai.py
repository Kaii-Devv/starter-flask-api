import os
import random
import sys
import time
import re
import requests
from bs4 import BeautifulSoup as par

def get_images(prompt):
    cok = {
		"_C_ETH": "1",
		"_clck": "lu3cul|2|fjn|0|1519",
		"_clsk": "1aknbmi|1709121522100|2|0|x.clarity.ms/collect",
		"_EDGE_S": "F=1&SID=044FE29F48A066691184F6AC49186705&mkt=en-id&ui=en-us",
		"_EDGE_V": "1",
		"_RwBf": "mta=0&rc=20&rb=20&gb=0&rg=0&pc=20&mtu=0&rbb=0&g=0&cid=&clo=0&v=2&l=2024-02-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2023-12-04T16:38:01.9684070-08:00&rwflt=0001-01-01T16:00:00.0000000-08:00&o=0&p=sapphire&c=true&t=5438&s=2023-09-28T11:14:55.7905620+00:00&ts=2024-02-28T11:58:40.8776225+00:00&rwred=0&wls=2&wlb=0&wle=1&ccp=0&lka=0&lkt=0&aad=0&TH=&e=jcCvmh_c9J2NGggMc03l2DrvUAYQ5fjQV6PQdJvWUXj4nlpOJN64BASYnTKiaSssGLouvLnlNYXP_AD_2CvgUA&A=889941B83D6BBECC0F66A715FFFFFFFF",
		"_Rwho": "u=d",
		"_SS": "SID=044FE29F48A066691184F6AC49186705&R=20&RB=20&GB=0&RG=0&RP=20",
		"_U": "1-kma8vyI3Vvs-gIwWqHEbfT9ummyUchdLtcgeBJ1frvjXqO8hxjsCf_vzfi_xWQA4fHaQQ0_K9nM6wAU8yqqIRInTZuqV7vaQxbmNlsX5Fm2Zyq0nHY1_hh38o8ilrGEuonzREX3M7BqZ1oksjtEr3Elep1FpO0q0O1ZySrwY-xJcfQgxLR70vfrHdtFF6f1OSyNnK1uXP3QqD4HWCh58g",
		"ANON": "A=889941B83D6BBECC0F66A715FFFFFFFF&E=1d77&W=1",
		"CSRFCookie": "81498c5d-dd5b-4870-b81e-efb082339d07",
		"GI_FRE_COOKIE": "gi_prompt=4&gi_fre=1&gi_sc=2",
		"KievRPSSecAuth": "FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACLrvczk4P6u3CAS66L4Xlw5f21fRUKSRqnitWDkxFqKuRpYp/wo6gaLGUABFzdmNVYXoWQH72rG6k9a/lz7swlc8BbGih400bae7/P/SteIFkVhCAlnUnsqkHWRDE44nITaGWHe9Tofju7q7e2cauLlSvuQTOZ0mKPWMZmEEgOE1GtxCpYnlIDKnj2p8qr3ShhZKC1d8/3f+ubToUCbgF/gKJAqbAV7VfayyAV9p6TaJCuacEU5akSEvYRHdaYNhiLqOpzWan7UcF2tdbPhdCzYQE8exD5IfmtA/0vnelYceqlM2NnW/NvNMjEhRMz4MjAZb0TeM8fVuoiaX++849lizaEqWb6x9ifPbm2kG341RsdwEpRZgPutdtdMe4YeCb7K4Nqjx5vvQP5m/dBi9Ut0Obo1MqDwwxZAvhBRfuhsccdcp9Lg/Ba4SbtcaHwiuEFqiiva5g2V4dcf3AsdsnnXC/aYndIe6YXAik7upV5yOVzi1CKnGU1NqgaCJL3p50A6tzBo78OCUD3PdTqbWMBRwuBnTi13tZqkjmj9BkMMb/04Ib2KZg8SxSTHwq9PgixLX+Wa4p746ZBtvYUl0c7l9jGzcM+vl3qtd8YKo64TB2+WkDT1QgFCfJQ3oYxtCrSPLR5AB1Axc1aw0TKrmGe7Vx7YHoqeLqVMTb5JSz5g/3uugaVgHVBfY/1DSnw3Jn4khAe9K0M0/Ek8InpBL+Oloa7OZlsneSGbCtQWeY0z5i+Kblk1wVViPpo1tlYdH4jEh5Qi+WeQ1egwybqVYgsrnKrPssJyq6f5RFUfbZ/UFIUHEQ1Vnlcf7gnAZfEXcZ9ligXqj4TWPKe7ktMgBlczduVS6YchDQ/HjgGLpgz6FWD2cIMSvLdxupcleXZI7HcilAFZs0iPEVF1iH3bsP9+V4kZ3gAU9P8vN2Lx5Og6zwl87BXPipE3al2BpUqUpmLDJ4HTVgbohpLLqCK/5N0jEq4Z0lEIrgzgklmfywqeGB7m5CNWAMAGIrBrwLKfEEwpTu7DEWwbHdIgLaoXZAABG/9v39n6JEHPKDvE/Bz3iOLj9FXhDqbajeK8nPbMRl59EgmtJinR8yFFVPSwiCW2EBaUkn37VisEfeXjZdvuEI7uIS1P15F74sHLBfmIrhU0gK5FwY1sx6lGrSof5h3RTB1kqZL8UWVavFsnftVAQILcBDb5IhU+ZItWHKjeY4F9CwZRcoGNWiCbR/TpZUFGCmtXh5JRyHtWSg6SKDagmg4tfVaPpoBPo1tblVTgvPQfVEw9Pz1ftA0jWxI7FbvpJY5orLYWTsLcuytaI5zNRX/rs20MVF6NiybsfA+22VFi3Q4MK0HJ+u/lRvYPQdr/OHFYfsUnUWK20xSnC007EcO4UAGFk4EGWjd35gqC+oqUkN4IX+y+H",
		"MUID": "2E0656BE5769679A2153428D56D166F4",
		"MUIDB": "2E0656BE5769679A2153428D56D166F4",
		"NAP": "V=1.9&E=1d1d&C=RkXzqFUOu84n8aHgwYcclkEARIxUyF9PcmKMGoi_Wdw2ElIpsLMxMw&W=1",
		"PPLState": "1",
		"SRCHD": "AF=GENILP",
		"SRCHHPGUSR": "SRCHLANG=en",
		"SRCHUID": "V=2&GUID=6737954B755B4F468B3E3ECCE9AD6B1D&dmnchg=1",
		"SRCHUSR": "DOB=20240228&POEX=W&T=1709121519000",
		"WLID": "+I5NxOjoubmdkQq/qG/MBm3IBIxyTw67NMgVZ07/Im3nc/t2/eDhfXmY9efHCwe18YZlRa8Hj0DaV+C7eQsXlFm4F/2UeIMghVEEVP/sQvU=",
		"WLS": "C=7993ea5bf7068659&N="
	}

    BING_URL = os.getenv("BING_URL", "https://www.bing.com")
    error_timeout = "Your request has timed out."
    error_redirect = "Redirect failed"
    error_blocked_prompt = ("Your prompt has been blocked by Bing. Try to change any bad words and try again.")
    error_being_reviewed_prompt = "Your prompt is being reviewed by Bing. Try to change any sensitive words and try again."
    error_unsupported_lang = "\nthis language is currently not supported by bing"
    ses: requests.Session = requests.Session()
    ses.headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language": "en-US,en;q=0.9","cache-control": "max-age=0","content-type": "application/x-www-form-urlencoded","referrer": "https://www.bing.com/images/create/","origin": "https://www.bing.com","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63","x-forwarded-for": f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"}
    cok="MUID=1C46FC4FAD6E60C63978E863AC38612F;MUIDB=1C46FC4FAD6E60C63978E863AC38612F;SRCHD=AF=NOFORM;SRCHUID=V=2&GUID=4644DD3E3212499085EFDEFA20454D89&dmnchg=1;_UR=cdxcls=0&QS=0&TQS=0;_HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wMi0yNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyLCJUb2JuIjowfQ==;SRCHHPGUSR=SRCHLANG=id&IG=38BF7AF40E7349FCB587A4739FFB3343&CW=1164&CH=2114&SCW=1164&SCH=4050&BRW=S&BRH=T&DPR=3.0&UTC=420&DM=0&PV=9.0.0&HV=1708954612&PRVCW=1164&PRVCH=2114&WTS=63844551363;_EDGE_S=SID=1BC301261DE16C023C8215121CD26D54&mkt=id-id&ui=id-id;_clck=xc8uuz%7C2%7Cfjo%7C0%7C1520;CSRFCookie=cd6aeb39-7e5c-40df-9dfe-e2a581987501;ANON=A=889941B83D6BBECC0F66A715FFFFFFFF&E=1d78&W=1;NAP=V=1.9&E=1d1e&C=PV2WHIY0ndUIQsxL3YG2D32xTDsjRAQAGHE97pTlOfXG518_IKmtew&W=1;PPLState=1;KievRPSSecAuth=FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACD1ADJpvEmctCARrm3lQZ+to2zn+q/kgHPq4u0OHREEd0kwjYT3Mq4tN6buPIG7+9elLhi7tvDxR1LySHf7rb2cpQBa2RafEnHg+vxTtdC+MSchoWjGDVmD4Dr1xrUMZ0PTD3X4w64kUZbKpGhFL5huAtnj1LnfAWqxAe3UdI1DVOapf8YGh/I2ZsuxO+RjHt31cZm4aHun43OVFFuI5yifsrNZKEZmGo4VQ+6a147XeYG+J5ccAfztwJpkgG/MaIL4e4k1yJcBfz8zqBc9MXxU5D2JgBFxfyTpK05XMaARx1n/P6XVCVhU27Rp7fhOvhZPfuOKLXEPDpHUnrBOBQDeh8UDt1BcP5zuK5MmoKKSywDYQXWOuU6ssTuBuS7LV5DhdlyQN+NyhuE2057zOo7eouMwPwLlUWfCD/Id6heBMX8LGTuRKypftK4HvvqvcWG21GjwJdvY/+e4i+ehBbTftP55YNJv2XimIfpWsie+SBy/m4Sgun69Gwk30cSTF7sT8e7FRelwSD0zVJHLCtMgU5GyCZ9ZOTrgerbHmPk9PdhYT1c0ps3nDIPXuiDky5dZ0w8DxamV1YECOGjfsr4n2ObgGyMnVd547gaGoBLVldmgvG41Sgf9pU76XjVpuabC+D/rmyc+wxswCUcBQuoihXejCXQdTPcM6SNv5RuQTl8/uhwP3do+popGHVjpPDeZCevNk+DUY6Anl89UCYmOXn/3Rp8wPCOGT+lkOWukNTWLrpGqWEp47zb21R1jUM/BBtRoydLPQCcaSaqaZuO8zc0j//87op3zKGe2XKrnt8u4c6HY5ydvpP1McQ2hVw+gb7TzpOiZY+Dv7ynVaDNC9waUZsbKPvHJNgO/03dTpvfQbEUTRaGBM762Na/6drhYTr9JF4CQW1APLOKbgUsFwZSpXaE4SPa04p/SHy9Ox2hX5JmPIm1Kzts67iQlGRajb5KphnJj+i01JnB6jbCm/n3sVi1VflPdaB3d1NLn1Wv/RGt"
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