from portal.models import User

class CreateUserRequest:
    # length in mins
    def __init__(self, name: str, email: str, role: User.Role):
        self.name = name
        self.email = email
        self.role = role


class GetUserRequest:
    # length in mins
    def __init__(self, id: int):
        self.id = id


class UserController:

    def create(self, request: CreateUserRequest) -> User:
        user = User(name=request.name, email=request.email, role=request.role)
        user.save()
        return user,

    def get(self, request: GetUserRequest) -> User:
            user = User.objects.get(id=request.id)
            return user,
