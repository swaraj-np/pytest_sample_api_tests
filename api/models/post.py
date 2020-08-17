from typing import List

from api.models.comment import Comment
from api.models.resource import ApiResource


class Post(ApiResource):

    def __init__(self, user_id: int, title: str, body: str, post_id: int = None, comments: List[Comment] = []):
        super().__init__(post_id)
        self.__user_id = user_id
        self.__title = title
        self.__body = body
        self.__comments = comments

    def get_title(self) -> str:
        return self.__title

    def get_body(self) -> str:
        return self.__body

    def get_user_id(self) -> int:
        return self.__user_id

    def set_title(self, title):
        self.__title = title

    def set_body(self, body):
        self.__body = body

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_comments(self, comments: List[Comment]):
        self.__comments = comments

    def get_comments(self) -> List[Comment]:
        return self.__comments

    def __eq__(self, other) -> bool:
        return self.get_user_id() == other.get_user_id() \
               and self.get_title() == other.get_title() \
               and self.get_body() == other.get_body() \
               and self.get_comments() == other.get_comments()

    def to_json(self) -> dict:
        post_json: dict = {}

        if self.get_id():
            post_json["id"] = self.get_id()

        post_json["userId"] = self.get_user_id()
        post_json["title"] = self.get_title()
        post_json["body"] = self.get_body()

        return post_json

    @staticmethod
    def from_json(json_data):
        if not ((type(json_data["userId"]) is int or type(json_data["userId"]) is str)
                and (type(json_data["id"]) is int)
                and (type(json_data["title"]) is str)
                and (type(json_data["body"]) is str)
        ):
            raise Exception("Provided json is not in the expected format")

        return Post(json_data["userId"],
                    json_data["title"],
                    json_data["body"],
                    post_id=json_data["id"]
                    )
