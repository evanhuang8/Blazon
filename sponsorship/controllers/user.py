from django.core.exceptions import ObjectDoesNotExist
from sponsorship.models import User

def auth(request):
  email = request.REQUEST.get('email', None)
  password = request.REQUEST.get('password', None)
