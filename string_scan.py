#
#
#
# 
#    .d8888b.  d8b 888      888                       .d8888b.                                                                        
#   d88P  Y88b Y8P 888      888                      d88P  Y88b                                                                       
#   888    888     888      888                      Y88b.                                                                            
#   888        888 88888b.  88888b.   .d88b.  888d888 "Y888b.    .d88b.  88888b.  .d8888b   .d88b.      .d8888b .d88b.  88888b.d88b.  
#   888  88888 888 888 "88b 888 "88b d8P  Y8b 888P"      "Y88b. d8P  Y8b 888 "88b 88K      d8P  Y8b    d88P"   d88""88b 888 "888 "88b 
#   888    888 888 888  888 888  888 88888888 888          "888 88888888 888  888 "Y8888b. 88888888    888     888  888 888  888  888 
#   Y88b  d88P 888 888 d88P 888 d88P Y8b.     888    Y88b  d88P Y8b.     888  888      X88 Y8b.    d8b Y88b.   Y88..88P 888  888  888 
#    "Y8888P88 888 88888P"  88888P"   "Y8888  888     "Y8888P"   "Y8888  888  888  88888P'  "Y8888 Y8P  "Y8888P "Y88P"  888  888  888 
#
#
#                                   (BETA)
#
#
#    Plugin Name    :   gibbersense.py
#    Plugin ID      :   gbrsns-01
#    Plugin Purpose :   Gibber Sense Deamon 
#
#    Plugin Author  :   @ajithatti
#
#    Plugin Version :    0.0.1
#    Plugin Status  :   beta
#
#====================================================================================================================================

# Include Section
import subprocess
import os
import os.path
import sys
import getopt
import enchant
import string


from sys import argv, stdout

# Plugin Informaiton

# Env Variable

# Plugin Mode

# Settings

# Report Findings

#------------------------------------------------------------------------------
# Function      : 
#
# Purpose       : 
#
# Parameters    : 
#
# Returns       : None


def fun( ):

    print "Fun"

pass



#------------------------------------------------------------------------------
# Function      : length_scan()
#
# Purpose       : Based on length of string try to find some sense
#
# Parameters    : string
#                 
# Returns       : None


def length_scan(string):

   print ""

pass



#------------------------------------------------------------------------------
# Function      : english_test()
#
# Purpose       : Based on length of string try to find some sense
#
# Parameters    : string
#                 
# Returns       : count of english words identified


def english_test(string):

    dict_en = enchant.Dict("en_US")

    words = string.split()
    wcount = 0

    for word in words :
        if(dict_en.check(word)) :
            wcount +=1
        pass
    pass

    return wcount

pass



#------------------------------------------------------------------------------
# Function      : isprime()
#
# Purpose       : computes and tells if a number is prime or not
#
# Parameters    : n number to be tested
#                 
# Returns       : True or False



def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True
pass


#------------------------------------------------------------------------------
# Function      : ishex()
#
# Purpose       : checks if a string is hexadecimal 
#
# Parameters    : n number to be tested
#                 
# Returns       : True or False



def ishex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)
pass




#------------------------------------------------------------------------------
# Function      : pattern_scan()
#
# Purpose       : Based on the string pattern try to make some sense
#
# Parameters    : string
#                 
# Returns       : None


def pattern_scan(string):


    words = string.split()
    wcount = len(words)

    eng_count = english_test(string)

    print "\n\t\tNumber of Wrods : ",  wcount
    print "\n\t\tEnglish words =", eng_count

    ratio = float("0.0")
    ratio = float(eng_count)/float(wcount)

    if (ratio > float("0.5")):
        print "\n\t\t> The given string is a collection of English words"
        return False 
    else :
        return True

pass


def check_special(string):

    words = string.split('/')
 
    eng_count = 0

    for word in words :
        
        eng_count  += english_test(word)
    pass

    return eng_count

pass

#------------------------------------------------------------------------------
# Function      : hash_scan()
#
# Purpose       : Probaly the string is a hash we will see if we have seen the
#                 string which gives this hash
#
# Parameters    : string
#                 
# Returns       : None


def hash_scan(string):

    l = len(string)
    hashstr = False

    if(l == 32):
        print "\n\t\tMay be the string is",  "MD4 Sum" 
        print "\n\t\tMay be the string is",  "MD5 Sum" 
        print "\n\t\tMay be the string is",  "NTLM Token"
        hashstr = True
         

    elif(l == 40):
        print "\n\t\tMay be the string is",  "SHA1" 
        hashstr = True

    elif(l == 56):
        print "\n\t\tMay be the string is",  "SHA224" 
        hashstr = True

    elif(l == 64):
        print "\n\t\tMay be the string is",  "SHA256" 
        hashstr = True

    elif(l == 96):
        print "\n\t\tMay be the string is",  "SHA384" 
        hashstr = True

    elif(l == 128):
        print "\n\t\tMay be the string is",  "SHA512" 
        hashstr = True

    if(hashstr):
        print "\n\t\tYou can check with https://crackstation.net/ if they have cracked this string"

    return not(hashstr)

pass






#------------------------------------------------------------------------------
# Function      :  string_scan() 
#
# Purpose       :  analyze a given string
#
# Parameters    :  string
#                 
#
# Returns       : None


def string_scan(org_string ):

    gibberish = True

    org_len = len(org_string)
    
    string = org_string.strip()

    new_len = len(string)

    print "\n\t[+] Statistical Analysis :"

    if(org_len != new_len):

        print "\n\t\t>>  Removing leading and trailing spaces\n"

    print "\n\t\tString Length = ", new_len


    print "\n\t[+] Findings :"
    
    if ' ' in string : 

        gibberish = pattern_scan(string)

    elif(string[new_len -1] == "="):
        print "\n\t\tMay be the string is BASE64 Encoded"

    elif(unicode(string, "utf-8").isnumeric()) :
        print "\n\t\tA numeric string"
        if(isprime(int(string)) ) :
            print "\n\t\tWow, its a prime number" 
    elif( '/' in string):
    
        print "\n\t\tEnglish words in the string " ,  check_special(string)
        print "\n\t\tSpecially crafted string"
        gibberish = False
    

    else :
        gibberish = hash_scan(string)


    if(ishex(string)):
        print "\n\t\tThe string is hexa decimal"


    if(gibberish == True):
        print "\n\t\tThe string is Gibberish"


pass




