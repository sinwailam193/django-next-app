from ninja import NinjaAPI, Schema

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str | None = None


@api.get("/me", response=UserSchema)
def helloworld(request):
    return request.user
