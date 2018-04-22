import random as ran
from time import sleep
# import emoji

HELP_ARRAY = ["Help", "Schools", "Classes", "Syllabus"]
HELP = "Some commands you can ask: Help | Schools | Classes | Syllabus"
KEYWORDS = ["Hello", "Hi", "sup", "Hey"]
GREETING_RESPONSES = ["sup bro", "hey", "*nods*", "hey you get my snap?"]
SCHOOL_LIST = ["UCB", "UCD", "UCI", "UCLA", "UCM", "UCR", "UCSD", "UCSF", "UCSB", "UCSC"]
CLASS_LIST = [["COMPUTER SCINECE", "CS10", "CS12", "CS14", "CS100", "CS111", "CS141"], 
			  ["ELECTRICAL ENGINEERING", "EE1A", "EE1LB", "EE20A", "EE100A", "EE120A", "EE120B"]]
DESIREDSCHOOL = []


def classAssistance(major, classNum):
	print "Welcome to the", major, "group messaging!!!!!!!"

	for i in range(len(CLASS_LIST[classNum - 1])):
		if i == len(CLASS_LIST[classNum - 1]) - 1:
			break
		else:
			print "\t", i + 1, "-", CLASS_LIST[classNum - 1][i + 1]
	group = raw_input("What class would you like to join? - ")
	print "Establishing connection"

	for x in range(0,3):
		sleep(0.3)
		print "."
	print "You are now connected to", CLASS_LIST[classNum-1][int(group)], "happy chatting!"#, emoji.emojize(":thumbs_up:")
	return
def majorAssistance():
	print "UCR Classes - "
	for i in range(len(CLASS_LIST)):
		print "\t", i + 1, "-", CLASS_LIST[i]

	classNum = raw_input("Which class (number) - ")

	if classNum.isdigit():
		if int(classNum) < 0 or int(classNum) > len(CLASS_LIST):
			print "Not within range"
			return
		elif classNum.isdigit():
			major = CLASS_LIST[int(classNum) - 1][0]
			print "Connecting you to UCR's", major, "group message"
			
			for x in range(0, 3):
				sleep(0.8)
				print "."

			classAssistance(major, int(classNum))
	else:
		print "not a valid input."
def schoolAssistance():

	if len(DESIREDSCHOOL) > 0:
		del DESIREDSCHOOL[:]

	print SCHOOL_LIST
	inList = True

	while inList:
		school = raw_input("Please select a school - ")
		for i in range(len(SCHOOL_LIST)):
			if school.lower() == SCHOOL_LIST[i].lower():
				print "Current School - ", SCHOOL_LIST[i]
				DESIREDSCHOOL.append(SCHOOL_LIST[i])
				return
		#if not in list
		if inList:
			cont = raw_input("Not a valid input. Enter e to exit, anything else to cont. ")
			if cont == "e":
				return "nothing"
def check_for_greeting(userQuestion):
	brokenDown = []
	for word in userQuestion:
		parsed = userQuestion.split(" ")
		brokenDown = parsed

	flag = False
	#print userQuestion
	while brokenDown[0] == "":
		brokenDown = brokenDown[1:]

	# for i in range(len(brokenDown)):
		# word = brokenDown[i].lower()
	# word = userQuestion.lower()
	# for j in range(len(HELP_ARRAY)):
	# 	# if word == HELP_ARRAY[j].lower():
	# 	# print "word - ", word
	# 	if word == HELP_ARRAY[j].lower():
	# 		flag = True
	# 		# print "Inside the 2nd loop word - ", word
	# 		if word == "schools" or (word == "classes" and len(DESIREDSCHOOL) == 0):
	# 			schoolAssistance()
	# 		elif word == "classes" and DESIREDSCHOOL[0] == "UCR":
	# 			majorAssistance()
	# 		elif word == "classes" and DESIREDSCHOOL[0] != "UCR":
	# 			print "As of now, we do not have the class schedule for", DESIREDSCHOOL[0], "\n\nTo change schools, enter schools option"
	# 		elif word == "help":
	# 			print HELP
	# 		elif word == "syllabus":
	# 			Syllabus()
	# 		return
	# 	elif word == KEYWORDS[j].lower():
	# 		flag = True
	# 		#IMPORTANT KEYWORDS AND HELPARRAY MUST BE SAME SIZE
	# 		print ran.choice(GREETING_RESPONSES)
	# 		return

	# if not flag:
	# 	print "Not a recgonized raw_input. Please Try again."
	# 	return

	for i in range(len(brokenDown)):
		word = brokenDown[i].lower()
		# for j in range(len(KEYWORDS)):
		for j in range(len(HELP_ARRAY)):
			if word == "schools":
			# if word == HELP_ARRAY[j].lower():
				schoolAssistance()
				return
			elif word == "classes":
				if word == HELP_ARRAY[j].lower():
					if len(DESIREDSCHOOL) == 0:
						schoolAssistance()
						if len(DESIREDSCHOOL) == 0:
							break
						elif DESIREDSCHOOL[0] == "UCR":
							majorAssistance()
					elif DESIREDSCHOOL[0] == "UCR":
						majorAssistance()
					else:
						print "No class data for", DESIREDSCHOOL[0]
					return
				elif word.lower() == KEYWORDS[j].lower():
					print ran.choice(GREETING_RESPONSES)
					return
	print HELP

def greetingMessage():
	print "Welcome to Find UC Kids. \n\nMy name is ChatBot, if you have any question, just ask away. \n\nOr type 'help' for a list of commands"
	x = raw_input("Message - ")

	return x
def main():
	flag = True
	while 1:
		if flag == True:
			check_for_greeting(greetingMessage())
			flag = False
		else:
			check_for_greeting(raw_input("Message - "))

main()

