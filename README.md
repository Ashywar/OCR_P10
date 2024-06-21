<h1 align="center">REST API Project - SOFTDESK - OpenClassRooms Project 10</h1>
<br>
<br>
Ce script Python est le 10e projet réalisé dans le cadre d'une formation chez OpenClassrooms.
<br>

## OVERVIEW
Beta version of a RESTful API made with Django REST Framework. SoftDesk is an API for managing to-do lists  (issue tracking system).This solution is aimed at corporate customers, in B2B.<br>
The app will basically allow users to create various projects, add contributors to specific projects, create issues within projects and assign labels to those issues based on their priorities, tags, etc. <br> 
The access is granted to authenticated users via JSON Web Tokens (JWTs).

## REQUIREMENTS
Python 3 <br>
Django 3 <br>
Django REST Framework 3 <br>
<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/Ashywar/OCR_P10
```
Start access the project folder

## for Windows
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
## . . . 
Install the python dependencies to the virtual environment
```
pip install -r requirements.txt
```
Create the database structure by using sqlite3
```
Go to src folder:
`cd src`
And make the migrations:
`python manage.py migrate`

```
Launch the local server:
```
python manage.py runserver`