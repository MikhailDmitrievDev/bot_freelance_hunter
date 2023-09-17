from pydantic import BaseModel


class WL_BASE_AUTH_MODEL(BaseModel):
    action: str = "login"
    code: str = ""
    login: str = ""
    password: str = ""
    store_login: str = ""


class User(BaseModel):
    first_name: str


class UserPageProps(BaseModel):
    user: User


class ResponseTemplate(BaseModel):
    pageProps: UserPageProps