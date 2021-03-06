Welcome to the juntagrico documentation
=========
Installation
---------

Install juntagrcio from it's git repository. You need an django app.

The following django settings are nescessary to run juntagrico.

Additional to juntagrico the following apps have to installed into django:

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'juntagrico',
        'impersonate',
    ]
    
The following authentication settings are required

.. code-block:: python

    AUTHENTICATION_BACKENDS = (
        'juntagrico.util.auth.AuthenticateWithEmail',
        'django.contrib.auth.backends.ModelBackend'
    )
    
Additionally also some changes in the middleware have to to be added

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )
    
Since we use session we need a serializer

.. code-block:: python

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
    
Django also needs to be configured to send emails and to access a database. If you need more helping points see the testsettings in the project folder



juntagrico specific settings
---------

You can use the following settings to configure juntagrico


* MEMBER_STRING

  The description text for memebers, if you use something special
  
  Type: String

  default value

  .. code-block:: python

    "Mitglied"

* MEMBERS_STRING

  Plural of the above

  Type: String

  default value
    
  .. code-block:: python

    "Mitglieder"

* ASSIGNMENT_STRING

  The description text for job assignemnts, if you use something special

  Type: String

  default value

  .. code-block:: python

    "Mitglied" 

* ASSIGNMENTS_STRING

  Plural of the above

  Type: String

  default value

  .. code-block:: python

    "Arbeitseinsätze"

* ORGANISATION_NAME

  The short name of your orgnisation

  Type: String

  default value

  .. code-block:: python

    "Juntagrico"

* ORGANISATION_LONG_NAME

  The long version of your organisation, if you have one otherwise also use the short one
  
  Type: String

  default value

  .. code-block:: python

    "Juntagrico the best thing in the world"

* ORGANISATION_ADDRESS

  The address of your organisation
  
  Type: dict with the keys
  - name
  - street
  - number
  - zip
  - city
  - extra

  default value

  .. code-block:: python

    {"name":"Juntagrico", 
        "street" : "Fakestreet",
        "number" : "123",
        "zip" : "12456",
        "city" : "Springfield",
        "extra" : ""}

* ORGANISATION_BANK_CONNECTION

  the bank connection informartion of your organisation
  
  Type: dict with the keys
  - PC (postkonto)
  - BIC
  - IBAN
  - NAME
  - ESR (if you enable billing)

  default value

  .. code-block:: python

    {"PC" : "01-123-5",
        "IBAN" : "CH 00 12345 67890 12345 67890 10",
        "BIC" : "BIC12345XX",
        "NAME" : "Juntagrico Bank",
        "ESR" : "01-123-45"}

* INFO_EMAIL

  The general email of your organistation
  
  Type: String

  default value

  .. code-block:: python

    "info@juntagrico.juntagrico"

* SERVER_URL

  The base url of your organisation (not the one where you run juntagrico)

  Type: String  

  default value

  .. code-block:: python

    "www.juntagrico.juntagrico"

* ADMINPORTAL_NAME

  The name you want to use for the portal
  
  Type: String

  default value

  .. code-block:: python

    "my.juntagrico"

* ADMINPORTAL_SERVER_URL

  The base url where you run juntagrico (and where your static lies)
  
  Type: String

  default value

  .. code-block:: python

    "my.juntagrico.juntagrico"

* BUSINESS_REGULATIONS

  Path to your business regulations document
  
  Type: String

  default value

  .. code-block:: python

    "/static/docs/business_regulations.pdf"

* BYLAWS

  Path to your bylaws document
  
  Type: String

  default value

  .. code-block:: python

    "/static/docs/bylaws.pdf"

* STYLE_SHEET

  If you want to use a custom design this specifies the path for your css
  
  Type: String

  default value

  .. code-block:: python

    "/static/css/juntagrico.css"

* FAQ_DOC

  Path to your FAQ document
  
  Type: String

  default value

  .. code-block:: python

    "/static/doc/fac.pdf"

* EXTRA_SUB_INFO

  If you use extra subscritions this describes the path to the document describing them
  
  Type: String

  default value

  .. code-block:: python

    "/static/doc/extra_sub_info.pdf"

* ACTIVITY_AREA_INFO

  Path to your document describing your activity areas
  
  Type: String

  default value

  .. code-block:: python

    "/static/doc/activity_area_info.pdf"

* SHARE_PRICE

  Price of one share
  
  Type: String

  default value
  
  .. code-block:: python

    "250"

* PROMOTED_JOB_TYPES

  Types of jobs which should apear on start page
  
  Type: List of Strings

  default value

  .. code-block:: python

    []

* PROMOTED_JOBS_AMOUNT

  Amount of jobs which should be promoted on the startpage
  
  Type: Integer

  default value

  .. code-block:: python

    2

* DEPOT_LIST_COVER_SHEETS

  The amount of cover sheets for your delivery lists, for each x one
  
  Type: String

  default value

  .. code-block:: python

    'x'

* DEPOT_LIST_OVERVIEWS

  The amount of overview sheets for your delivery lists, for each x one
  
  Type: String

  default value

  .. code-block:: python

    'x'

* DEPOT_LIST_GENERATION_DAYS

  Days on which the deliverylist can be generated
  
  Type: List of Integers representing days of the week

  default value

  .. code-block:: python

    [1,2,3,4,5,6,7]

* BILLING

  Enabling bill generation and management
  
  Type: Boolean

  default value

  .. code-block:: python

    False

* BUSINESS_YEAR_START

  Defining the start of the business year
  
  Type: dict with the keys
  - day
  - month

  default value

  .. code-block:: python

    {"day":1, "month":1}

* BUSINESS_YEAR_CANCELATION_MONTH

  The date until you can cancel your subscriptions
  
  Type: Integer

  default value

  .. code-block:: python

    10

* DEMO_USER

  If you run a demo setup and want to display the login name on the login page
  
  Type: String

  default value

  .. code-block:: python

    ''

* DEMO_PWD

  If you run a demo setup and want to display the password on the login page

  default value

  .. code-block:: python

    ''

* CIRCLES

  Defining the different images for core and job assignments etc

  default value

  .. code-block:: python

    {'circle_full': '/static/img/circle_full.png',
        'circle_alomst_full': '/static/img/circle_alomst_full.png',
        'circle_half': 'static/img/circle_half.png',
        'circle_almost_empty': '/static/img/circle_almost_empty.png',
        'circle_empty': '/static/img/circle_empty.png',
        'circle_full_core': '/static/img/circle_full_core.png',
        'circle_x': '/static/img/circle_x.png',
        'circle_y': '/static/img/circle_y.png'
        }

* GOOGLE_API_KEY

  The google api key to enable the mapps in juntagrico
  
  Type: String

  default value

  .. code-block:: python

    "GOOGLE_API_KEY"

For your convenience all settings with default values to copy into your settings.py and to adapt them

.. code-block:: python

        MEMBER_STRING = "Mitglied"
    MEMBERS_STRING = "Mitglieder"
    ASSIGNMENT_STRING = "Mitglied"
    ASSIGNMENTS_STRING = "Arbeitseinsätze"
    ORGANISATION_NAME = "Juntagrico"
    ORGANISATION_LONG_NAME = "Juntagrico the best thing in the world"
    ORGANISATION_ADDRESS = {"name":"Juntagrico", 
                "street" : "Fakestreet",
                "number" : "123",
                "zip" : "12456",
                "city" : "Springfield",
                "extra" : ""}
    ORGANISATION_BANK_CONNECTION = {"PC" : "01-123-5",
                "IBAN" : "CH 00 12345 67890 12345 67890 10",
                "BIC" : "BIC12345XX",
                "NAME" : "Juntagrico Bank",
                "ESR" : "01-123-45"}
    INFO_EMAIL = "info@juntagrico.juntagrico"
    SERVER_URL = "www.juntagrico.juntagrico"
    ADMINPORTAL_NAME = "my.juntagrico"
    ADMINPORTAL_SERVER_URL = "my.juntagrico.juntagrico"
    BUSINESS_REGULATIONS = "/static/docs/business_regulations.pdf"
    BYLAWS = "/static/docs/bylaws.pdf"
    STYLE_SHEET = "/static/css/juntagrico.css"
    FAQ_DOC = "/static/doc/fac.pdf"
    EXTRA_SUB_INFO = "/static/doc/extra_sub_info.pdf"
    ACTIVITY_AREA_INFO = "/static/doc/activity_area_info.pdf"
    SHARE_PRICE = "250"
    PROMOTED_JOB_TYPES = []
    PROMOTED_JOBS_AMOUNT = 2
    DEPOT_LIST_COVER_SHEETS = 'x'
    DEPOT_LIST_OVERVIEWS = 'x'
    DEPOT_LIST_GENERATION_DAYS = [1,2,3,4,5,6,7]	
    BILLING = False
    BUSINESS_YEAR_START = {"day":1, "month":1}
    BUSINESS_YEAR_CANCELATION_MONTH = 10
    DEMO_USER = ''
    DEMO_PWD = ''
    CIRCLES = {'circle_full': '/static/img/circle_full.png',
            'circle_alomst_full': '/static/img/circle_alomst_full.png',
            'circle_half': 'static/img/circle_half.png',
            'circle_almost_empty': '/static/img/circle_almost_empty.png',
            'circle_empty': '/static/img/circle_empty.png',
            'circle_full_core': '/static/img/circle_full_core.png',
            'circle_x': '/static/img/circle_x.png',
            'circle_y': '/static/img/circle_y.png'
        }
    GOOGLE_API_KEY = "GOOGLE_API_KEY"