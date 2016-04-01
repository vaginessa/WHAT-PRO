#! /usr/bin/env python

# WiFi Auditing Tool Survey
# Exploit Tools

from Tkinter import *
import subprocess

window = Tk()
window.title ( 'WHAT Geolocation v1.0' )
WINDOW_SIZE = "10x10"
img = PhotoImage( file = '/root/WHAT-PRO/Wifi_Logo.gif' )
small_img = PhotoImage.subsample( img , x = 4 , y = 4 )
label = Label( window , image = small_img , bg = 'red')
label.grid(row=0,column=0) 

btn_end = Button( window , text = 'Close' , command=exit )
btn_end.grid(row=10,column=0)

def runShellScript6():
	import subprocess
	subprocess.call(['/root/WHAT-PRO/./GISKISMET-BSSID-LAUNCH.sh'])

btn_scn = Button( window , text = 'GISKISMET (BSSID)' , command=runShellScript6 , width = 15 )
btn_scn.grid(row=2,column=0 ) 

def runShellScript7():
	import subprocess
	subprocess.call(['/root/WHAT-PRO/./GISKISMET-LAUNCH.sh'])

btn_pcp = Button( window , text = 'GISKISMET (Track)' , command=runShellScript7 , width = 15 )
btn_pcp.grid(row=1,column=0)

#def runShellScript8():
#	import subprocess
#	subprocess.call(['/root/WHAT-PRO/./WPS-ATK-LAUNCH.sh'])

#btn_pcp = Button( window , text = 'WPS' , command=runShellScript8 , width = 15 )
#btn_pcp.grid(row=1,column=2)

#def runShellScript9():
#	import subprocess
#	subprocess.call(['/root/WHAT/./WPS-PIX-LAUNCH.sh'])

#btn_ovp = Button( window , text = 'WPS-PIXIE' , command=runShellScript9 , width = 15 )
#btn_ovp.grid(row=1,column=3)

#def runShellScript10():
#	import subprocess
#	subprocess.call(['/root/WHAT-PRO/./MITM-LAUNCH.sh'])

#btn_dad = Button( window , text = 'MITM-Ettercap' , command=runShellScript10 , width = 15 )
#btn_dad.grid(row=1,column=4)

#def runShellScript11():
#	import subprocess
#	subprocess.call(['/root/WHAT-PRO/./AIRCRACK-LAUNCH.sh'])

#btn_dac = Button( window , text = 'AIRCRACK' , command=runShellScript11 , width = 15 )
#btn_dac.grid(row=1,column=5)

#def runShellScript12():
#	import subprocess
#	subprocess.call(['/root/WHAT-PRO/./METASPLOIT-LAUNCH.sh'])

#btn_db = Button( window , text = 'Metasploit' , command=runShellScript12 , width = 15 )
#btn_db.grid(row=1,column=6)

#def runShellScript7():
#	import subprocess
#	subprocess.call(['/root/WHAT/./WIPE-CREATE-LAUNCH.sh'])

#btn_dad = Button( window , text = 'Renew Storage' , command=runShellScript7 , width = 15 )
#btn_dad.grid(row=4,column=5)

#def runShellScript8():
#	import subprocess
#	subprocess.call(['/root/WHAT/./WIFI-BOOST.sh'])

#btn_dad = Button( window , text = 'Card Power Boost' , command=runShellScript8 , width = 15 )
#btn_dad.grid(row=2,column=3)

def runShellScript9():
	import subprocess
	subprocess.call(['/root/WHAT-PRO/./ISNIFF-LAUNCH.sh'])

btn_isn = Button( window , text = 'Start iSniff' , command=runShellScript9 , width = 15 )
btn_isn.grid(row=3,column=0)

def runShellScript10():
	import subprocess
	subprocess.call(['/root/WHAT-PRO/./LOCNOGPS-LAUNCH.sh'])

btn_loc = Button( window , text = 'Start loc-nogps' , command=runShellScript10 , width = 15 )
btn_loc.grid(row=4,column=0)

window.mainloop()

