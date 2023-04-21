from portal.controllers.user_controller import UserController, GetUserRequest
from portal.controllers.user_controller import CreateUserRequest
from django.http import HttpResponse

from django.views.generic import View
import pdb

from portal.models import User


class UserView(View):

    user_controller = UserController()

    def post(self, request, *args, **kwargs):
        create_user_request = CreateUserRequest(request.POST["name"],
                                                  request.POST["email"],
                                                  User.Role(request.POST["role"]))

        user, = self.user_controller.create(create_user_request)
        return HttpResponse(user.id)

    def get(self, request, *args, **kwargs):
        # pdb.set_trace()
        get_user_request = GetUserRequest(kwargs["id"])

        user, = self.user_controller.get(get_user_request)
        return HttpResponse(user)
