'''Test suite for custom exception classes'''
import mock
from pytest import raises
from requests import Request
from requests.exceptions import ConnectionError
from httpie.status import ExitStatus
from utils import HTTP_OK, http

#add mock patch decorator
def test_error_method(program):
    pass
    #send request with invalid method

    #get response from invalid request

    #verify HTTP response status is 405 meaning the request method is unauthorized ?(not sure if this is necessary)

    #verify that the correct error message is returned through cli