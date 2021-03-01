# FoodApi


## Local Setup
```
1. Install python3 from <a href="https://www.python.org/" target="_blank">here</a>
1. pip install -r requirements.txt
1. python manage.py migrate
1. python manage.py createsuperuser(type username and password)
1. python manage.py runserver
```

# API Paths
* [**api/v1/**](#apiv1)
	* [**api/v1/foodapi/**](#apiv1foodapi)



* [**auth/**](#auth)
	* [**auth/login/**](#authlogin)
		* [**auth/login/refresh/**](#authloginrefresh)
	* [**auth/register/**](#authregister)


___	
## api/v1/
### api/v1/foodapi/
**Allowed Methods** : GET
<br>**Access Level** : Authorized
<br>return a json object of all products available on the website - [Link](https://jsonplaceholder.typicode.com/posts)


## auth/
### auth/login/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json - [More information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

#### auth/login/refresh/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'refresh'}
<br>*POST :* the data you post should include 'refresh' and the value of it should be user refresh token that is sent when user login.

### auth/register/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exceptions handled , should have a proper place to show them in frontend.


# Future Work:
- [x] add users and configurations
- [x] add CORS and configurations
- [x] Filter ojects by userid from given api
