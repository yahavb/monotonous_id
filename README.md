# monotonous_id
generating monotonous id 

### Deploy Aurora Serverless PG
https://aws.amazon.com/rds/aurora/serverless/

### Deploy django app

`sudo -H pip3 install django`

`pip3 install django psycopg2 django-postgres-extra django-sslserver`

`django-admin startproject django_app`

`cd django_app`

`django-admin startapp mono`

Configure the DB in `django_app/settings.py`. In the DATABASES section

Add the logistics and psqlextra to `INSTALLED_APPS` in `django_app/settings.py`

`./manage.py pgmakemigrations`

`./manage.py migrate`

### Configure secure ALB access

#### eks cluster prep

Create ECR

```bash
./create-ecr-repos.sh
```
Build the logisitics application docker image

```bash
./build
```

Execute step 1, 2, and 3 in https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html

Provision a certificate with ACM and reference it in `k8s-ingres.yaml`


Deploy to eks:

```bash
kubectl apply -f k8s-app.yaml
kubectl apply -f k8s-svc.yaml
kubectl apply -f k8s-ingres.yaml
```
