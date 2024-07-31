class grandfather():
	def g_property(self):
		print("Grand Father Property")

class father(grandfather):
	
	def property(self):
		print("Father Property")


class child(father):
	def c_property(self):
		print("child Property")

c = child()
c.c_property()
c.property()
c.g_property()

f = father()
f.g_property()

#vehicle
