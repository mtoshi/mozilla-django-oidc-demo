mozilla-django-oidc-demo
====================================
* This repository is experimental for mozilla-django-oidc.
* PyPI https://pypi.org/project/mozilla-django-oidc/
* Github https://github.com/mozilla/mozilla-django-oidc
* Readthedocs https://mozilla-django-oidc.readthedocs.io
* Mozilla https://infosec.mozilla.org/guidelines/iam/openid_connect.html

Demo app installation
====================================
* Get repo and runserver.

.. code::

    $ python3.7 -m venv /tmp/mozilla-django-oidc-demo && source /tmp/mozilla-django-oidc-demo/bin/activate
    $ git clone git@github.com:mtoshi/mozilla-django-oidc-demo.git
    $ cd mozilla-django-oidc-demo
    $ pip install setuptools --upgrade && pip install pip --upgrade
    $ pip install -r requirements.txt
    $ cp .env.sample.google .env  # Please check env variables.
    $ python manage.py migrate
    $ python manage.py runserver 127.0.0.1:8000

* Access with your browser.

.. code::

    http://localhost:8000/

* This demo app has several env files

.. code::

    .env.sample.google
    .env.sample.line
    .env.sample.yahoojapan
    .env.sample.hydra

* Please switch accordingly.

.. code::

    # Example

    $ cp .env.sample.line .env

