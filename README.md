# Setup

1. `git clone https://github.com/Coupdeg/coup-web.git` and cd
2. install postgresql
3. run `sudo pip install virtualenv`
4. run `virtualenv myprojectenv`
5. run `source myprojectenv/bin/activate`
6. run `pip install django psycopg2`
7. create config database in `/config/local_setting.py`
	```
	from settings import *

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
	      	'NAME': 'coup_development',
	      	'USER': 'myprojectuser',
	      	'PASSWORD': 'password',
	      	'HOST': 'localhost',
	      	'PORT': '5000'
	    }
	}
	```
	1. in console pgsql 
		1. `CREATE DATABASE coup_development;` 
		2. `CREATE USER myprojectuser WITH PASSWORD 'password';`
		3. `GRANT ALL PRIVILEGES ON DATABASE coup_development TO myprojectuser;`
	2. run `python manage.py makemigrations`
	3. run `python manage.py migrate`
8. run `npm install`
9. run `python manage.py collectstatic`

# Tools used in the project
- jquery v.3.2.1
- bootstrap v4.0.0-beta
- dj-database-url==0.4.2
- Django==1.11.4
- gunicorn==19.7.1
- psycopg2==2.7.3
- pytz==2017.2
- whitenoise==3.3.0
- Pillow==4.2.1
