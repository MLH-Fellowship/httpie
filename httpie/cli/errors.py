class Error(Exception):
    '''Base Class for custom exceptions'''
    def __init__(self, *args, **kwargs):
        super().__init__(self,*args, **kwargs)
    #TODO: Do I need to define custom methods/attributes for Error class or is *args, **kwargs,and built-in methods from Exception class sufficient?

class ConnectionError(Error):
    #TODO: Work on this class together
    '''Exception raised for error when connecting to server'''
    pass

class BasicAuthError(Error):
    '''Exception raised for wrong username and pw when authenticating'''
    #TODO: may need to account for different auth types within this class
    pass

class MethodMismatchError(Error):
    '''Exception raised when the wrong method is used with the wrong URL request'''
    pass
    #initialize class

    #define attributes such as error message and maybe the request or error itself?

    #define error by status code of response? or parse request to check whether url and method match?

    #define custom error message

        #TODO: Figure out what information is important to include to help user

    #if confirmed

    #return custom error message

    #do i need an else statement?

class LocalHostError(Error):
    '''Exception raised when the user fails to provide a valid localhost'''
    pass

class InvalidArgument(Error):
    '''Exception raised when user passes in invalid argument to a parameter'''
    pass

class OfflineError(Error):
    '''Exception raised when user attempts a request offline'''
    pass

#TODO: ADD the rest of the classes including a general catch-all one for errors we may miss
#TODO: Write tests for intended class functionctionality