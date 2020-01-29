from src.LicensePlateSplitter import LicensePlateSplitter
import requests
from bs4 import BeautifulSoup
import src.config.core as config

class ArrLicenseService:
	def __init__(self, licensePlateSplitter):
		self.cty = licensePlateSplitter.cty
		self.no = licensePlateSplitter.no
		self.lit = licensePlateSplitter.lit

	def process(self):
		basePageResponse = requests.get(config.url['baseLicenseNo'])
		basePageHeaders = basePageResponse.headers
		basePageCookies = basePageResponse.cookies
		basePageSoup = BeautifulSoup(basePageResponse.text, 'html.parser')

		tokenInput = basePageSoup.input
		tokenAttr = tokenInput.attrs
		token = tokenAttr['value']

		payload = {
			'_token': token,
			'jud': self.cty,
			'nr': self.no,
			'lit': self.lit,
		}

		response = requests.post(config.url['checkLicenseNo'], data=payload, cookies=basePageCookies, allow_redirects=True)
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		messageSuccess = soup.select_one('.alert-success')

		if (messageSuccess == None):
			messageSuccess = soup.select_one('.alert-danger')
			self.status = False
		else:
			date = messageSuccess.find('b')	
			expiration = date.text
			self.status = True
			self.expiration = expiration.strip()

	def getStatus(self):
		return self.status

	def getExpiration(self):
		return self.expiration
