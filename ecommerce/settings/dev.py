from .base import *
from .local import *
# importing os module  
import os 
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Python program to explain os.environ object  
from django.utils.crypto import get_random_string

ARN_bucket = 'arn:aws:s3:::mybucket-last'
  
# Adding AWS environment variables  
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAIHE5IC2KRZIREABA'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

# Adding STRIPE environment variables

os.environ['STRIPE_PUBLISHABLE_KEY'] = 'pk_test_7tl7qCi6l6VwSfyaqUmbh1lQ'
os.environ['STRIPE_SECRET_KEY'] = 'sk_test_b1nb09QpEo8rT380EK52VXpw'

chars = 'amnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)