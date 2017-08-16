#Coded By The M4d Sc13nT15t
#Can You Hear Those Voices?
#Look Into My Eyes Can You See The Pain
#The Chaos I Bring, Youll Never Forget My Name
#The Troubles, The Pain, The Panic, The Fear
#We're Not Santa, But We Will Be Around All Year
from termcolor import colored
print colored("""



      Your Doing Something Naughty                {((((((}
                                                 {)))))))))
      Secrets Are What Your After               ((((( _  _))
                                               )))))) e (e((
     So lets Get That Hash Shall We?          ((((((    >)))
                                              _))))))   ()/(
      Come On Put It In                    .-'  (((((.--' )))
                   .-'''''-._          _.-'         :: (((((
                 .`          '-.    .-'     _.-''  :::)))))))
                 :              ':-:    _.-' :'   .:::((((((
                 :               .:   .:: : :     ::::)))))))
                  :.          ..::   .:: : '      ::::((((((
                   :.        (:::  .:::: : :      o ::)))))))
       _.-.         :.        \/  :-'-'-'-'`'-.-'`:: :((((((
  __.-'   _\       _ :.        \ /             ))):.  :))))))
 (    .-' ;;'-.-''' '':.        :             (((((:.  :((((
  ```'-..-.;._  _.-''-.\         :             ))))):.   ))))
  __.-'   _\_.`'        \        :            (((((((:. '(((
(    _.-' ;;                     :                    :. '---.__
 `'''-....;;,,,,,,,,,,,,,,,;,___:                      \:..b===='


""",'red')
print colored("C0d3d By Th3 M3nT4L H05p1T4L C0d3r5",'white')

import sys

import hashlib, sys



m = hashlib.md5()



hash = ""

hash_file = raw_input("What Is The Path To The Hashes You Wish To Crack?  ")
print colored("If You Treat Her Right She Will Give Up Her Secrets",'yellow') 
wordlist = raw_input("What is your wordlist?  (Enter Path To File:  ")


try:
	hashdocument = open(hash_file,"r")

except IOError:# Just To Check For Errors
	print colored ("Inncorect File Vale! Try Again Scriptkiddie!.",'red')

	raw_input()
	sys.exit()

else:
	hash = hashdocument.readline()
	hash = hash.replace("\n","")
	
try:
	wordlistfile = open(wordlist,"r")

except IOError:#Last Check and Buffer Flush
	print colored ("Inncorect File Vale! Try Again Scriptkiddie!",'red')

	raw_input()
	sys.exit()
else:
	pass

for line in wordlistfile:
	m = hashlib.md5()  #Only Running a Flush

	line = line.replace("\n","")

	m.update(line)

	word_hash = m.hexdigest()

	if word_hash==hash:
		print colored ("Hash Has Been Found!!  The Collision Results Are:",'blue', line)

		raw_input()
		sys.exit()

print colored ("The Wordlist You Are Using Isnt Working, Try A Differnt Rainbow or Wordlist!.",'yellow')
raw_input()
sys.exit()
