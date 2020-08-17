import pytest
import requests


@pytest.mark.basic
def test_all_posts(urls):
    response = requests.get(urls["posts"])

    assert response.status_code == 200

    json_data = response.json()

    for post in json_data:
        assert type(post["id"]) == int

        assert type(post["userId"]) == int

        assert type(post["title"]) == str
        assert post["title"].strip()


@pytest.mark.basic
def test_post_creation(urls):
    new_post = {
        "userId": 10,
        "title": "at nam consequatur ea labore ea harum",
        "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
    }
    #  create a new post
    response = requests.post(urls["posts"], data=new_post)

    assert response.status_code == 201

    # fetch the new post and verify values
    response = requests.get(urls["post_with_id"].format(100))

    assert response.status_code == 200

    post = response.json()
    assert post["userId"] == new_post["userId"]
    assert post["title"] == new_post["title"]
    assert post["body"] == new_post["body"]


@pytest.mark.basic
def test_posts_by_user(urls):
    user_id = 1
    # check number of posts by this user
    response = requests.get(urls["posts_by_user"].format(user_id))
    assert response.status_code == 200

    json_data = response.json()
    no_of_posts = len(json_data)

    new_post = {
        "userId": user_id,
        "title": "test title",
        "body": "some test post body text"
    }
    #  create a new post
    response = requests.post(urls["posts"], data=new_post)

    # check number of posts by this user again
    response = requests.get(urls["posts_by_user"].format(user_id))
    assert response.status_code == 200

    json_data = response.json()
    # check that the number of posts has increased by 1
    assert no_of_posts + 1 == len(json_data)


@pytest.mark.basic
def test_comments_on_post(urls):
    post_id = 1
    response = requests.get(urls["comments_on_post"].format(post_id))
    assert response.status_code == 200

    json_data = response.json()

    # check that all comments belong to the same post
    for comment in json_data:
        assert comment["postId"] == post_id

    no_of_comments = len(json_data)

    new_comment = {
        "postId": post_id,
        "name": "test user",
        "email": "tstmail1@somedomain.com",
        "body": "new test comment"
    }
    #  create a new comment
    response = requests.post(urls["posts"], data=new_comment)

    # check number of comments by this user again
    response = requests.get(urls["comments_on_post"].format(post_id))
    assert response.status_code == 200

    json_data = response.json()
    # check that the number of comments has increased by 1
    assert no_of_comments + 1 == len(json_data)

    # check that all comments belong to the same post
    for comment in json_data:
        assert comment["postId"] == post_id

