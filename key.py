import environ
import os
from os.path import join,basename,abspath

env = environ.Env()

env.read_env(".env")

API_KEY = os.environ.get("API_KEY")