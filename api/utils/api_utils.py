base_url: str = "https://jsonplaceholder.typicode.com/"

url_dict = {
    "posts": f"{base_url}posts",
    "post_with_id": f"{base_url}posts/{{}}",
    "posts_by_user": f"{base_url}user/{{}}/posts",
    "posts_filtered_by_user": f"{base_url}posts?userId={{}}",
    "comments": f"{base_url}comments",
    "comments_on_post": f"{base_url}posts/{{}}/comments"
}