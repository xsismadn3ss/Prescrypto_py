from .models import Users
class Auth():
    """Auth
       class to make auth object wich validate if the session is started or don't  
    """
    def __init__(self, state:bool, id, description = "", user = None):
        self.id = id
        self.state = state
        self.description = description
        self.user = user

auth = Auth(False, None)