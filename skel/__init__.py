"""Our Flask app."""


from os import environ

from flask import Flask


# Create our base Flask app:
app = Flask(__name__)

# Dynamically load the appropriate environment-specific app settings (defaults
# to use development settings):
app.config.from_object(environ.get('FLASK_SETTINGS_MODULE', 'skel.settings.dev.DevConfig'))
