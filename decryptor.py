# -*- coding: utf-8 -*-

#==============================================================================#
# Name:                  $[ActiveDoc-Name]
# Purpose:
#------------------------------------------------------------------------------
# Author:      CyberDev
# Created:     Mon Apr  1 18:48:15 2019
# Copyright:   (c) CyberDev Mon Apr  1 18:48:15 2019
# Licence:     Personal                                                  
#==============================================================================#

#-------------------------------------------------#
#         Importation des modules externes        #
#-------------------------------------------------#
#import


#-------------------------------------------------#
#            Définition des fonctions             #
#-------------------------------------------------#
def encrypt(phrases):
	global result
	lettres = list(phrases)
	for i in range(0,len(lettres)):
		if (lettres[i] == 'a'):
			result.append(1)
		elif (lettres[i] == 'b'):
			result.append(2)
		elif (lettres[i] == 'c'):
			result.append(3)
		elif (lettres[i] == 'd'):
			result.append(4)
		elif (lettres[i] == 'e'):
			result.append(5)
		elif (lettres[i] == 'f'):
			result.append(6)
		elif (lettres[i] == 'g'):
			result.append(7)
		elif (lettres[i] == 'h'):
			result.append(8)
		elif (lettres[i] == 'i'):
			result.append(9)
		elif (lettres[i] == 'j'):
			result.append(10)
		elif (lettres[i] == 'k'):
			result.append(11)
		elif (lettres[i] == 'l'):
			result.append(12)
		elif (lettres[i] == 'm'):
			result.append(13)
		elif (lettres[i] == 'n'):
			result.append(14)
		elif (lettres[i] == 'o'):
			result.append(15)
		elif (lettres[i] == 'p'):
			result.append(16)
		elif (lettres[i] == 'q'):
			result.append(17)
		elif (lettres[i] == 'r'):
			result.append(18)
		elif (lettres[i] == 's'):
			result.append(19)
		elif (lettres[i] == 't'):
			result.append(20)
		elif (lettres[i] == 'u'):
			result.append(21)
		elif (lettres[i] == 'v'):
			result.append(22)
		elif (lettres[i] == 'w'):
			result.append(23)
		elif (lettres[i] == 'x'):
			result.append(24)
		elif (lettres[i] == 'y'):
			result.append(25)
		elif (lettres[i] == 'z'):
			result.append(26)
		elif (lettres[i] == ' '):
			result.append(27)
		elif (lettres[i] == '_'):
			result.append(28)
		else:
			print("Erreur ")
	print(result)


def decrypt(liste):
	global phrase
	for i in range(0,len(liste)):
		if (liste[i] == 1):
			phrase += "a"
		elif (liste[i] == 2):
			phrase += "b"
		elif (liste[i] == 3):
			phrase += "c"
		elif (liste[i] == 4):
			phrase += "d"
		elif (liste[i] == 5):
			phrase += "e"
		elif (liste[i] == 6):
			phrase += "f"
		elif (liste[i] == 7):
			phrase += "g"
		elif (liste[i] == 8):
			phrase += "h"
		elif (liste[i] == 9):
			phrase += "i"
		elif (liste[i] == 10):
			phrase += "j"
		elif (liste[i] == 11):
			phrase += "k"
		elif (liste[i] == 12):
			phrase += "l"
		elif (liste[i] == 13):
			phrase += "m"
		elif (liste[i] == 14):
			phrase += "n"
		elif (liste[i] == 15):
			phrase += "o"
		elif (liste[i] == 16):
			phrase += "p"
		elif (liste[i] == 17):
			phrase += "q"
		elif (liste[i] == 18):
			phrase += "r"
		elif (liste[i] == 19):
			phrase += "s"
		elif (liste[i] == 20):
			phrase += "t"
		elif (liste[i] == 21):
			phrase += "u"
		elif (liste[i] == 22):
			phrase += "v"
		elif (liste[i] == 23):
			phrase += "w"
		elif (liste[i] == 24):
			phrase += "x"
		elif (liste[i] == 25):
			phrase += "y"
		elif (liste[i] == 26):
			phrase += "z"
		elif (liste[i] == 27):
			phrase += " "
		elif (liste[i] == 28):
			phrase += "_"
		else:
			print("erreur")
	print(phrase)


#-------------------------------------------------#
#              Programme principal                #
#-------------------------------------------------#
phrase=""
result=[]
liste_1=[]
decrypt(liste_1)
mots = input("Your sentence : ")
encrypt(mots)



#----------fonction de test du module-------------#
#if __name__ == '__main__':
    #main()


