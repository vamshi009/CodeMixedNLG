import operator
final = []
inmy = []
finalsent = [] #list of sentences with words only
finalpos = [] #list of sentences with pos sequences only
sent = [] #each sentence 
pos = [] #each pos sequence
f = open("input.txt")
hello = list(f)
for i in hello:
#	print i,
	le = i.split()
#	print le
#	print len(le)
	if len(le) != 0:
		inmy.append(le)
		sent.append(le[0])
		pos.append(le[2])
	else:
		final.append(inmy)
		finalsent.append(sent)
		finalpos.append(pos)
#		print "***adding new sentence******* and its len is+++"
#		print len(final) 
		inmy = []
		sent = []
		pos = []
		

#print "printing sentences&&&&&&&"
#print final
#print "word sentences ***********"
#print finalsent
#print "sequence tags*********"
#print finalpos
#oneworddict_________________
oneworddict = {}
for eachsent in finalsent: #unigram count
	for eachword in eachsent:
		if eachword in oneworddict:
			oneworddict[eachword] = oneworddict[eachword] + 1
		else:
			oneworddict[eachword] = 1
#print "^^^^^^^^^^^^^^^^"
#print oneworddict

#oneworddict_________________

#onseqdict*******************
oneseqdict = {}
for eachposseq in finalpos: #unigram count
	for singlepos in eachposseq:
		if singlepos in oneseqdict:
			oneseqdict[singlepos] = oneseqdict[singlepos] + 1
		else:
			oneseqdict[singlepos] = 1
#print "^^^^^^^^^^^^^^^^ one seq dict !!!!!!!!!!!!!!!!!!11"
#print oneseqdict
#oneseqdict*******************


#twoworddict___________________________________
twoworddict = {}

#print "final sent after unigram count$$$$$$$$"
#print finalsent
for eachsent in finalsent:
	
#print ":::::::::"
#print eachsent
	for i in range(0,len(eachsent)):
		if (i+1) > (len(eachsent)-1):
			break;
#print "the word selected is %%%%%%%"
#		print eachsent[i:i+2]
#		print "from the sent"
#		print eachsent
		y = tuple(eachsent[i:i+2])
		if y in twoworddict:
			twoworddict[y] = twoworddict[y] + 1
		else:
			twoworddict[y] = 1
#print "@@@@@@@@@@@@@@@@@ two word dict"
#print twoworddict
#twoworddict______________________________________


#twoseqdict**********************************************************************
twoseqdict = {}

#print "final pos after unigram count$$$$$$$$"
#print finalpos
for eachposseq in finalpos:
	
#print ":::::::::"
#	print eachposseq
	for i in range(0,len(eachposseq)):
		if (i+1) > (len(eachposseq)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachposseq[i:i+2]
#		print "from the sent"
#		print eachposseq
		y = tuple(eachposseq[i:i+2])
		if y in twoseqdict:
			twoseqdict[y] = twoseqdict[y] + 1
		else:
			twoseqdict[y] = 1
#print "@@@@@@@@@@@@@@@@@ two seq dict"
#print twoseqdict
#twoseqdict**************************************************************************


#threeworddict____________________________________
threeworddict = {}
for eachsent in finalsent:
	
#	print ":::::::::"
#	print eachsent
	for i in range(0,len(eachsent)):
		if (i+2)>(len(eachsent)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachsent[i:i+3]
#		print "from the sent"
#		print eachsent
		y = tuple(eachsent[i:i+3])
		if y in threeworddict:
			threeworddict[y] = threeworddict[y] + 1
		else:
			threeworddict[y] = 1
#print "@@@@@@@@@@@@@@@@@ three word dict"
#print threeworddict

#threeworddict______________________________________

#threeseqsict**************************************************************************
threeseqdict = {}
for eachposseq in finalpos:
	
#	print ":::::::::"
#	print eachposseq
	for i in range(0,len(eachposseq)):
		if (i+2)>(len(eachposseq)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachposseq[i:i+3]
#		print "from the sent"
#		print eachposseq
		y = tuple(eachposseq[i:i+3])
		if y in threeseqdict:
			threeseqdict[y] = threeseqdict[y] + 1
		else:
			threeseqdict[y] = 1
#print "@@@@@@@@@@@@@@@@@ three seq dict________"
#print threeseqdict

#threeseqdict**************************************************************************


#fourworddict________________________________________________________
fourworddict = {}
for eachsent in finalsent:
	
#	print ":::::::::"
#	print eachsent
	for i in range(0,len(eachsent)):
		if (i+3)>(len(eachsent)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachsent[i:i+4]
#		print "from the sent"
#		print eachsent
		y = tuple(eachsent[i:i+4])
		if y in fourworddict:
			fourworddict[y] = fourworddict[y] + 1
		else:
			fourworddict[y] = 1
#print "@@@@@@@@@@@@@@@@@ four word dict"
#print fourworddict

#fiveworddict__________________________________________________________

#fiveseqdict****************************************************************************

fourseqdict = {}
for eachposseq in finalpos:
	
#	print ":::::::::"
#	print eachposseq
	for i in range(0,len(eachposseq)):
		if (i+3)>(len(eachposseq)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachposseq[i:i+4]
#		print "from the sent"
#		print eachposseq
		y = tuple(eachposseq[i:i+4])
		if y in fourseqdict:
			fourseqdict[y] = fourseqdict[y] + 1
		else:
			fourseqdict[y] = 1
#print "@@@@@@@@@@@@@@@@@ four seq dict"
#print fourseqdict




#fiveeqdict*****************************************************************************



#fiveworddict_____________________________________________________
fiveworddict = {}
for eachsent in finalsent:
	
#	print ":::::::::"
#	print eachsent
	for i in range(0,len(eachsent)):
		if (i+4)>(len(eachsent)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachsent[i:i+5]
#		print "from the sent"
#		print eachsent
		y = tuple(eachsent[i:i+5])
		if y in fiveworddict:
			fiveworddict[y] = fiveworddict[y] + 1
		else:
			fiveworddict[y] = 1
#print "@@@@@@@@@@@@@@@@@ five word dict"
#print fiveworddict

#fiveworddict______________________________________________________


#fiveseqdict***************************************************************************************

fiveseqdict = {}
for eachposseq in finalpos:
	
#	print ":::::::::"
#	print eachposseq
	for i in range(0,len(eachposseq)):
		if (i+4)>(len(eachposseq)-1):
			break;
#		print "the word selected is %%%%%%%"
#		print eachposseq[i:i+5]
#		print "from the sent"
#		print eachposseq
		y = tuple(eachposseq[i:i+5])
		if y in fiveseqdict:
			fiveseqdict[y] = fiveseqdict[y] + 1
		else:
			fiveseqdict[y] = 1
#print "@@@@@@@@@@@@@@@@@ five seqdict&&&&&&&&&"
#print fiveseqdict



#fiveseqdict****************************************************************************************
for vamsi in range(1,1000):
#	print "in for loop for i as iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
#	print vamsi
	sorted_oneworddict = sorted(oneworddict.items(), key = operator.itemgetter(1))  #generating sentences using probablities
	sorted_oneworddict.reverse()
#	print sorted_oneworddict
#	print sorted_oneworddict[0]
	check = sorted_oneworddict[0]
	ser = list(check)
	print "This is the unigram taken"
	print ser[0]
	oneworddict[ser[0]]=oneworddict[ser[0]]*0.9

	twowordhelp = {}                            #generating two words of sequences^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	for key in twoworddict:
		le = key
		mu = list(le)
#		print "printin the key"
#		print mu
#		print "printin mu[0]"
#		print mu[0]
#		print "printin sorted_oneworddict"
#		print ser[0]
		if mu[0] == ser[0]:
#			print "=-- found one_____"
#			print mu
			if key in twowordhelp:
				print "I'm already there"
			else:
				twowordhelp[key]=twoworddict[key]

	
#	print "search completed list is"
#	print twowordhelp
	sorted_twowordhelp = sorted(twowordhelp.items(), key = operator.itemgetter(1))
	sorted_twowordhelp.reverse()
	le2 = len(sorted_twowordhelp)
                                      #checking if such word exists
	if le2>0:
#		print sorted_twowordhelp
#		print "and it is"
#		print sorted_twowordhelp[0]
		ny = list(sorted_twowordhelp[0])
		ny2 = ny[0]
		ny3=list(ny2)
		print "this is the wanted bigram--"
		print ny3
		ny3t = tuple(ny3)
		twoworddict[ny3t] = twoworddict[ny3t]*0.9
	else:
		print "bigramhelp not found!! :p"

	threewordhelp = {}                 #generating three words of sequences^^^^^^^^^^^^^^^^^^^^^^^^^6
	for key in threeworddict:
		we = list(key)
#		print we
#		print "the following words are we[0] and ny3[0] we[1]  ny3[1]"
#		print we[0], ny3[0], we[1], ny3[1]
		if we[0]==ny3[0] and we[1]==ny3[1]:
#			print "we have found the third word------"
#			print we
			if key in threewordhelp:
				print "already there re---"
			else:
				threewordhelp[key] = threeworddict[key]

#	print "this is threewordhelp"			
#	print threewordhelp

	sorted_threewordhelp = sorted(threewordhelp.items(), key = operator.itemgetter(1))
	sorted_threewordhelp.reverse()
#	print sorted_threewordhelp
	le3 = len(sorted_threewordhelp)
                                      #checking if such word exists
	if le3 > 0:
#		print "and it is"
#		print sorted_threewordhelp[0]
		gy = list(sorted_threewordhelp[0])
		gy2 = gy[0]
		gy3 = list(gy2)
		print "this is the wanteid trigram"
		print gy3
		gy3t = tuple(gy3)
		threeworddict[gy3t] = threeworddict[gy3t]*0.9
	else:
		print "threewordhelp not found! :p"

	fourwordhelp = {}                          #generating four words of sequences^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	for key in fourworddict:
		qe = list(key)
#		print qe
#		print "the following are qe[0] gy3[0] qe[1] gy3[1] qe[2] gy3[2]"
#		print qe[0], gy3[0], qe[1], gy3[1], qe[2], gy3[1]
		if qe[0]==gy3[0] and qe[1]==gy3[1] and qe[2]==gy3[2]:
#			print "WE HAVE FOUND THE FOURTH WORD-----"
#			print qe
			if key in fourwordhelp:
				print "already foutrth word there re----"
			else:
				fourwordhelp[key] = fourworddict[key]
#	print "this is fourwordhelp"
#	print fourwordhelp

	sorted_fourwordhelp = sorted(fourwordhelp.items(), key = operator.itemgetter(1))
	sorted_fourwordhelp.reverse()
#	print sorted_fourwordhelp
	le4 = len(sorted_fourwordhelp)
                                             #checking if such word exists
	if le4 > 0:
#		print "and it is"
#		print sorted_fourwordhelp[0]
		fy = list(sorted_fourwordhelp[0])
		fy2 = fy[0]
		fy3 = list(fy2)
		print "this is the wanted fourgram"
		print fy3
		fy3t = tuple(fy3)
		fourworddict[fy3t] = fourworddict[fy3t]*0.9
	else:
		print "fourwordhelp not found!!!! :P"

	fivewordhelp = {}     #generating five word sequencs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	for key in fiveworddict:
		ae = list(key)
#		print ae
#		print "the following are ae[0] fy3[0] ae[1] fy3[1] ae[2] fy3[2] ae[3] fy3[3]"
		if ae[0] == fy3[0] and ae[1]==fy3[1] and ae[2]==fy3[2] and ae[3]==fy3[3]:
#			print "WE HAVE FOUND THE FIFTH WORD...."
#			print ae
			if key in fivewordhelp:
				print "already fifth word therre----"
			else:
				fivewordhelp[key] = fiveworddict[key]
#	print "this is five word help"
#	print fivewordhelp

	sorted_fivewordhelp = sorted(fivewordhelp.items(), key = operator.itemgetter(1))
	sorted_fivewordhelp.reverse()
#	print "len of sortedfivewordhelp checking its"
	length = len(sorted_fivewordhelp)
#	print length
                                 #checking if such word exists
	if length > 0:                 
#		print sorted_fivewordhelp
#		print "and it is "
#		print sorted_fivewordhelp[0]
		sy = list(sorted_fivewordhelp[0])
		sy2 = sy[0]
		sy3 = list(sy2)
		print "*******************this is the wanted fivegram********************"
		print sy3
		print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
		sy3t = tuple(sy3)
		fiveworddict[sy3t] = fiveworddict[sy3t]*0.9
	else:
		print "fiveword bigram not found :p"
#	
#	print "*****************************************************************************************************************************************"
