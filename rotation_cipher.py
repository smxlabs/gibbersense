#
#                                                                                                                                        #
#           .d8888b.    d8b   888        888                                 .d8888b.                                                    #
#          d88P  Y88b   Y8P   888        888                                d88P  Y88b                                                   #
#          888    888         888        888                                Y88b.                                                        #
#          888          888   88888b.    88888b.     .d88b.    888d888       "Y888b.      .d88b.    88888b.    .d8888b     .d88b.        #
#          888  88888   888   888 "88b   888 "88b   d8P  Y8b   888P"            "Y88b.   d8P  Y8b   888 "88b   88K        d8P  Y8b       #
#          888    888   888   888  888   888  888   88888888   888                "888   88888888   888  888   "Y8888b.   88888888       #
#          Y88b  d88P   888   888 d88P   888 d88P   Y8b.       888          Y88b  d88P   Y8b.       888  888        X88   Y8b.           #
#           "Y8888P88   888   88888P"    88888P"     "Y8888    888           "Y8888P"     "Y8888    888  888    88888P'    "Y8888        #
#                                                                                                                                        #
#
#                                   (beta)
#
#
#    Plugin Name    :   freq_analysis.py
#    Plugin ID      :   fqa-01
#    Plugin Purpose :   Provides frequency analysis of a file contents.
#                       Used to analyse subsitution cipher. 
#
#    Plugin Author  :   @ajithatti
#
#    Plugin Version :   0.0.1
#    Plugin Status  :   beta
#
################################################################################



# Include Section
import os.path
import getopt
import os
import re
import sys
from sys import argv, stdout

from PIL import Image
import random


# --------------------------------------------------------------------------------
# Function      : usage
#
# Purpose       : Proivde a mini help on usage of this program
#
# Parameters    : None
#
# Returns       : None

def usage(script):
    print "\n\n  %s [-o] [-i]  " %script
    print "\n    Purpose  : Computes the frequency distribution each alphabet"
    print "                 present in a file. Used for crypt analysis of "
    print "                 common subsitution ciphers of English text"
    print "\n"
    print "        -o [--out]       : stores the frequency distribution table in a givne file"
    print "        -i [--in]        : path of a file to be analyzed"
    print " \n\n\n"

    sys.exit(2)


pass  # USAGE BLOCK


# --------------------------------------------------------------------------------
# Function      : usage
#
# Purpose       : Proivde a mini help on usage of this program
#
# Parameters    : None
#
# Returns       : None


def log( message, sink) :

    sink.write(message)
pass


buf = ""
# --------------------------------------------------------------------------------
# Function      : usage
#
# Purpose       : Proivde a mini help on usage of this program
#
# Parameters    : None
#
# Returns       : None


def file_process(in_file):

    f = open(in_file, "r")
    buf = f.read()
    return buf

pass 


# --------------------------------------------------------------------------------
# Function      : usage
#
# Purpose       : Proivde a mini help on usage of this program
#
# Parameters    : None
#
# Returns       : None


def rotate(in_file, dist, sink):

 
    buf = file_process(in_file)
    rot = ""

    l = len(buf)
    i = 0

    while (i < l) :

        c = ord(buf[i])
        if( c >= 65 and c <=90) : 
            c += int(dist)
            if (c > 90):
                c = c - 90 + 64
        elif( c>= 97 and c <= 122): 
            c += int(dist)
            if (c > 122):
                c = c - 122 + 96
        pass
        i +=1
        rot += chr(c) 
    pass


    log(rot, sink)

pass 


# --------------------------------------------------------------------------------
# Function      :   main
#
# Purpose       :   Rottion Cipher, substitute current alphabet with next 'dth' 
#                   alphabet. Also known as Caesar Cipher 
#
# Parameters    :   in      -   path of a file to be analyzed 
#                   out     -   file in which frequency distribution is to be stored
#
# Returns       :   dist    -   Distance of hights frequency alphabet from 'e'


def main(argv):


    # Initialize the variables
    in_file = ""
    out_file = ""
    this_script = argv[0]
    dist = ""
    sink = stdout


    if len(argv) < 3:
        usage(this_script)
        sys.exit(2)
    pass  # if block

    # --- try block

    try:
        opts, args = getopt.getopt(argv[1:], "o:i:d:",["out=", "in=","dist="])


    except getopt.GetoptError:
        usage(this_script)
        sys.exit(2)
    pass  # TRY BLOCK

    #---- Process the arguments passed to the script

    for opt, arg in opts:

        if opt in ("-i", "--in"):
            in_file = arg 
        elif opt in ("-o", "--out"):
            out_file = arg 
        elif opt in ("-d", "--dist"):
            dist = arg 
 
        pass # IF BLOCK
    pass # FOR BLOCK


    if( out_file != ""):
        sink = open(out_file, "w")
    pass

    if( in_file == ""):
        print "\n File name for frequency analysis is not specified, Exiting \n\n"
        return (-2)
    pass

    if( dist == ""):
        print "\n Rotation Parameter is not specified, Exiting \n\n"
        return (-2)
    pass

    dist = int(dist) %26


    dist = rotate(in_file, dist, sink)

    return dist

    print "\n\n"

pass # main


#-------------------------------------------------------------------------------
#
# Kick off the script

if __name__ == "__main__":

    main (sys.argv[0:])

pass # IF BLOCK
