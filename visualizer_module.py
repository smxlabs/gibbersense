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
#    Plugin Name    :   visualizer-module.py
#    Plugin ID      :   vm-01
#    Plugin Purpose :   Provides visual representation of any given file.
#                       this module accepts Text, PDF, Binary files.works
#                       for files containing random numbers as well.
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
import string_scan as sscan
import extract_strings as xstrings

# Global Declearations 

buf = ""
FILE_STATS = {}
FILE_TYPE = {}



FILE_STATS["stat_ascii"] = 0
FILE_STATS["stat_lower"] = 0
FILE_STATS["stat_higher"] = 0
FILE_STATS["stat_null"] = 0
FILE_STATS["total_len"] = 0


FILE_TYPE["type"] = ""    # Type is TEXT or BINARY or ENCRYPTED
FILE_TYPE["content"] = ""
FILE_TYPE["name"] = ""


def print_stats():


    stat_ascii = FILE_STATS["stat_ascii"] 
    stat_lower = FILE_STATS["stat_lower"]
    stat_higher = FILE_STATS["stat_higher"] 
    stat_null = FILE_STATS["stat_null"] 
    total_len = FILE_STATS["total_len"]

    ascii_pc =  int (float(stat_ascii)/float(total_len) *100)
 
    lower_pc =  int(float(stat_lower )/float(total_len) *100)
    higher_pc = int(float(stat_higher )/float(total_len) *100)

    print "\t[+] Gibber Sense Statistical Analysis  \n"
    print "\t\t  %  of printable ASCII Chars     :", ascii_pc     
    print "\t\t  %  of printable LOW  Chars      :", lower_pc 
    print "\t\t  %  of printable HIGH Chars      :", higher_pc 
    print "\t\t  number of printable NULL Chars  :", stat_null
    print "\t\t  File size in number of Chars    :",  total_len



    
    print "\n\t[+] Findings : \n\n"

    if (ascii_pc > 95):
        FILE_TYPE["type"] = "TEXT"
    else :

        word_count = 0
        eng_count = 0
       
 
        for string in xstrings.strings(FILE_TYPE["name"]) :

            #print string

            if('/' in string or ' ' in string) :
                
                eng_count = sscan.check_special(string)

                if(eng_count > 0) :
                    
                    FILE_TYPE["type"] = "BINARY"
                pass
            pass
        pass

        # application specific file
        # binary file

        if(eng_count == 0) :
            FILE_TYPE["type"] = "ENCRYPTED"

    print "\t\tThe file type is found to be " , FILE_TYPE["type"] 

pass 


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
    print "\n    Purpose  : Provides visual representation of a given file"
    print "                 can be used for visualizing Binary files, Random"
    print "                 Random Numbers, text, pdf files etc"
    print "\n"
    print "        -o [--out]       : stores the visualization of RNG in this file"
    print "        -i [--in]        : path of a file to be analyzed"
    print " \n\n\n"

    sys.exit(2)


pass  # USAGE BLOCK



def log( message, sink) :

    sink.write(message)
pass


def file_process(in_file):

    f = open(in_file, "r")
    buf = f.read()
    return buf

pass 



def drawImage(in_file):

    FILE_TYPE["name"] = in_file

    f = open(in_file, "r")
    buf = f.read()

    l = len(buf)
    FILE_STATS["total_len"] = l
    FILE_TYPE["content"] = buf

    h = l/100 + 1
    w = 100

    if (h > 1000) :
        max = int (l**0.5+1)
       # print " max =" , max
        w = max +1
        h = max +1
    pass       
    

    # print "length = " , w
    # print "l/100 = ", h


    testImage = Image.new("RGB", (w, h), (255,255,255))
    pixel = testImage.load()


    i = 0

    for x in range(w):
        for y in range(h):

            if(i < l):
                col = ord(buf[i])
                #print "char", buf[i],"(", ord(buf[i]), ")"
            else :
                col = 255
            i +=1

            if(col >= 32 and col <=126):
                # visible text range
                b = col
                r = 0
                g = 0
                FILE_STATS["stat_ascii"] += 1 

            elif(col < 32 and col > 0 ):
                # Low Range
                b = 0
                r = 0
                g = col
                FILE_STATS["stat_lower"] += 1

            elif(col > 126 and col < 255):
                # High Range 
                b = 0
                r = col
                g = 0
                FILE_STATS["stat_higher"] += 1

            elif(col == 0):
                # Null
                b = 0
                r = 0
                g = 0
                FILE_STATS["stat_null"] += 1

            elif(col == 255):
                # Null
                b = 255
                r = 255
                g = 255

            red =  r  #random.randrange(0,255)
            blue = g #random.randrange(0,255)
            green = b  #random.randrange(0,255)
            pixel[x,y]=(red,blue,green)
    pass

    f.close()


    return testImage

pass 



# --------------------------------------------------------------------------------
# Function      :   main
#
# Purpose       :   converts file contents in to pixels to generate visualization 
#
# Parameters    :   in      -   path of a file to be visually tested (optional)
#                   out     -   *.png file in which the visual image is to be stored
#
# Returns       :   None


def main(argv):


    # Initialize the variables
    in_file = ""
    out_file = ""
    this_script = argv[0]


    if len(argv) < 3:
        usage(this_script)
        sys.exit(2)
    pass  # if block

    # --- try block

    try:
        opts, args = getopt.getopt(argv[1:], "o:i:",["out=", "in="])


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
        pass # IF BLOCK
    pass # FOR BLOCK


    if( out_file == ""):
        print "\n File name to store the image is not specified, Exiting \n\n"
        return (-2)
    pass

    if( in_file == ""):
        print "\n File name to be visually analyzed \n\n"
        return (-2)
    pass





    finalImage = drawImage(in_file)
    finalImage.save(out_file)

    FILE_TYPE["name"] = in_file

    print_stats()
    print "\n\nThe visualization of file <", in_file, "> is stored in <", out_file, ">" 
    print "\n\n"

pass # main


#-------------------------------------------------------------------------------
#
# Kick off the script

if __name__ == "__main__":

    main (sys.argv[0:])

pass # IF BLOCK
