# Udrive
Cloud based storage website with django framework

## About
Users are directed to landing page on opening the website.Unregisteres users are redirected to register page ,after registering they are redirected to login page.
After login the users are directed to Home page where the users can see their files and folders in the root directory.The navbar contain 5 tabs :
*  Home
*  Favourites
*  All Users
*  Profile
*  Logout

## Environment Setup

*  Install [Django](https://docs.djangoproject.com/en/3.2/topics/install/)
*  Install all the required pacakges mentioned in the req.txt using the command pip install -r requirements.txt
*  Run the server and Connect the port to localhost:8000

## Tech Stacks Used

*  HTML
*  CSS
*  Django
*  JavaScript

## Key features

* Responsive website
* User can register using any Email ID.
* User can create Folders and upload Files.
* User can search other user using Searchbar.
* User can make their files and folder public to share among users
* User can browse and download all shared files and folders of other users.
* User can download the folders as zip.
* User can add their favourite files and folder to Favourites tab.
* User can delete their files and folder.
* User can rename their files and folder.
* User can change their profile details from username to password.
* Each user have a default profile image.
* Each file have and folder have icons according to their extension

### Landing Page
![Landing Page](https://github.com/DeepSeaCreature0/Udrive/assets/138828627/5cbd7eef-5163-4d4f-90ec-53c17c39dc30)
![mobile Landing Page](https://github.com/DeepSeaCreature0/Udrive/assets/138828627/e6852a98-0b08-49e2-9fc9-ccf7788589e5) ![mobile Landing Page navbar](https://github.com/DeepSeaCreature0/Udrive/assets/138828627/48bea4bf-960a-4eac-af4a-8a3ab8b867eb)


### Register Page
* New Users have to register ,they can use any mail to register but the username must should be unique.
![Register Page]
![mobile Register Page]

### Login Page
* User have to login after registration. The web application is authenticated and user must sign in using his username created in Register Page. 
![Login Page]
![mobile Login Page]

### Home Page
* After login user willl be redirected to Home tab where they can see all the files and folder in the root directory
![Home Page]
![mobile Home Page]

### Favourites Page
* In this tab user will find all its favourite files and folders
![Fav Page]
![mobile Fav Page]

### All Users Page
* In this tab user will find all the registered users.
* User can find their target user  using a searchbar.
![All Users]
![mobile All Users]

### Profile Page
* This tab contain all the information about user and the user can update his/her profile from username to password .
![Profile Page]
![mobile Profile Page]




