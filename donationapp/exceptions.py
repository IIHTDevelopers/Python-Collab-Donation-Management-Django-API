
from rest_framework.exceptions import APIException
class IdNotAvailable(APIException):
    default_detail = 'Specified id is not available'

class InvalidData(APIException):
    default_detail = 'Specified data is invalid'
