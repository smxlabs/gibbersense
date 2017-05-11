# gibbersense

Found a Gibberish string or file in the wild and dont know what is it? Throw it to GibberSense, it might try to make some sense out of it. 


Being an extensible framework, we are adding more to the capabilities of GibberSense.


Extract Sense out of Gibberish stuff

#LAMMA   (BETA)


###Vulnerability Assessment Framework for all the Crypto Implimentations.


(An Open Source Initiative by - SECURITY MONX )




Gibber Sense Documentation  (beta)

        File Name   :   README

        Author      :   @ajithatti

        Org         :   Security Monx

        Version     :   0.0.1

        Purpose		: 	Gives introduction of Gibber Sense




Table Of Contents   :

        A.      Licenses Information
        B.      Introduction to Gibber Sense
        C.      Dependencies
        D.      Using Gibber Sense
        E.      Features
        F.      Note
        G.      Contributors




A. Licenses Information

    LAMMA Framework (beta) and its documents are covered with NO Licenses.
    You are free to use it in any way you want. No conditions what so ever.

    For details about the project visit our website
        "http://www.securitymonx.com/Project-LAMMA"




B. Introduction to Gibber Sense

    Gibber Sense is a python based tool and extension to LAMMA also known as BCAF (Basic Crypt Analysis Framework) module.
    The best use case Gibber Sense is to verify the robustness of encryption libraries if they are free from any backdoor or flaws. But it can also be used to guess type of encryption , hashing schemes, type of encrypted session cookies. If you trying to develop your own secrete encryption scheme, Try and see what GibberSense has to say about it.
    
    Gibber Sense takes 2 types of inputs Strings and Files. Once you feed any gibberish input, it tries to make sense out of it using statistical and basic crypt analysis  
    
    Gibber Sense can identify 100 different string formats and can give you directions for further investigations. 
    For Files, Gibber Sense offers -
      * Content type analysis, 
      * Strings extraction, 
      * Frequency Analysis, 
      * Decryption of substitution ciphers, 
      * Attempts decryption with all popular encryption schemes using null keys,
      * Entropy visualization  
      * XORring
      * and pattern analysis. 


C. Dependencies  :   Gibber Sense uses following python modules  :

                    1.  magic  - Identifies the File Type

                         pip install python-magic

                    2.  PIL - Python Imaging Library 

                        pip install pil



D. Using Gibber Sense :

1.  Gibber Sense is a command line tool 

$ python gibbersense.py 

   .d8888b.    d8b   888        888                                 .d8888b.                                              
  d88P  Y88b   Y8P   888        888                                d88P  Y88b                                             
  888    888         888        888                                Y88b.                                                  
  888          888   88888b.    88888b.     .d88b.    888d888      "Y888b.      .d88b.    88888b.    .d8888b     .d88b.  
  888  88888   888   888 "88b   888 "88b   d8P  Y8b   888P"           "Y88b.   d8P  Y8b   888 "88b   88K        d8P  Y8b 
  888    888   888   888  888   888  888   88888888   888               "888   88888888   888  888  "Y8888b.   88888888 
  Y88b  d88P   888   888 d88P   888 d88P   Y8b.       888          Y88b  d88P  Y8b.       888  888        X88   Y8b.     
  "Y8888P88    888   88888P"    88888P"     "Y8888    888          "Y8888P"     "Y8888    888  888    88888P"   "Y8888  
       


    gibbersense.py [-h] [-s] [-f] [-o] 

    Purpose  : Gibber Sense accepts any gibberish string or file and
                 tries to extract sense out of it


        -h [--help]      : prints this usage help
        -s [--string]    : provide a string parameter to Gibber Sense
        -f [--file]      : proivde a file path parameter to Gibber Sense
        -o [--out]       : save the result of analysis to this file
 


2. Analyze a String 

            $ python gibbersense.py -s "eb5b3ed9d88a9a43d95a4a97958190c0"

              [+] Processing String  eb5b3ed9d88a9a43d95a4a97958190c0 


              [+] Statistical Analysis :

                String Length =  32

              [+] Findings :

                May be the string is MD4 Sum

                May be the string is MD5 Sum

                May be the string is NTLM Token

                You can check with https://crackstation.net/ if they have cracked this string

                The string is hexa decimal


              [+] Analysis complete...



3. Analyze a file
            python gibbersense.py -f test.pdf

              [+] Processing File : test.pdf 


              [+] Gibber Sense Statistical Analysis  

                  %  of printable ASCII Chars     : 38
                  %  of printable LOW  Chars      : 12
                  %  of printable HIGH Chars      : 49
                  number of printable NULL Chars  : 2026
                  File size in number of Chars    : 526477

              [+] Findings : 


                The file type is found to be  BINARY

                File Type : PDF document, version 1.4

              [+] Suggestions 
              
                The visualization of file < test.pdf > is stored in < test.pdf.png >

              [+] Analysis complete...




         $ python gibbersense.py -f rot.txt .pdf

               [+] Processing File : rot.txt 


                  The visualization of file < rot.txt > is stored in < rot.txt.png >
                [+] Gibber Sense Statistical Analysis  

                    %  of printable ASCII Chars     : 99
                    %  of printable LOW  Chars      : 0
                    %  of printable HIGH Chars      : 0
                    number of printable NULL Chars  : 0
                    File size in number of Chars    : 3568

                [+] Findings : 


                  The file type is found to be  TEXT

                  File Type : UTF-8 Unicode text, with very long lines

                [+] Suggestions 

                  Looks like an Encoded file. Try decoding or substitution cipher

                  Consider Frequency analysis of the Text file

                  The visualization of file < rot.txt > is stored in < rot.txt.png >

                [+] Analysis complete...




E.     Features    :

The Gibber Sense tool is aimed at assist in basic crypt-analysis :

        1.  BASIC      :   
                        Gibber Sense attempts to check if a file conents are text or binary.
                        Looks for English contents in the Text file.
                        based on the contents it suggests next course of action.

        2.  Statistical Analysis  :    
                        Gibber Sense provides stastical analysis of text contents. 
                        be able to extend the functionalities easily by adding custom
                        plugins.

        3.  Visualization :   
                        Gibber Sense generated pixel map for the contents of a file to 
                        visually detect the randomness/patterns.

        4.  Basic Cryptanalysis :   
                        Gibber Sense has scripts to perform rotation ciphers, XOR crypt and 
                        decryption with aes-128-xxx-mode with NULL passwords.


F.    Note    :

    We are putting more analysis behind Gibber Sense. Help us to make it better by reaching us at 
    
            a j i t [ a t ] s e c u r i t y m o n x [ d o t ] c o m




G.Contributors

    1.  Ajit Hatti - @ajithatti <twitter handle>

