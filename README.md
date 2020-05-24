# covid-19-api

A simple API of covid-19 stats for Japan.

## Getting started

Install required packages using pipenv.
If pipenv is not installed on your environment, install pipenv at first.

```
$ pipenv install --dev
$ pipenv shell
```

Run server.

```
$ cd api
$ python manage.py runserver
```

Then, server will be started on 8000 port.

## Initial setup

Set up environment args.

```
$ cd api
$ cp .env.tmpl .env
$ vim .env
```

Setup database.

```
$ python manage.py migrate
```

Load initial prefectures info.

```
$ python manage.py loaddata stats/fixtures/prefectures.json
```

## Load statitics

This API loads data from Yahoo stats.

Run script.

```
$ pipenv run  python manage.py runscript stats_loader
```
