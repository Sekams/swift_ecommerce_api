# Swift eCommerce API

**The Swift eCommerce API** is a Django REST Framework API for serving data persistence methods to the Swift eCommerce Application.

## Progress Tracking
https://www.pivotaltracker.com/n/projects/2145830

## Live API
WIP

## Getting Started
To be able to use the application locally, one should follow the guidelines highlighted below.

1. Clone/download the application Github repository by running the command below in a git shell
```
git clone https://github.com/Sekams/swift_ecommerce_api.git
```
2. Set up a virtual environment (follow instructions at: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

3. Install the application requirements by running the code below in the virtual environment:
```
pip install -r requirements.txt
```

4. Install Postgres SQL and create a database called _"swift\_ecommerce\_api"_

5. Create the database tables by running the following command within the virtual environment:
```
python manage.py create_db
```

6. After all the requirements are installed on the local virtual environment, run the application by running the following code in the virtual environment:
```
python manage.py runserver
```
7. After successfully running the application, one can explore the features of the Shopping List Application API exploring the : http://127.0.0.1:5000 in any web browser of choice

## Features
* WIP

## EndPoints

| Type | API EndPoint | Public Access | Description |
| --- | --- | --- | --- |
| WIP | N/A | N/A | N/A |


## Testing
The application's tests can be executed by running the code below within the virtual environment:
```
python manage.py test
```