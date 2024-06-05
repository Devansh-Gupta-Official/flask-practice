#2 functions- authentication and identity

from user import User

users=[User(1,'Devu','mypassword'),User(2,'Gojo','infinite')]

username_mapping={u.username:u for u in users}
userid_mapping={u.id:u for u in users}

def authenticate(username,password):
    #check if user exists and return user
    user=username_mapping.get(username,None) #get is a dictionary method that returns None if the key is not found instead of error
    if user and user.password==password:
        return user
    
#this is needed by jwt syntax
def identity(payload):
    user_id=payload['identity']
    return userid_mapping.get(user_id,None)