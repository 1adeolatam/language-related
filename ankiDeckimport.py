#!/usr/bin/env python

import googletrans

langCodes = """Afrikaans 	af
Albanian 	sq
Amharic 	am
Arabic 	ar
Armenian 	hy
Azeerbaijani 	az
Basque 	eu
Belarusian 	be
Bengali 	bn
Bosnian 	bs
Bulgarian 	bg
Catalan 	ca
Cebuano 	ceb 
Chinese (Simplified) 	zh-CN 
Chinese (Traditional) 	zh-TW 
Corsican 	co
Croatian 	hr
Czech 	cs
Danish 	da
Dutch 	nl
English 	en
Esperanto 	eo
Estonian 	et
Finnish 	fi
French 	fr
Frisian 	fy
Galician 	gl
Georgian 	ka
German 	de
Greek 	el
Gujarati 	gu
Haitian Creole 	ht
Hausa 	ha
Hawaiian 	haw 
Hebrew 	he**
Hindi 	hi
Hmong 	hmn 
Hungarian 	hu
Icelandic 	is
Igbo 	ig
Indonesian 	id
Irish 	ga
Italian 	it
Japanese 	ja
Javanese 	jw
Kannada 	kn
Kazakh 	kk
Khmer 	km
Korean 	ko
Kurdish 	ku
Kyrgyz 	ky
Lao 	lo
Latin 	la
Latvian 	lv
Lithuanian 	lt
Luxembourgish 	lb
Macedonian 	mk
Malagasy 	mg
Malay 	ms
Malayalam 	ml
Maltese 	mt
Maori 	mi
Marathi 	mr
Mongolian 	mn
Myanmar (Burmese) 	my
Nepali 	ne
Norwegian 	no
Nyanja (Chichewa) 	ny
Pashto 	ps
Persian 	fa
Polish 	pl
Portuguese (Portugal, Brazil) 	pt
Punjabi 	pa
Romanian 	ro
Russian 	ru
Samoan 	sm
Scots Gaelic 	gd
Serbian 	sr
Sesotho 	st
Shona 	sn
Sindhi 	sd
Sinhala (Sinhalese) 	si
Slovak 	sk
Slovenian 	sl
Somali 	so
Spanish 	es
Sundanese 	su
Swahili 	sw
Swedish 	sv
Tagalog (Filipino) 	tl
Tajik 	tg
Tamil 	ta
Telugu 	te
Thai 	th
Turkish 	tr
Ukrainian 	uk
Urdu 	ur
Uzbek 	uz
Vietnamese 	vi
Welsh 	cy
Xhosa 	xh
Yiddish 	yi
Yoruba 	yo
Zulu 	zu"""

def main(args):
	if len(sys.argv) != 5:
		print("Improper number of arguments")
		print("Usage: python3 ankiDeckimport.py [input] [output] [targetLang] [single char delimeter]")
		print("Languages and respective codes are \n" + langCodes)

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
