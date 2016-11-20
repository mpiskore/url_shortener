# Url Shortener
### An application for shortening URL addresses.

## Usage:
Run the server locally with `./manage.py runserver` and check out the fancy web app.

You can add URL addresses, application will shorten them for you (unless they have been already short, like, for example, `wp.pl` ;) ) and you will be able to access the provided url with its shorten version immediately or share with friends for later use!

You can also check the information on given shorten URL by preceding the url with an exclemation mark (!). Don't worry about the odd username - we fake all the user data!

## Installation:

simply clone the repo locally, prepare a virtualenv or pyenv and:

`pip install -r requirements.txt`

prepare a database for local run purposes (by default it is a PostgeSQL database, but it can be changed in `settings.py`, as well as the user name and DB name):
In `psql` client:
`ALTER ROLE django SET client_encoding TO 'utf8';`
`ALTER ROLE django SET default_transaction_isolation TO 'read committed';`
`ALTER ROLE django SET timezone TO 'UTC';`
`CREATE DATABASE url_shortener`

And run the server in project's root directory:
`./manage.py runserver`

## Testing:

Setup the tools:
`ALTER USER django CREATEDB`
`pip install -r requirements_dev.txt`

And run the tests:
`./manage.py test`

## Future development:

* The front-end is ugly and it was meant to be, I'm no front-end developer, but there is a chance that I'll learn and feel the need to improve this.
* FTP url addresses are not handled at the moment, I don't think that this is a big issue, but for art of development's sake I can take care of it some day.
* No CI, no deploy scripts - result of lack of time more than lack of skill, if the project is going to be improved and, maybe, used by anyone (joke!) this can be also implemented.
