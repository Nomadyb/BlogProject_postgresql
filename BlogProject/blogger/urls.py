from django.urls import path
# from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .views import *
# from .views import BlogCreateView, BlogDetailView

urlpatterns = [
    path("blogger/blog", BlogView.as_view(), name="blog"),

]


# urlpatterns = [
#     path("blogger/blog", BlogCreateView.as_view(), name="blog"),
#     path("blogger/blog", BlogDetailView.as_view(), name="blog"),
# ]



# urlpatterns = [
#     path("blogger/blog", BlogCreateView.as_view()),
#     path("blogger/blog/detail", BlogDetailView.as_view()),
#     path("blogger/blog/update", BlogUpdateView.as_view()),
#     path("blogger/blog/delete", BlogDeleteView.as_view()),
# ]


