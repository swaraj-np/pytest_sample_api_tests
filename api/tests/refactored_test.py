from typing import List

import pytest

from api.actions import api_actions
from api.models.comment import Comment
from api.models.post import Post


@pytest.mark.refactored
def test_all_posts():
    posts: List[Post] = api_actions.get_all_posts()

    for post in posts:
        assert post.get_title().strip()
        assert post.get_body().strip()


@pytest.mark.refactored
def test_post_creation():
    new_post = Post(10,
                    "at nam consequatur ea labore ea harum",
                    "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
                    )

    api_actions.create_new_post(new_post)

    post = api_actions.get_post_with_id(100)

    assert post == new_post


@pytest.mark.refactored
def test_posts_by_user():
    user_id = 1

    posts = api_actions.get_posts_by_user(user_id)
    no_of_posts = len(posts)

    new_post = Post(user_id, "test title", "some test post body text")
    api_actions.create_new_post(new_post)

    posts = api_actions.get_posts_by_user(user_id)
    assert len(posts) == no_of_posts + 1


@pytest.mark.refactored
def test_comments_on_post(urls):
    post_id: int = 1
    comments: List[Comment] = api_actions.get_comments_on_post(post_id)

    # check that all comments belong to the same post
    for comment in comments:
        assert comment.get_post_id() == post_id

    no_of_comments = len(comments)

    # post a new comment
    new_comment = Comment(post_id, "tstmail1@somedomain.com", "test user", "new test comment")
    api_actions.create_new_comment(new_comment)

    # check number of comments by this user again
    comments: List[Comment] = api_actions.get_comments_on_post(post_id)

    # check that the number of comments has increased by 1
    assert len(comments) == no_of_comments + 1

    # check that all comments belong to the same post
    for comment in comments:
        assert comment.get_post_id() == post_id

