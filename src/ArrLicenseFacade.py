from src.LicensePlateSplitter import LicensePlateSplitter
from src.ArrLicenseService import ArrLicenseService

class ArrLicenseFacade:
	def __init__ (self, licensePlate):
		self.licensePlate = licensePlate

	def process(self):
		splitter = LicensePlateSplitter(self.licensePlate)
		service = ArrLicenseService(splitter)
		service.process()

		if (service.getStatus() == True):
			print('Valid! => license: [' + self.licensePlate + '], expiration: [' + service.getExpiration() + ']')
		else:
			raise Exception('Invalid transport license [' + self.licensePlate + ']')

