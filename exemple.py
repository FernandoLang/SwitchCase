from switch import Switch



#Function Exemple
def print_phrase(phrase = "No argument!"):
	print(phrase)



#the switcher will be used to make a cases
switcher = "print"

#phrase to print
phrase_to_print = "hello world" 

#Call the Switch class with your switcher
s = Switch(switcher)

#case Print, print_phrase is not called because the first letter is upperCase
s.case("Print", print_phrase, phrase_to_print)

#case print, print_phrase is called and phrase_to_print will be passed as an argument
s.case("print", print_phrase, phrase_to_print)

#case ballon, print_phrase is not called beacause the switcher and the 'ballon' are not the same
s.case("ballon", print_phrase, phrase_to_print)

#case print, but anything argument is not passed, print_phrase is called with default phrase defined in the method
s.case("print", print_phrase)

#case any case is true, case_else execute a default method (this is equivalent a Default Case)
s.case_else(print_phrase, "this is as default case")

############### OUTPUT CASE ANY IS TRUE ###############

#C:\User\****\Desktop\pythonExemple>python exemple.py

#hello world
#No argument!

#######################################################

############### OUTPUT CASE ANY IS FALSE ##############
#C:\User\****\Desktop\pythonExemple>python exemple.py

#this is as default case

#######################################################
