#!/usr/bin/env python

# Convert from Arabic numerals to Cardinal Russian Word form in Normative Case
#
# Other cases will be implemented in the future
# 
# in the style of https://github.com/scottdchris/NumToWords/blob/master/NumToWords.py

#Teens: remove last char, then append надцать except for 11,12,13

units = ['','один','два','три','четыре','пять','шесть','семь','восемь','девять']
teens = ['десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
tens  = ['','','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто ']
hundreds = ['','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']
Num = 0

setArray = [False,False,False,False,False,False,False,False]


def digitsToArr(num):
	digArray = [0,0,0,0,0,0,0,0,0]
	digArray[0] = num//100000000%10 	#Hundred Millions
	digArray[1] = num//10000000%10 		#Ten Millions
	digArray[2] = num//1000000%10 		#Millions 
	digArray[3] = num//100000%10 		#Hundred-thousands
	digArray[4] = num//10000%10 		#Ten thousands
	digArray[5] = num//1000%10 			#Thousands
	digArray[6] = num//100%10 			#Hundreds
	digArray[7] = num//10%10 			#Tens
	digArray[8] = num%10 				#Units
	return digArray

def hasZeroTrail(digArr):
	if (digArr[6]!=0 and not(digArr[3]!=0 or digArr[4]!=0 or digArr[5]!=0)):
		return digArr[7]==0 and digArr[8]==0
	elif (digArr[3]!=0 or digArr[4]!=0 or digArr[5]!=0):
		return digArr[6]==0 and digArr[7]==0 and digArr[8]==0
	elif (digArr[0]!=0 or digArr[1]!=0 or digArr[2]!=0):
		return digArr[3]==0 and digArr[4]==0 and digArr[5]==0 and digArr[6]==0 and digArr[7]==0 and digArr[8]==0

def digToWord(no):
	num = int(no)
	digArray = digitsToArr(int(num))
	wrd = ''
	if (num == 0):
		wrd = u'ноль'
	elif ( num >= 1 and num < 10):
		wrd = units[num]
	elif (num >= 10 and num < 20):
		wrd = teens[num%10]
	elif(num >= 20 and num < 100):
		wrd += tens[int(num/10)]
		if(digArray[8] != 0):
			wrd += ' ' + units[num%10]
	elif(num >= 100 and num < 1000):
		wrd += hundreds[int(num/100)]
		if(not hasZeroTrail(digArray)):
			wrd += ' ' + digToWord(digArray[7]*10 + digArray[8])
	elif(num >= 1000 and num < 1000000):#NOT WORKING
		wrd += digToWord(digArray[3]*100+digArray[4]*10+digArray[5]) + ' тысяч '
		#print( digArray)
		if(digArray[4] != 1): # Not teads
			if(digArray[5] == 1):
				wrd = wrd[:-1] + 'a '
				l = wrd.split()
				#print(len(l)-1)
				#print(l[len(l)-2])
				l[len(l)-2] = l[len(l)-2][0:2]+'нa '
				wrd = ' '.join(l)
				#print(wrd)
			elif(digArray[5] < 5 ):
				wrd = wrd[:-1] + 'и '
		#print(not hasZeroTrail(digArray))
		if(not hasZeroTrail(digArray)):
			wrd += ' ' + digToWord(digArray[6]*100+digArray[7]*10+digArray[8])
	
	wrd = ' '.join(wrd.split())
	return wrd
	#casesOfword(wrd)

#gtFiveTwentyThirty()
# returns true if the tens and units part are >= 5 and
# <= 30. 
#i.e x|{05,...,30}
#e.g 125, 15, 529, 21 => true
#
def gtFiveTwentyThirty():
	return(((digArray[7] == 0) and (digArray[8] >= 5))
	or (( digArray[7] == 1 ) and (digArray[8] <= 9))
	or  digArray[7] <=3 )

#
#
#
def fortyNinetyHun():
	return(digArray[7] == 4 or digArray[7] == 9 or digArray[6] == 1)

#This series of functions returns true if it is not the teens case for 1 through 4
#
def one():
	return digArray[8] == 1 and digArray[7] != 1
def two():
	return digArray[8] == 2 and digArray[7] != 1
def three():
	return digArray[8] == 3 and digArray[7] != 1
def four():
	return digArray[8] == 4 and digArray[7] != 1
# TODO
# Make functions for each case that transform into the correct 
# They can use the global digit array instead of just using the nominative version of the word
#
# ! FIX LOGIC FOR CASES 
#

def genitive(nominative):
	splited = nominative.split()
	numword = len(splited)
	
	if one():
		splited[numword-1] = 'одного'
		setArray[7] = True
	elif two():
		splited[numword-1] = 'двух'
		setArray[7] = True
	elif three():
		splited[numword-1] = 'трёх'
		setArray[7] = True
	elif four():
		splited[numword-1] = 'четырёх'
		
	if fortyNinetyHun():
		if digArray[7] == 4:
			splited[numword-2] = 'сорока'
		if digArray[7] == 9:
			splited[numword-2] = 'девяноста'
		if digArray[6] == 1:
			if(numword == 1):
				splited[0] = 'ста'			
			if(numword == 2):
				splited[numword-2] = 'ста'
			if(numword >= 3):
				splited[numword-3] = 'ста'	
				
	if gtFiveTwentyThirty() and not fortyNinetyHun():
		splited[numword-1] = splited[numword-1][:-1] +'и'
		if(numword > 1 and digArray[7] < 4):
			splited[numword-2] = splited[numword-2][:-1] +'и'
	return ' '.join(splited)		

def dative(nominative):
	splited = nominative.split()
	numword = len(splited)
	if fortyNinetyHun():
		return genitive(nominative)
	if gtFiveTwentyThirty():
		return genitive(nominative)	

def prepositional(nominative):
	splited = nominative.split()
	numword = len(splited)
	if fortyNinetyHun():
		return genitive(nominative)
	if gtFiveTwentyThirty():
		return genitive(nominative)


def accusative(nominative):
	splited = nominative.split()
	numword = len(splited)
	if fortyNinetyHun():
		return nominative
	if gtFiveTwentyThirty():
		return nominative

def instrumental(nominative):
	splited = nominative.split()
	numword = len(splited)
	if fortyNinetyHun():
		return genitive(nominative)
	if gtFiveTwentyThirty():
		splited[numword-1] = splited[numword-1] +'ю'
		if(numword > 1 and digArray[7] < 4):
			splited[numword-2] = splited[numword-2] +'ю'
	return ' '.join(splited)

def casesOfword(word):
	print("Nominative/Именительный   : " + word)
	#print("Genitive/Родительный      : " + genitive(word))
	##print("Dative/Дательный          : " + dative(word))
	#print("Accusative/Винительный    : " + accusative(word))
	#print("Instrumental/Творительный : " + instrumental(word))
	#print("Prepositional/Предложный  : " + prepositional(word))

def main(args):
	#print(u'ноль')
	#digToWord(sys.argv[1])
	if len(sys.argv) != 2:
		print("Improper number of arguments")
		print("Usage: python3 numbertorussword.py [number]")
		return 1
	Num = int(sys.argv[1])
	casesOfword(digToWord(Num))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
