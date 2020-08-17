from typing import List

import requests

from api.models.comment import Comment
from api.models.post import Post
from api.utils.api_utils import url_dict


def get_all_posts() -> List[Post]:
    response = requests.get(url_dict["posts"])

    assert response.status_code == 200

    post_list: List[Post] = []
    for post_json in response.json():
        post_list.append(Post.from_json(post_json))

    return post_list


def create_new_post(new_post: Post) -> Post:
    response = requests.post(url_dict["posts"], data=new_post.to_json())

    assert response.status_code == 201

    return Post.from_json(response.json())


def create_new_comment(new_comment: Comment) -> Comment:
    response = requests.post(url_dict["comments"], data=new_comment.to_json())

    assert response.status_code == 201

    return Comment.from_json(response.json())


def get_post_with_id(post_id: int) -> Post:
    response = requests.get(url_dict["post_with_id"].format(post_id))

    assert response.status_code == 200

    return Post.from_json(response.json())


def get_posts_by_user(user_id: int) -> List[Post]:
    response = requests.get(url_dict["posts_by_user"].format(user_id))
    assert response.status_code == 200

    post_list: List[Post] = []
    for post_json in response.json():
        post_list.append(Post.from_json(post_json))

    return post_list


def get_comments_on_post(post_id: int) -> List[Comment]:
    response = requests.get(url_dict["comments_on_post"].format(post_id))
    assert response.status_code == 200

    comment_list: List[Comment] = []
    for comment_json in response.json():
        comment_list.append(Comment.from_json(comment_json))

    return comment_list

