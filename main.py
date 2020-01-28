import requests
import time
from bs4 import BeautifulSoup

checkNoUrl = 'http://213.177.9.75:9998/verf_nr'
baseUrl = 'http://213.177.9.75:9998/publica'
licenseJud = 'B'
licenseNr = '100'
licenseLit = 'BWS'
license = licenseJud + "-" + licenseNr + "-" + licenseLit

basePageResponse = requests.get(baseUrl)
basePageHeaders = basePageResponse.headers
basePageCookies = basePageResponse.cookies
basePageSoup = BeautifulSoup(basePageResponse.text, 'html.parser')

tokenInput = basePageSoup.input
tokenAttr = tokenInput.attrs
token = tokenAttr['value']

payload = {
	'_token': token,
	'jud': licenseJud,
	'nr': licenseNr,
	'lit': licenseLit,
}

response = requests.post(checkNoUrl, data=payload, cookies=basePageCookies, allow_redirects=True)
html = response.text
print("Checking license for: " + license)
soup = BeautifulSoup(html, 'html.parser')
messageSuccess = soup.select_one('.alert-success')

if (messageSuccess == None):
	messageSuccess = soup.select_one('.alert-danger')
	print("Invalid!")
else:
	date = messageSuccess.find('b')	
	print("Valid! => " + date.text)

