from django.urls import path
# from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .views import BlogView


urlpatterns = [
    path("blogger/blog", BlogView.as_view(), name="blog"),
]


# urlpatterns = [
#     path("blogger/blog", BlogCreateView.as_view(), name="blog_create"),
#     path("blogger/blog/detail", BlogDetailView.as_view(), name="blog_detail"),
#     path("blogger/blog/update", BlogUpdateView.as_view(), name="blog_update"),
#     path("blogger/blog/delete", BlogDeleteView.as_view(), name="blog_delete"),
# ]

