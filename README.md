# rental-app
Test rental app

To run:
* Clone the repo
* Create venv `python -m venv .venv`
* Activate venv `source .venv/bin/activate`
* Install requirements `pip install -r requirements.txt`
* Run migration `python manage.py migrate`
* Load fixtures `python manage.py loaddata rentals.sample.json` `python manage.py loaddata reservations.sample.json`
* Run server `python manage.py runserver` or run tests `python manage.py test`
