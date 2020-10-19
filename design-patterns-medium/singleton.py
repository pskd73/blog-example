class UserService:
    
    __instance = None

    def __init__(self):
        if self.__instance is None:
            UserService.__instance = self
        else:
            raise Exception('Instance already initiated!')

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            UserService()
        return cls.__instance



print(UserService.get_instance())
print(UserService.get_instance())
