# Create your models here.
from initiatives.models import ORMInitiative
from django.db import models

Roles_options = (
    ("1", "Student"),
    ("2", "Admin"),
    ("3", "Internal team"),
    ("4", "Teacher"),
    ("5", "Others"),
)



class Email_verification(models.Model):
    email = models.EmailField(primary_key=True)
    token = models.CharField(max_length=1024)
    expiry = models.DateTimeField(auto_now_add=False)



class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Skill (models.Model):
     skill_id = models.IntegerField(primary_key=True)
     skill_name = models.CharField(max_length = 50)

     def __str__(self):
        return self.skill_name

class ORMUser(models.Model):
     User_id = models.IntegerField(primary_key = True)
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     college_name = models.CharField(max_length=50)
     email = models.EmailField()
     is_email_verified = models.BooleanField(default=False)
     role = models.CharField( max_length = 20, choices = Roles_options,default = '1') 
     department = models.OneToOneField(Department,on_delete=models.CASCADE)
     skill = models.ManyToManyField(Skill)
     #initiatives = models.ManyToManyField(ORMInitiative)
     userimage = models.ImageField(upload_to=None)
     username = models.CharField(max_length=50)
     password = models.CharField(max_length=30,null=True)
     disable_account = models.BooleanField(default=False)
     last_login = models.DateTimeField()
     login_count = models.PositiveIntegerField()
     is_active = models.BooleanField(default=True)



class ORMProject(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    technology = models.CharField(max_length=200)
    #user_id = models.ForeignKey(ORMUser,on_delete = models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(ORMUser, related_name='user',on_delete=models.CASCADE)
    About_me = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    projects = models.ForeignKey(ORMProject,on_delete=models.CASCADE)
