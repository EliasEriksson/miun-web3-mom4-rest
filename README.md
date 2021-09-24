# miun-web3-mom4-rest

## Running with django development server
The development server is not intended for production use. Instead a proper web server should be used.
This application is hosted at https://miun.eliaseriksson.eu/ with NGINX + uWSGI but apache2 + mod_wsgi is another option.
1. Clone this repository with `git clone https://github.com/EliasEriksson/miun-web3-mom4-rest`.
2. navigate into the repository with `cd miun-web3-mom4-rest`.
3. Create a virtual environment with `python3 -m venv venv` (windows: `python -m venv venv`).
4. Activate the virtual environment with `source venv/bin/activate` (windows (cmd): `venv/Scripts/activate.bat`).
5. Install dependencies with `python -m pip install -r requirements.txt`.
6. Navigate to django root with `cd rest_root`.
7. Generate a django secret key 
`python -c "from django.core.management.utils import get_random_secret_key as gen;print(gen())"`.
8. Add the file `rest_root/rest/credentials.json` with the the following content but with your database credentials 
   and your generated django secret key.
   ```json
   {
       "database": {
           "NAME": "you database name",
           "USER": "you database user",
           "PASSWORD": "your database users password",
           "HOST": "your database host address",
           "PORT": "3306"
       },
       "secret_key": "your django secret key"
   }
   ```
9. From within `rest_root/` create new migrations with `python manage.py makemigrations`.
10. Apply the migrations with `python manage.py migrate`.
11. Run the development server with `python manage.py runserver`