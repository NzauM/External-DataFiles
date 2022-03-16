## Guests App

#### An application to demonstrate the different types of external data files and their manipulation in Python

## Description
#### This is a project that imports data from different types of external data files(XML, CSV, JSON, and SQL). The project has 4 external data files, one of each, and a file on how to execute it. The files(executexml.py, executejson.py and executecsv.py) contain details on how to import their data. You can clone, install the requirements and run the file to see and manipulate your data from the terminal.

## SetUp/Installation Requirements
* You need to have Python and Postgres installed.
* You need to have an existing Postgres Database User

### To Setup;
* Fork and Clone the repository
* Navigate to the External-DataFiles folder
* Install a virtual environment and activate it by running:
```
python3 -m venv virtual
source virtual/bin/activate
```
* Install all the packages and dependencies by running:
```
pip install -r requirements.txt
```
* Confirm you have all requirements by running:
```
pip freeze > dependencies.txt
```
* All the packages in requirements.txt should reflect in dependencies.txt
* Configure your database settings to match your postgres credentials
* Create a database called guests
* Run system checks and migrations to create the tables 
* Now, import the data from your .sql file by running:
```
psql -h <db-host> -U <db-user> -d <db-name> -f <sql-file>
```
Replace the fields in <> with the real values, the db-host often be 'localhost'
* Now serve the application by running:
```
python3 manage.py runserver
```
* You should see your application on the browser with the data from the .sql file
* To write to a .sql file, run:
```
pg_dump <db_name> <file_name.sql>
```
Remember to replace db_name with your database name and file_name with your desired file name

* To traverse the json file from the terminal, run
```
python3 executejson.py
```
* To traverse the csv file from the terminal, run
```
python3 executecsv.py
```
* To traverse the xml file from the terminal, run
```
python3 executexml.py
```

### Known Bugs
There are no known issues at the moment, If you come across any issue or bug, kindly let me know through [Issues](https://github.com/NzauM/External-DataFiles/issues/new/choose)

## Technologies Used
* Python
* Django
* PSQL Database + Psycopg2

## Licence
MIT License

Copyright (c) [2022] [MercyNzau]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





