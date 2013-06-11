#Author; Hawwrawr
#Date;5-10-13
#Open Sourced, need Testers anyways
#Python 2.7


import random

#Used to set case values
cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]

#Used to see which case you've selected
checkList = [] 

#Used to see the value of your case
yourCase = []


def main():
	"""
	myCase is literally just for the looks, the number you choose doesn't determine anything at all besides which case you've selected because the value of your case is randomly selected, and is the probability of it being the same twice is 1/26
	"""
	myCase = raw_input("Choose a case (1,26): ")

	#Checks to see if the value you've input is within the index range of the the length of cases
	if int(myCase) > 26 or int(myCase) < 1:
		print "Index Out Of Range"
		main()
		
	else:
		
		#Used to randomly select a value from the list of Values that was listed above
		Case = random.choice(cases)
		
		#Removes that Value so it cannot be re-used in future casses
		cases.remove(Case)
		
		#Adds your case to the list to keep track of your case Value
		yourCase.append(Case)
		
		#Adds the number of the case you selected to the list
		checkList.append(myCase)
		
		#Directs you to the new function	
		Remove(myCase,checkList)

#This function's purpose is to remove cases		
def	Remove(myCase,checkList):
	
	#Determines how much turns you have left until moving on to the Banker() funtion
	turn = 3
	
	#A while loop to get all 3 Removals done
	while turn != 0:
		
		#Again just to see which case you've selected or not
		caseRemove = raw_input("Choose a case to be removed (1,26): ")
		
		#Checks to see if the input is within index range
		if int(caseRemove) > 26 or int(caseRemove) < 1:
			print "Index out of range"
		
		#Checks to see if the number you've input is already been used
		if caseRemove in checkList:
			print "Case already taken."
			
		else:
			#This chunk right here is basically the same as the above, 
			Case = random.choice(cases)
			cases.remove(Case)
			checkList.append(caseRemove)
			#Used to escape the while loop and signal the completion of the removals for this round
			turn = turn - 1
			
	#Checks to see if there is one case left
	if len(cases) == 1:
		Banker(myCase,checkList)
	Banker(myCase,checkList)

#The Banker() function is to offer you the average amount of what is still inside the cases.
def Banker(myCase,checkList):
	#Used to find the Average of your cases
	bankOffer = sum(cases)/float(len(cases))	
	
	#Again checks to see if you have 1 case left over
	if len(cases) == 1:
		
		#Asks you to see if you want your case or not
		finalChoice = raw_input("Would you like to keep your case (Y)es or (N)o: ")
		if finalChoice == "y" or finalChoice == "Y":
			
			#This Little peice is to make it when the number is displayed, it won't have bracets around it
			yourCase2 = sum(yourCase)
			print "You won","$",yourCase2
			main()
			
		elif finalChoice == "N" or finalChoice == "n":
			print "You won","$","%.2f"%bankOffer
			main()
			
		#If you input something besides n or y then it keeps asking the question until you get it right
		else:
			print "Invalid Input"
			Banker(myCase,checkList)
			
	#this portion is for when the cases are greater than 1
	if len(cases) > 1:	
			
		#Everything Down here is pretty much self explainable
		print "The Banker Offered","$","%.2f"%bankOffer, "Do You Accept (Y)es or (N)o" 
		offerDecision = raw_input(">")
		
		if offerDecision == "Y" or offerDecision == "y":
			print "You\'ve won","$","%.2f"%bankOffer
			#Same as above
			yourCase2 = sum(yourCase)
			
			print "Your case contained","$",yourCase2
		elif offerDecision == "N" or offerDecision == "n":
			Remove(myCase,checkList)
				
		else:
			print "Invalid Input"
			Banker(myCase,checkList)
main()
