### import library firebase
import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7
from firebase import firebase

### Setup Firebase ###
SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)

def makeId(id):
    return ('Alat1/pengguna/' + id)

def get(inetId):
    return SPR.get(inetId, None)

def update(inetId, tipe):
    value = 55
    SPR.put(inetId, tipe, value)
    

#----- Fungsi Update -----
#def dataUpdate():