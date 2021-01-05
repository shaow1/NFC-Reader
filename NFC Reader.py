import serial
import urllib
import requests
import subprocess

ser = serial.Serial('/dev/ttyAMA0',  115200, timeout = 0.5)	#Open the serial Port
ser.flushInput()	# Clear the input buffer
link = "http://www.easybook2017.com/nfc" #This is the domain which we connect to our MangoDB with all book informations
f = urllib.urlopen(link)
myfile = f.read()


b = []
while True:
	data = ser.readlines()
	if data:
        #This is our own way manipulating data read from NFC tag
        # you will need to change it based on your reading results
        c = data[0].split()[4].strip('\r\n').strip('n')
        d = data[1].split()[4].strip('\r\n')
        serial = c + d
        print serial
        payload = { 'serial' : serial}
        r = requests.get('http://www.easybook2017.com/nfc',params = payload)
        print r.url
        if myfile == 'undefined':
            print "Success!"
            subprocess.call(['aplay -fdat /home/pi/piano2.wav'], shell = True) #Provide some sound feedback indicates a successful return
        elif myfile == '1':
            print "This book does not exist!"
        elif myfile == '2':
            print "Data transfer error!"
             
