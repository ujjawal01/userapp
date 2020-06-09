from .models import ORMUser
from .entities import User
from .exceptions import EntityDoesNotExistException

class UserRepo(object):

    
    
    def _decode_db_user(self, db_user):
        return User(user_id=db_user.id,firstname=db_user.firstname, lastname=db_user.lastname,college_name=db_user.college_name, email=db_user.email,department=db_user.department,skills=db_user.skills,userimage=db_user.userimage,username=db_user.username)



    def create_user(self,user_id=None,username=None,firstname=None,lastname=None,college_name=None,email=None,department=None,skills=None):
        created_orm_user = ORMUser.objects.create(user_id=user_id,username=username,firstname=firstname,lastname=lastname,college_name=college_name,email=email,department=department,skills=skills)
        created_orm_user.user_id = User.user_id
        created_orm_user.firstname = User.firstname
        created_orm_user.lastname = User.lastname
        created_orm_user.college_name = User.college_name
        created_orm_user.email = User.email
        created_orm_user.role = User.role
        created_orm_user.is_email_verified =User.is_email_verified
        created_orm_user.department = User.department
        created_orm_user.skills = User.skills
        created_orm_user.userimage = User.userimage
        created_orm_user.username = User.username
        created_orm_user.save()

        return self._decode_db_user(created_orm_user)
    

    def get_user(self, id=None):
        try:
            if id is not None:
                return self._decode_db_user(ORMUser.objects.get(id=id))

        except ORMUser.DoesNotExist:
            raise EntityDoesNotExistException
    
    
    def update_user(self, user):

        orm_user = ORMUser.objects.get(id=user.id)

        orm_user.firstname = user.firstname
        orm_user.lastname = user.lastname
        orm_user.college_name = user.college_name
        orm_user.email = user.email
        orm_user.department = user.department
        orm_user.skills = user.skills
        #orm_user.userimage = user.userimage
        orm_user.username = user.username
        orm_user.save()

        return self._decode_db_user(orm_user)


    def delete_user(self, user):
        ORMUser.objects.filter(id=id).delete()
        

        
    