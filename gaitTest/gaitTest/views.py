#render allows for quick use of templates
from django.shortcuts import render
#firbase python library
import pyrebase

#make sure firebase authentication is enabled in firebase dashboard
#firebase config goes here
config={
    'apiKey': "API-KEY",
    'authDomain': "AUTH-DOMAIN",
    'databaseURL': "DATABASE-URL",
    'projectId': "PROJECT-ID",
    'storageBucket': "STORAGE-BUCKET",
    'messagingSenderId': "MSI",
    'appId': "API-ID",



}
#firebase initialization
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


#views are defined below

#defines signin view
def signin(request):
    return render(request,'login.html')

#defines homeview
def home(request):
	return render(request,"Home.html")


#this redirects into the homeview if user exits and credentials are correct
def postsignin(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        #check for error with login
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid email or password"
        return render(request,'login.html',{"message":message})
    
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,'Home.html',{"email":email})

#logout button on homeview defined here
#redirects to loginview
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,'login.html')

#defines loginview
def signup(request):
    return render(request,'registration.html')

#redirects to login upon successful registration
def postsignup(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        #create user with given information
        print("before user created")
        user=authe.create_user_with_email_and_password(email,passs)
        print("User created")
        uid = user['localId']
        print("UID created")
        idToken = request.session['uid']
        print("Token created")
        print(uid)
    except:
        print('Error creating user')
        return render(request,'registration.html')
    return render(request,'login.html')


