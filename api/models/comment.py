from api.models.resource import ApiResource


class Comment(ApiResource):

    def __init__(self, post_id: int, email: str, name: str, body: str, comment_id: int = None):
        super().__init__(comment_id)
        self.__post_id = post_id
        self.__name = name
        self.__email = email
        self.__body = body

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_body(self) -> str:
        return self.__body

    def get_post_id(self) -> int:
        return self.__post_id

    def set_email(self, email):
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_body(self, body):
        self.__body = body

    def set_post_id(self, post_id):
        self.__post_id = post_id

    def __eq__(self, other) -> bool:
        return self.get_post_id() == other.get_post_id() \
                and self.get_name() == other.get_name() \
                and self.get_email() == other.get_email() \
                and self.get_body() == other.get_body()

    def to_json(self) -> dict:
        comment_json: dict = {}

        if self.get_id():
            comment_json["id"] = self.get_id()

        comment_json["postId"] = self.get_post_id()
        comment_json["email"] = self.get_email()
        comment_json["name"] = self.get_name()
        comment_json["body"] = self.get_body()

        return comment_json

    @staticmethod
    def from_json(json_data):
        if not ((type(json_data["postId"]) is int or type(json_data["postId"]) is str)
                and (type(json_data["id"]) is int)
                and (type(json_data["email"]) is str)
                and (type(json_data["name"]) is str)
                and (type(json_data["body"]) is str)
        ):
            raise Exception("Provided json is not in the expected format")

        return Comment(json_data["postId"],
                       json_data["name"],
                       json_data["email"],
                       json_data["body"],
                       comment_id=json_data["id"]
                       )
