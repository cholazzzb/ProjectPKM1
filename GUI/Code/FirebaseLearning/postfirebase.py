import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7

import SPRRFID as RFID
from firebase import firebase

### Setup Firebase ###
SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)

RFID.checkId()

print (RFID.checkId.id)

# Make the userPath

'''
userPath = 'Alat1/pengguna/' + id

# Get data to update
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)

# Update data
SPR.put(userPath, 'botol kecil', 4)

# Check if the data has been updated
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)
'''