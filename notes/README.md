# Gotchas

- Ports should be 8080

# Setup

## Authentication

- `gcloud auth list` - List logged in accounts
- `gcloud auth login` - Login with new account
- `gcloud config set account [email]` - Change authenticated account

## Project

- `gcloud projects list` - List projects
- `gcloud config set project [project]` - Set project

# Project `root`

All DNS goes here.

# React

## Setup

1. Setup `Dockerfile`
2. Add deploy command to npm: `"deploy": "gcloud builds submit --tag gcr.io/[project]/[dir] && gcloud run deploy frontend --image gcr.io/[project]/[dir] --platform managed --region us-east1"`
3. Create Bucket
4. Point Webppack at bucket

# Django 

## Setup

1. Setup `cloud_sql_proxy` and point at database instance connection name 
`./cloud_sql_proxy -instances="online-outings-273216:us-east1:online-outings"=tcp:5432`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `gsutil mb gs://[YOUR_GCS_BUCKET]` Create Bucket
6. `gsutil defacl set public-read gs://[YOUR_GCS_BUCKET]` Set bucket to public-read
7. `python manage.py collectstatic`
8. `gsutil rsync -R static/ gs://[YOUR_GCS_BUCKET]/static` Upload static files
9. Update `settings.py` to point at static content with URL `http://storage.googleapis.com/[YOUR_GCS_BUCKET]/static/`
10. Set cloud run app to be able to connect to database

## Resources

- https://cloud.google.com/python/django/kubernetes-engine
- https://cloud.google.com/python/django/appengine
- https://github.com/GoogleCloudPlatform/python-docs-samples/issues/870
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy
- https://cloud.google.com/dns/docs/quickstart
