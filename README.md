# Setup Development Environment
[virtualenv](http://www.virtualenv.org/en/latest/index.html) is required to 
establish a fresh development environment. Python 2.7 is required, since some package cannot run in Python 3

    mkdir pyenv
    virtualenv -p /usr/bin/python2.7 pyenv
    source pyenv/bin/activate


install required tools and libraries

    pip install django
    pip install django-admin-bootstrapped
    pip install django-crispy-forms
    pip install pytz
    pip install django-timezone-field
    pip install django-countries
    pip install django-ajax-forms

If install pytz failed, try 'easy_install pytz' instead

Then checkout the latest source code, and start the site

    git clone https://github.com/stellatse/alpha.git
    cd alpha
    python manage.py syncdb
    python manage.py loaddata unk/countries.json
    python manage.py loaddata unk/initia_data.json
    python manage.py runserver 0.0.0.0:8080
