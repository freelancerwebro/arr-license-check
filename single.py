from src.LicensePlateSplitter import LicensePlateSplitter
from src.ArrLicenseService import ArrLicenseService
import sys

if len(sys.argv) >= 2:
	splitter = LicensePlateSplitter(sys.argv[1])
	service = ArrLicenseService(splitter)
	service.process()

	if (service.getStatus() == True):
		print('Valid! => license: [' + sys.argv[1] + '], expiration: [' + service.getExpiration() + ']')
	else:
		raise Exception('Invalid transport license [' + sys.argv[1] + ']')
else:
	raise Exception('License plate is missing!')
	