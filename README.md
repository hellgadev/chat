# Chat

## About
This repository hosts the code for a rest api implementation of the simple chat


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and 
testing purposes. 

### Prerequisites

These instructions are valid for Linux. 

You need to install following software:
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installing

Clone git-repositories:
```bash
git clone git@github.com:hellgadev/chat.git
```

Change the work directory to cloned project root dir:

```
cd chat
```
### Run the project
```
python3 manage.py migrate
python3 manage.py runserver localhost:8000
```

### Apply the dump 
Install SQLite cli 
```bash
sudo apt install sqlite3
```
Apply dump
```bash
sqlite3 db.sqlite3 < dump.sql
```

### Project resources
**Local uri**

Chat API http://localhost:8000/api/
Admin http://localhost:8000/admin/

### API Documentation
Postman collection placed [here](postman/Chat.postman_collection.json)

## Built With
* [Django](https://www.djangoproject.com/) – ORM.
* [SQLite](https://www.sqlite.org/) – database. 
* [DRF](https://www.django-rest-framework.org/) - API.
