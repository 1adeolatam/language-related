#!/usr/bin/env python

import googletrans


langs = googletrans.LANGUAGES

def displayLangs():
    print ("Language   Language code")
    for lang in sorted(langs):
        print (langs[lang] + " " + lang)
        

def main(args):
	if len(sys.argv) != 5:
		print("Improper number of arguments")
		print("Usage: python3 ankiDeckimport.py [input] [output] [targetLang] [single char delimeter]")
		displayLangs()

		return 1
	inpFName = sys.argv[1]
	outFName = sys.argv[2]

	targetLang = sys.argv[3]
	delimeter = sys.argv[4]

	inp = open(inpFName)
	words = [word.strip() for line in inp.readlines() for word in line.split(',') if word.strip()]
	print(words)


	targetList = []
	tran = googletrans.Translator()
	c = 0
	count = len(words)
	for i in words:
		print(str(c) + " / " + str(count) + " Translate")
		targetList.append(tran.translate(i,dest=targetLang).text)
		c+=1
	out = open(outFName,"w")
	for i in range(len(targetList)):
		print(i)
		out.write(targetList[i] + delimeter+ words[i] + '\n')

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
