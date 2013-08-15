# Setup Development Environment
[virtualenv](http://www.virtualenv.org/en/latest/index.html) is required to 
establish a fresh development environment.

    mkdir pyenv
    virtualenv pyenv
    source pyenv/bin/activate


install required tools and libraries

    pip install django
    pip install django-admin-bootstrapped

Then checkout the latest source code, and start the site

    git clone https://github.com/stellatse/alpha.git
    cd alpha
    python manage.py syncdb
    python manage.py loaddata unk/countries.json
    python manage.py runserver