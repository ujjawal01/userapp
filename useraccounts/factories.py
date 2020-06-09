from .repositories import UserRepo
from useraccounts.interactors import CreateUserAccountInteractor,UpdateUserAccountInteractor,GetUserAccountInteractor,DeleteUserAccountInteractor
from .views import UserView

class create_user_repo_factory(object):
    @staticmethod
    def get():
        return UserRepo()


class create_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return CreateUserAccountInteractor(user_repo)

   

class get_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return GetUserAccountInteractor(user_repo)



class update_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return UpdateUserAccountInteractor(user_repo)

class delete_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return DeleteUserAccountInteractor(user_repo)

class User_view_factory(object):
    @staticmethod
    def create(request, **kwargs):
        return UserView(create_user_account_interactor_factory.get(),get_user_account_interactor_factory.get(),update_user_account_interactor_factory.get(),delete_user_account_interactor_factory.get())