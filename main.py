import requests
#set your URL
url = "http://127.0.0.1:8000/exercises/exercises/"

'''
set your headers .. 
note >> dont set content type 
'''
headers = {'Accept': 'application/json; indent=4',
           'Authorization': f'Token 307ca96205030d44f6fbde58f72590ffb34ae312'}

'''
set your data here 
note >> just your data without any files
'''

data =  {
        "exercise_name": "bench press",
         "category":"Chest",
         "visibility":"private" ,
         }

'''
set your files here with same syntax

note >> 'exercise_pic' & 'exercise_vid' this is keys  of my request 
'''
files= [
  ('exercise_pic',('1.jpg',open('1.jpg','rb' ).read(),'image/jpeg')) ,
  ('exercise_vid',('Smith_Machine_Squat_-_Thighs_Exercise-2.mp4',open('Smith_Machine_Squat_-_Thighs_Exercise-2.mp4','rb' ).read(),'image/jpeg'))
]

reply = requests.post(url, data=data, files=files, headers=headers).json()
print(reply)