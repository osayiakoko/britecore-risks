# britecore-risks

## Project setup

#### Project setup prerequisite
* create a postgres database on Amazon RDS 
* create an Amazon s3 bucket

#### Steps for setup:

* cd directory to project root folder
* create a '.env' file and create the following variable with corresponding values:
* * SECRET_KEY=Value
* * AWS_ACCESS_KEY_ID=Value
* * AWS_SECRET_ACCESS_KEY=Value
* * AWS_STORAGE_BUCKET_NAME=Value
* * DB_HOST=Value
* * DB_USERNAME=Value
* * DB_PASSWORD=Value
* * DB_NAME=Value
*  Open terminal in project root folder
```bash
# create virtual env
$ python3 -m venv venv

# activate virtual env
$ source venv/bin/activate

# change directory to src folder
$ cd src

# install dependencies
$ pip install -r requirements.txt

# run database migrations
$ python manage.py makemigrations
$ python manage.py migrate

# create superuser
$ python manage.py createsuperuser

# collect static files
$ python manage.py collectstatic

# start server 
$ python manage.py runserver
```


### Deploy to AWS lambda
* create an iam user on Amazon and copy **access key id** and **secret key id**
* Open terminal on your computer

```bash
# navigate to user home folder
$ cd ~

# create .aws directory
$ mkdir .aws

# create credentials file and enter keys as follows:
# aws_access_key_id=Value
# aws_secret_key_id=Value
$ nano credentials 
# ctrl/command s to save 


# install zappa in not already installed
$ pip install zappa

# deploy to aws lambda
$ run zappa deploy dev

# copy returned url
# update django ALLOWED_HOSTS and CORS_ALLOWED_ORIGINS with url

# deploy update:
$ zappa update dev
