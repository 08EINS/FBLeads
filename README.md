# Facebook Leads Classification Application

Base project for an individual productive assignment (IPA).

## Project Overview

Candidate: Dominic Monn

Person in charge: Fabio A. Camichel

Experts: Luzi Stamm and Dinesh Rajakaruna


## Technical Overview

* Python 3.6
* Django 1.11
* PostgreSQL
* Docker



## Setup Docker
To communicate from django to postgres, we need to put database configuration in django applications settings file. It should look like this:

    DATABASES = {  
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

Now lets run ```docker-compose build``` in terminal within the project directory. It will build/rebuild (if necessary) all the containers. For first time running the containers, run ```docker-compose up -d```. Lets go to browser and type: localhost:8000. We should see the django application up and running.

For stopping the docker, run ```docker-compose stop```. Re-running docker, use ```docker-compose start```.

### Shell accessing
    # nginx
    docker exec -ti nginx bash

    # web
    docker exec -ti web bash

    # database
    docker exec -ti db bash  

### logs

    # nginx
    docker-compose logs nginx  
    
    # web
    docker-compose logs web  
    
    # database
    docker-compose logs db  
