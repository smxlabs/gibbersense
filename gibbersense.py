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
from sys import argv, stdout
import string_scan as sscan
import file_scan   as fscan

# Plugin Informaiton

# Env Variable

# Plugin Mode

# Settings

# Report Findings

#------------------------------------------------------------------------------
#Function      : log
#
# Purpose       : logs given string in to the designated sink
#
# Parameters    : 1. message - message string to be logged
#                 2. The destination of the log
#
# Returns       : None


def log(message, sink):
    sink.write(message)
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

    print"" 
    print"   .d8888b.    d8b   888        888                                 .d8888b.                                              "
    print"  d88P  Y88b   Y8P   888        888                                d88P  Y88b                                             "
    print"  888    888         888        888                                Y88b.                                                  "         
    print'  888          888   88888b.    88888b.     .d88b.    888d888      "Y888b.      .d88b.    88888b.    .d8888b     .d88b.  '
    print'  888  88888   888   888 "88b   888 "88b   d8P  Y8b   888P"           "Y88b.   d8P  Y8b   888 "88b   88K        d8P  Y8b '
    print'  888    888   888   888  888   888  888   88888888   888               "888   88888888   888  888  "Y8888b.   88888888 '
    print"  Y88b  d88P   888   888 d88P   888 d88P   Y8b.       888          Y88b  d88P  Y8b.       888  888        X88   Y8b.     "
    print'  "Y8888P88    888   88888P"    88888P"     "Y8888    888          "Y8888P"     "Y8888    888  888    88888P"   "Y8888  '
    print"       "                                                  

    print "\n\n    %s [-h] [-s] [-f] [-o] " %script
    print "\n    Purpose  : Gibber Sense accepts any gibberish string or file and" 
    print "                 tries to extract sense out of it"
    print "\n"
    print "        -h [--help]      : prints this usage help"
    print "        -s [--string]    : provide a string parameter to Gibber Sense"
    print "        -f [--file]      : proivde a file path parameter to Gibber Sense"
    print "        -o [--out]       : save the result of analysis to this file"
    print " \n\n\n"

    sys.exit(2)


pass  # USAGE BLOCK


# --------------------------------------------------------------------------------
# Function      : 
#
# Purpose       : 
#
# Parameters    : 
#
# Returns       : None


def list_all_remote_scripts(path):
    indir = os.getcwd()

    prefix = ""

    if(indir.endswith("LAMMA")):
        prefix = "modules/remote-module/"

    if(indir.endswith("modules")):
        prefix = "remote-module/"

    indir = indir + "/" + prefix + path

    for root, dirs, filenames in sorted(os.walk(indir)):
        pos = indir.__len__()
        check_dir = root[pos:]
        if ( check_dir.find(".git") != -1):
            continue

        print "./" + root[pos:] + "/"

        for f in filenames:
            if f.endswith(".py"):
                if (f == "__init__.py"):
                    continue
                print "\t  ", f

    exit(0)


pass




# --------------------------------------------------------------------------------
# Function      : get_path_prefix
#
# Purpose       : based on from where the script is invoked, it returns the cwd
#
# Parameters    : None
#
# Returns       : relative cwd


def get_path_prefix() :
    indir = os.getcwd()

    prefix = ""

    if (indir.endswith("LAMMA")):
        prefix = "modules/trust-module/"

    if (indir.endswith("modules")):
        prefix = "trust-module/"

    indir = indir + "/" + prefix

    return prefix
pass




# -------------------------------------------------------------------------------
# Function  : main
#
# Purpose   : The Gibber Sense script.
#
# Params    : 1. argv     (list)    - list of command line arguments
#
# Returns   : None


def main(argv):

    # **** Lets process the arguments *********

    # Initialize the variables

    this_script = argv[0]
    string = ""
    in_file = ""
    out_file = ""
    sink = stdout

    # ---- Show the usage for too few arguments

    if len(argv) < 3:
        usage(this_script)
        sys.exit(2)
    pass  # if block

    # --- try block

    try:
        opts, args = getopt.getopt(argv[1:], "h:s:f:o:",
                                   ["help=", "string=", "file=","out="])


    except getopt.GetoptError:
        usage(this_script)
        sys.exit(2)
    pass  # TRY BLOCK

    # ---- Process the arguments passed to the script

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(this_script)

        elif opt in ("-s", "--string"):
            string = arg

        elif opt in ("-f", "--file"):
            in_file = arg

        elif opt in ("-o", "--out"):
            out_file = arg


        pass  # IF BLOCK
    pass  # FOR BLOCK

    # ---- collect the values and check


    # --- Check if string is to be analyzed : flag [-s]

    if (string != ""):
    
        # process string
        print "\n  [+] Processing String ", string, "\n"

        sscan.string_scan(string)

    pass  # if Block


    # -- Check if file has to be analyzed : flag [-f]

    if (in_file != ""):
        # process string
        print "\n  [+] Processing File :", in_file, "\n"
        
        fscan.file_scan(in_file)

    pass  # if Block

    # -- Set the out file --

    if (out_file != ""):
        sink = open(out_file, "a+")
        print "     Reports will be stored in file => %s" %out_file
        cmd_string = cmd_string + " -o " + out_file
    pass

    print "\n\n\t[+] Analysis complete...\n\n"


pass  # main




# -------------------------------------------------------------------------------
#
# Kick off the script

if __name__ == "__main__":
    main(sys.argv[0:])

pass  # IF BLOCK
