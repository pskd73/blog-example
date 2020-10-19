class User:
    def __init__(self, user_dict: dict):
        self.email = user_dict['email']
        self.name = user_dict['name']


class GoogleUser(User):
    def __init__(self, user_dict: dict):
        super(GoogleUser, self).__init__(user_dict)
        self.google_user_id = user_dict['guid']


class FacebookUser(User):
    def __init__(self, user_dict: dict):
        super(FacebookUser, self).__init__(user_dict)
        self.fb_user_id = user_dict['fbid']


class UserFactory:
    @classmethod
    def get(cls, user_dict: dict) -> User:
        if user_dict.get('guid') is not None:
            return GoogleUser(user_dict)
        if user_dict.get('fbid') is not None:
            return FacebookUser(user_dict)
        raise NotImplementedError('Invalid user')


## somewhere in code
## get user_dict from database/or some data store
user_dict_from_db = {'guid': '1', 'email': 'abc@def.com', 'name': 'Abc Ghi'}
user = UserFactory.get(user_dict_from_db)
print(user.name) # I know that user contains name, does not matter what variant of user it is
if (type(user) == GoogleUser):
    print('I can still do variant specific things, if required')