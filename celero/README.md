# Desafio Celero - Back-End

## Installation

- Assure Python3 is installed and run in the terminal the following command: `pip3 install -r requirements.txt`
- If you want to populate the DB, you can download the results and regions CSV files `https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv`
## Running the project

- Run this command to create the initial Database: `python3 manage.py migrate`
- Create a superuser to access the admin area: `python3 manage.py createsuperuser`
- Start the server: `python3 manage.py runserver`
- The application will be accessible at `localhost:8000` and the admin can be accessed at `localhost:8000/admin`

## Uploading CSV files

- Upload results CSV to: `POST api/v1/upload-results-csv/`
- Upload regions CSV to: `POST api/v1/upload-regions-csv/`

## Managing the objects

- The endpoints to manage the objects are the following (all of them accept GET, POST, PUT, PATCH and DELETE methods):
- `api/v1/region/:id` 
- `api/v1/noc/:id` 
- `api/v1/city/:id` 
- `api/v1/sport/:id` 
- `api/v1/event/:id` 
- `api/v1/team/:id` 
- `api/v1/athlete/:id` 
- `api/v1/olympics/:id` 
- `api/v1/result/:id`
