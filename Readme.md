# Portfolio:
Portfolio api. Django 3.1, Django RestFramework and Python 3

## Installation:
Clone and run `pip3 install -r requirements.txt` from project directory

## Run form console:
From project directory run `python3 manage.py makemigrations`, `python3 manage.py migrate`

## Provide environment vriables:
Rename file `env.sample` to `.env` and provide DB credentials there

## Run Api from Http:
From project directory run `python3 manage.py runserver` and go to `http://127.0.0.1:8000/`

## Create superuser for Admin:
From project directory run: `python3 manage.py createsuperuser` and go to: `http://127.0.0.1:8000/admn`

## Enter sample data:
Log in to `http://127.0.0.1:8000/admn` and create some categories, items (blog) and info pages (articles)

## Obtain JWT Token:
Post to `http://127.0.0.1:8000/api/token/` user and password as raw data `{"username": "youruser", "password": "yourpassword"`
from Postman or use below paylod:


	curl --location --request POST 'http://127.0.0.1:8000/api/token/' \
	--header 'Content-Type: application/json' \
	--data-raw '{
    	"username": "apiuser",
    	"password": "admin"
	}'

## Call API:
Call Api urls like `http://127.0.0.1:8000` passign JWT Token (Postman Authoriztion -> Bearer Token) or use paste Postman code from below:

	curl --location --request GET 'http://127.0.0.1:8000' \
	--header 'Authorization: Bearer your.token.obtain_from_/api/token/' \
	--data-raw ''

## Api Urls:
Welcome page: `http://127.0.0.1:8000`

Portfolio items: `http://127.0.0.1:8000/items?category=DBCategory&page=1`

Categories: `http://127.0.0.1:8000/categories`

Articles by title: `http://127.0.0.1:8000/article?title=DBarticleTitle` 