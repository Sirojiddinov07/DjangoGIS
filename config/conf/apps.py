#####################
# My Settings
#####################
INSTALLED_APPS = [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "rosetta",
    "django_redis",
    "rest_framework_simplejwt",
    "crispy_forms",
    "import_export",
    "django_ckeditor_5",
    "polymorphic",
    "drf_spectacular",
    'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',
    'django_rest_passwordreset',

    #####################
    # My apps
    #####################
    "core.apps.home.apps.HomeConfig",
    "core.apps.map.apps.MapConfig",
    "core.apps.custom_user.apps.CustomUserConfig",
    "core.console.ConsoleConfig",
    "core.apps.websocket.apps.WebsocketConfig",
]
