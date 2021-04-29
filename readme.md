# Expressnews
**Expressnews is a new aggregation web application which scraps fresh news from news sources and display to authenticated users and users can save the news in their feeds**
- Backend:-Django
- Frontend:-Vuejs
- UI-framework:-Vueitfy
- Authentication:- JWT
- Database:-postgresql
- Scraping:- Celery,Rabbitmq

 ## Description:-
  Expressnews is a progressive web application. The user interface of application is developed in Vuejs with Vuetify framework and backend is developed in Django a Python framework . The application has a worker thread which is developed using **Celery** a python library which is runs using **RabbitMQ server** . **Celery** scraps the news briefing from the news sources and display them to the users . The users can save the news post in their feeds.

**Video link for web app:-**[![Expressnews](https://i9.ytimg.com/vi_webp/Fzwz9xvECOA/mqdefault.webp?time=1619656200000&sqp=CIj8p4QG&rs=AOn4CLBNoVg2xVJCpMlDuT3sPWKB3FJn2Q)](https://youtu.be/Fzwz9xvECOA "Project Demo")
## Features :-

- User authentication system implementation using Json web tokens
- Implementation of news saving feature for users in their feeds using ManytoMany fields from news table to users table
- Implementation of text classification WRNN algorithm using tensorflow and keras in the backend
- News api to display the scraped news
- Celery workers to scrap the news from the source urls using the rabbitmq server as the broker service and save in database







## Requirements:-
- Rabbitmq server which is developed in Erlang
- Postgresql database system

## Project Setup:-
> **Clone this project on to your system**

**Setting up backend:-**
 -
**Project has requrements.txt file so install all the requirements:-**
`py -m pip install -r requirements.txt`
>open the expressnews folder which is a backend folder 

**Add this additional files in newsAPI app directory:-**
>[news_text_classification.h5](https://drive.google.com/file/d/1B8FQMW2zXtMHukGr0t_JyjdJaEkXB0-E/view)
>[encoder](https://drive.google.com/file/d/1-BM0RC-uekunmd0BNP367jqdQ6aTM2Dd/view)
>[tokenizer.pickle](https://drive.google.com/file/d/1FcukFsb9fMFbuByJzz4MO7MuSge5Kz1w/view)

**Migrate the databases to the database system**
`python manage.py makemigrations`
`python manage.py migrate`

**Setup and start the rabbitmq server to run the celery**
**To run the scraping process**
`celery -A expressnews worker -l info`

**Run the backend server using command**
`python manage.py runserver`
>This will start development server on http://127.0.0.1:8000/ it will have all required APIs

*Setup the superuser of the django application so as to access admin of website*

## Setting up Frontend
>open expressui folder which is the frontend of application

**Install all the node dependencies**
`npm install`

**Run the frontend server**
`npm run serve`
>This will start development server on http://localhost:8081/ . This will be the userinterface of application

## Colab file DL implementaion
[link](https://colab.research.google.com/drive/1HUWJuFNBZzTebgVplXx4snJEn0cmaUku?usp=sharing)


## Flow chart

![flowchart](https://drive.google.com/uc?export=view&id=1EjRj3JpbW0U7VYAjGhUty9wHEn3NDGy2)

## Entity relationship diagram

![flowchart](https://drive.google.com/uc?export=view&id=1L9yDYi_vGsnb8zQ6TqavnVcvrDcVSmv0)