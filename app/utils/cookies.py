import json


class CookiesManager:
    """
    Operations with cookies for further use.
    """

    def __init__(self, cookies):
        self.__cookies = cookies

    def write_cookie(self):
        # TODO: edit this for mongoDB
        with open("cookies.json", "w") as file:
                json.dump(dict(self.__cookies), file)


    def get_cookies():
        # TODO: edit this for mongoDB
        with open("cookies.json", "r") as file:
            cookies = json.load(file)
        return cookies