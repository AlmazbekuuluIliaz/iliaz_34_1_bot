import requests

url = "https://www.prnewswire.com/news-releases/news-releases-list/"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.prnewswire.com/news-releases/',
  'Connection': 'keep-alive',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text) 