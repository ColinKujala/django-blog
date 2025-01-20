from django.urls import path
from blogging.views import stub_view, BlogListView, BlogDetailView, add_post_view


urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("add/", add_post_view, name="add_post"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
