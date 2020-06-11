class Error(Exception):
    '''Base Class for custom exceptions'''
    def __init__(self, *args, **kwargs):
        super().__init__(self,*args, **kwargs)
        
    #TODO: Do I need to define custom methods/attributes for Error class or is *args, **kwargs,and built-in methods from Exception class sufficient?

class ConnectionError(Error):
    #TODO: Work on this class together
    '''Exception raised for error when connecting to server'''
    pass

class AuthError(Error):
    '''Exception raised for wrong username and pw when authenticating'''
    #TODO: may need to account for different auth types within this class
  
  
class MethodMismatchError(Error):
    '''Exception raised when the wrong method is used with the wrong URL request'''
    def __init__(self,*args):
        self.exc = None
        self.message = None
        
    def __str__(self):
        self.message = "HTTP Error 405. Method not allowed."
        return self.message
        #TODO: Should I provide more information about appropriate methods?

# raise MethodMismatchError

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