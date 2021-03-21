from os import environ


SESSION_CONFIGS = [

    dict(
        name='messaging',
        num_demo_participants=140,
        app_sequence=['messaging'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='habs',
        display_name='HABS Research Study',
        participant_label_file='participantList.txt',
        use_secure_urls=True
    )
]

ADMIN_USERNAME = 'habs'
# for security, best to set admin password in an environment variable

#ADMIN_PASSWORD = '123'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'xvtl-0vqu1$u^egm&j!3+ut33d@0d#2qm3hi16n34+*4vm12o^'

INSTALLED_APPS = ['otree']