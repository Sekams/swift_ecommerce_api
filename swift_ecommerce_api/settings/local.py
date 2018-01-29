from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='x@$q7l1@y^qdtkfk-c@2x)6dc_pe=)3!_z3=^xop0$_ufc(ic=')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
