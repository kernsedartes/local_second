DEBUG = True
ALLOWED_HOSTS = ["*"]

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

TINKOFF_API_KEY = "your-api-key"
ENDPOINT_TINKOFF = "your-secret-key"
API_KEY_TINKOFF = "your-api-key"
SECRET_KEY_TINKOFF = "your-secret-key"

OPEN_AI_API_KEY = "your-api-key"

NGROK_URL = "https://db87242fe8b5.ngrok-free.app"

APP_SETTINGS = LocalSettingsClass(
    portal_domain="b24-68oetn.bitrix24.ru",
    app_domain="127.0.0.1:8000",
    app_name="local_second",
    salt="wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF",
    secret_key="wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf",
    application_bitrix_client_id="local.68710e7e833cb2.53743072",
    application_bitrix_client_secret="ddTyR1IXqlp9ECtZEWdK71rc5V76obij6hwwjRhYK2EVuc1F5Y",
    application_index_path="/",
)

DOMAIN = "56218ef983f3-8301993767665431593.ngrok-free.app"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "local_second",
        "USER": "postgres",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    },
}

BITRIX_WEBHOOK_DOMAIN = "b24-68oetn.bitrix24.ru"
BITRIX_WEBHOOK_KEY = "7ye37zvxaxlz5gxw"
BITRIX_BASE_URL = "https://b24-68oetn.bitrix24.ru"
