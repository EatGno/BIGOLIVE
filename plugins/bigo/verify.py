import requests
import time

def checkExists(siteId):
  url = "https://ta.bigo.tv/official_website/studio/getInternalStudioInfo"

  payload = "siteId=" + siteId + "&=verify%3D"
  
  headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.bigo.tv",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.bigo.tv/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "TE": "trailers"
  }

  response = requests.request("POST", url, data=payload, headers=headers)

  if response.json()['data']['sid'] is None:
    return False
  else:
    return True

def verify(siteId):
  url = "https://ta.bigo.tv/official_website/studio/getInternalStudioInfo"

  payload = "siteId=" + siteId + "&=verify%3D"

  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.bigo.tv",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.bigo.tv/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "TE": "trailers"
  }

  while True:
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.json()['data']['hls_src'] != "":
      return True
      # return response.json()['data']['hls_src'], response.json()['data']['siteId'], response.json()['data']['nick_name']

    print('Streamer is offline, rechecking in three minutes.')
    
    time.sleep(180)

def concurrentVerify(siteId):
  url = "https://ta.bigo.tv/official_website/studio/getInternalStudioInfo"

  payload = "siteId=" + siteId + "&=verify%3D"

  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.bigo.tv",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.bigo.tv/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "TE": "trailers"
  }

  while True:
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.json()['data']['hls_src'] != "":
      return True
    
    time.sleep(180)
