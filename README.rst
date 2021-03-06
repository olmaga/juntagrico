Juntagrico
=====

.. image:: https://travis-ci.org/juntagrio/juntagrico.svg?branch=master
    :target: https://travis-ci.org/juntagrico/juntagrico
   
.. image:: https://img.shields.io/gemnasium/juntagrico/juntagrico.svg
    :target: https://gemnasium.com/github.com/juntagrico/juntagrico

.. image:: https://img.shields.io/codeclimate/github/juntagrico/juntagrico.svg
    :target: https://codeclimate.com/github/juntagrico/juntagrico

**the easy solution for cooperative vegetable growers**

Juntagrico is a simple Django app to conduct Web-based juntagrico. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "juntagrico" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'juntagrico',
    ]

2. Include the juntagrico URLconf in your project urls.py like this::

    url(r'^my/', include('juntagrico.urls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a job (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/my/home to visit juntagrico.
