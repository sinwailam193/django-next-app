from ninja import Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str | None = None


@api.get("/me", response=UserSchema, auth=JWTAuth())
def helloworld(request):
    return request.user


api.register_controllers(NinjaJWTDefaultController)
