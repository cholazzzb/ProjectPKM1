from firebase import firebase

SPR = firebase.FirebaseApllication('https://smartplastic-65d5e.firebaseio.com/', None)

while True:
    temperature = int(input("What is the temperature? "))

    data_to_upload = {
        'Temp' : temperature,
        'Name' : "Nic"
    }


    result = SPR.post('/MyTestData/', data_to_upload)

    print (result)
