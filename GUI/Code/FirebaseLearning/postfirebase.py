from firebase import firebase

### Setup Firebase ###
SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)

# Make the userPath
id = 264811178633
userPath = 'Alat1/pengguna/' + id

# Get data to update
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)

# Update data
SPR.put(userPath, 'botol kecil', 4)

# Check if the data has been updated
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)
