# FoodApi - [Link](https://ag602.pythonanywhere.com/)


## LOCAL SETUP
```
1. git clone https://github.com/ag602/FoodApi.git
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser(type username and password)
5. python manage.py runserver
```

## LIBRARIES/FRAMEWORKS USED
1. Django - [Django](https://www.djangoproject.com)
2. For access and refresh tokens - [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest)


## RUN INSTRUCTIONS
```
1. Create user from auth/register/
2. Get access token from auth/login/
3. Test the api on api/v1/foodapi/ using the access token
Note - Refresh token expires in 1 day and Access token expires in 5 minutes.

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
**Allowed Methods** : GET, POST
<br>**Access Level** : Authorized
<br>return a json object of all products available on the website - [Link](https://jsonplaceholder.typicode.com/posts)


## auth/
### auth/login/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* The data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json - [More information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

### auth/login/refresh/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'refresh'}
<br>*POST :* The data you post should include 'refresh' and the value of it should be user refresh token that is sent when user login.

### auth/register/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exceptions handled , should have a proper place to show them in frontend.


# Future Work:
- [] add CORS and configurations
- [] Filter ojects by userid from given api
