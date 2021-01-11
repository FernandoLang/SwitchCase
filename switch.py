#Basically, check if the switcher passed in the constructor is equal a comparer, if yes
#execute the function with or whithout arguments.
#if no case is executed, case else excute default function

class Switch:
	def __init__(self, switcher):
		self.switcher = switcher
		self.__p = False

	def case(self, comparer, function, args = None ):
		if self.switcher == comparer:
			if args != None:
				function(args)
				self.__p = True
			else:
				function()
				self.__p = True

		else:
			pass

	def case_else(self, function, args=None):
		if self.__p == False:	
			if args != None:
				function(args)
			else:
				function()
		else:
			pass