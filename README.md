# HTU-ICTC6-CP-mysouq.
*HRD-Souq

-Install the requirements (python -m pip install -r requirements.txt).

-On a Windows command prompt, run the following commands:

$ set FLASK_APP="capstone"
$docker-compose up -d
$ set FLASK_ENV="development"
$ flask run

-Three type of users 
1-buyer Default -> role = 0
2-seller -> role = 1
3-Admin -> Password = 1234 , -> role = 2

-To initialize the DataBase using this route -> '/init-db'

**********************************************************
-Database contains :
    models.user :
        1-class User
    
    models.item:
        1-class Item
        2-class Category

    models.request:
        1-class BuyRequest
        2-class UpgradeRequest
**********************************************************
-Blueprints contains :  

    1-home
    2-login
    3-notification
    4-profile
    5-signup
    6-user
**********************************************************
-Forms contains :

    1-edit profile form
    2-items form
    3-login form
    4-sign up form

**********************************************************
-Templates contains :

    
    1-login
    2-sign up
    3-user
    4-item
    5-profile
    6-notification
