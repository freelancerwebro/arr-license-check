from src.ArrLicenseFacade import ArrLicenseFacade
import sys

if len(sys.argv) >= 2:
	arrLicense = ArrLicenseFacade(sys.argv[1])
	arrLicense.process()
else:
	raise Exception('License plate is missing!')
	