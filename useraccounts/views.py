from .serializers import UserSerializer
from .decorators import serialize_exceptions
from django.shortcuts import render
#from .factories import create_user_profile_interactor,get_user_profile_interactor,update_user_profile_interactor


#def home(request):
   # return(render(request,'basis.html'))

class UserView(object):

    def __init__(self,create_user_profile_interactor=None,get_user_profile_interactor=None,update_user_profile_interactor=None,delete_user_profile_interactor=None):
        self.create_user_profile_interactor = create_user_profile_interactor
        self.get_user_profile_interactor = get_user_profile_interactor
        self.update_user_profile_interactor = update_user_profile_interactor
        self.delete_user_profile_interactor = delete_user_profile_interactor
    
    #update user viewfunction
    
    def patch(self, id,firstname,lastname,college_name,email,department,skills,username):
        user = self.update_user_profile_interactor.set_params(id=id,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills,username=username).execute()
        body = UserSerializer.serialize(user)
        status = 200
        return body, status
    

    #Retrieve user viewfunction
    def get(self,id):
        user = self.get_user_profile_interactor.set_params(id=id).execute()

        body = UserSerializer.serialize(user)
        status = 200
        return body, status

    #Create user viewfunction
    def post(self, id,username, email,firstname,lastname):
        user = self.create_user_profile_interactor.set_params(id=id,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills,username=username).execute()

        body = UserSerializer.serialize(user)
        status = 200
        return body, status


    def delete(self, id):
        self.delete_user_profile_interactor.set_params(id=id).execute()

        body = None
        status = 200
        return body, status
    
