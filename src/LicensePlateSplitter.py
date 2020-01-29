from src.LicensePlateValidator import LicensePlateValidator

class LicensePlateSplitter:
	def __init__(self, licensePlate):
		validate = LicensePlateValidator(licensePlate)
		if (validate.check()):
			parts = licensePlate.split('-')
			self.cty = parts[0]
			self.no = parts[1]
			self.lit = parts[2]
		else:
			raise Exception('Invalid license plate: ' + licensePlate)