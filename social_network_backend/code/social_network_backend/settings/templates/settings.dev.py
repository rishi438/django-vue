import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = True
SECRET_KEY = env("SECRET_KEY")
