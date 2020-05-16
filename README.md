# covid-19-api

A simple API of covid-19 stats for Japan.

## Getting started

Install required packages using pipenv.
If pipenv is not installed on your environment, install pipenv at first.

```
$ pipenv install --dev
```

Run server.

```
$ cd api
$ pipenv run python manage.py runserver
```

Then, server will be started on 8000 port.

## Load statitics

This API loads data from Yahoo stats.

Run script.

```
$ pipenv run  python manage.py runscript stats_loader
```
