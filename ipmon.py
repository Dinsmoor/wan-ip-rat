#!/usr/bin/env python2
import time, os, smtplib
from requests import get

class IpMon():

    def __init__(self):
        open('oldip.txt', 'a').close() # make sure the record file exists
        while 1: # loop forever for constant monitoring
            if self.doipthing(): pass # if no change then who cares
            else: self.sendemail() # let me know if it changes
            time.sleep(1200) # don't hog resources, check every 20 min

    def doipthing(self):
        log = open('oldip.txt','r+') # ip record file
        oldip = log.read()
        self.ip = get('https://api.ipify.org').text # works as of 2017
        if oldip != self.ip: # write the new IP to the record file
            log.write(self.ip)
            log.close() # commit changes to disk from buffer
            return False
        else: return True

    def sendemail(self):
        server = smtplib.SMTP('mail.cock.li',587)
        server.ehlo() # herro
        server.starttls() # mail.cock.li uses starttls on 587
        server.login('email@cock.li','mypassword') # yay cleartext passwords
        server.sendmail("email@cock.li","email@airmail.cc","\nNEW IP NOTIFICATION: "+self.ip)

if __name__ == "__main__": mon = IpMon()
