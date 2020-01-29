import re
import src.config.core as config

class LicensePlateValidator:
	def __init__(self, licensePlate):
		self.licensePlate = licensePlate

	def check(self):
		if (re.match(config.regex['licensePlate'], self.licensePlate)):
			return True
		else:
			return False