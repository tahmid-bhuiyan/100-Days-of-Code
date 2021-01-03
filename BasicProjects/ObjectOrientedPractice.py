class Device:
	def __init__(self, name, watts=100, on=False):
		self.name = name
		self.watts = watts
		self.on = on
	def __str__(self):
		if self.on is True:
			return '(+%dW: %s)' % (self.watts, self.name)
		else:
			return '(+0W: %s)' % self.name
	def __repr__(self):
		return "Device('%s', %s, %s)" % (self.name, self.watts, self.on)
	def __eq__(self, other):
		if ((self.name==other.name)and(self.watts==other.watts)and
		(self.on==other.on)):
			return True
		else:
			return False
	def turn_on(self):
		self.on = True
	def turn_off(self):
		self.on = False
	def toggle(self):
		if self.on == True:
			self.on = False
		else:
			self.on = True
class Outlet:
	def __init__(self, devices = None):
		if devices == None:
			self.devices = []
		else:
			self.devices = devices
	def __str__(self):
		bruh = self.devices
		why = []
		wow = ''
		for i in bruh:
			wow = Device.__str__(i)
			why.append(wow)
		wut = 'Outlet([' + (', '.join(why)) + '])'
		return wut
	def __repr__(self):
		watermelon = self.devices
		chickfila = []
		popeyes = ''
		for i in watermelon:
			popeyes = Device.__repr__(i)
			chickfila.append(popeyes)
		kfc = 'Outlet([' + (', ').join(chickfila) + '])'
		return kfc
	def __eq__(self, other):
		if self.devices == other.devices:
			return True
		else:
			return False
	def add_device(self, device):
		self.devices.append(device)
	def remove_device(self, name):
		sunshine = self.devices
		bruh = None
		for i in range(len(sunshine)):
			if name == sunshine[i].name:
				bruh = sunshine[i]
				del sunshine[i]
				break
		return bruh
	def turn_off_all(self):
		if self.devices is not None:
			for outlet in self.devices:
				outlet.turn_off()
	def max_watts(self):
		total_watts = 0
		for n in self.devices:
			total_watts += n.watts
		return total_watts
	def watts_now(self):
		total_watts = 0
		for n in self.devices:
			if n.on == True:
				total_watts += n.watts
		return total_watts
	def add_device(self, device):
		screwdriver = self.devices
		screwdriver.append(device)
		return self.devices

class Circuit:
	def __init__(self, outlets = None):
		if outlets is None:
			self.outlets = []
		else:
			self.outlets = outlets
	def __str__(self):
		if self.outlets is None:
			return 'Circuit([])'
		else:
			return 'Circuit({})'.format(','.join(self.outlets))
	def __eq__(self, other):
		if not isinstance(other, Circuit):
			return False
		else:
			return self.outlets == other.outlets
	def add_outlet(self, other):
		if isinstance(other, Outlet):
			self.outlets.append(other)
	def max_watts(self):
		if self.outlets is None:
			return 0
		else:
			total_watts = 0
			for outlet in self.outlets:
				total_watts += outlet.max_watts()
			return total_watts
	def watts_now(self):
		if self.outlets is None:
			return 0
		else:
			total_watts = 0
			for outlet in self.outlets:
				total_watts += outlet.watts_now()
			return total_watts
	def turn_off_all(self):
		if self.outlets is not None:
			for outlet in self.outlets:
				outlet.turn_off_all()