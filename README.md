# Setup

1. `git clone https://github.com/Coupdeg/coup-web.git` and cd
2. install postgresql
3. run `sudo pip install virtualenv`
4. run `virtualenv myprojectenv`
5. run `source myprojectenv/bin/activate`
6. run `pip install django psycopg2`
7. config database in `/config/settings.py`
	1.```
		default': {
        		'ENGINE': 'django.db.backends.postgresql_psycopg2',
        		'NAME': 'coup_development',
        		'USER': 'myprojectuser',
        		'PASSWORD': 'password',
        		'HOST': 'localhost',
        		'PORT': '5000'
    		}
	  ```
	2.in console pgsql 
		1. `CREATE DATABASE coup_development;` 
		2. `CREATE USER myprojectuser WITH PASSWORD 'password';`
		3. `GRANT ALL PRIVILEGES ON DATABASE coup_development TO myprojectuser;`
	3. run `python manage.py makemigrations`
	4. run `python manage.py migrate`	
