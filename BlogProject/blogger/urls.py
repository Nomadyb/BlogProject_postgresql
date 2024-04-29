from django.urls import path
# from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .views import *
# from .views import BlogCreateView, BlogDetailView


urlpatterns = [
    path("blogger/blog", BlogView.as_view(), name="blog"),
    path('blogger/blog/comments',CommentAPIView.as_view(), name='blog-comments'),
    

]



# urlpatterns = [
#     path("blogger/blog", BlogView.as_view(), name="blog"),
#     path("blogger/blog/add_comment",
#          CreateCommentAPIView.as_view(), name="add_comment"),
#     path('blogger/blog/<int:blog_id>/comments',
#          ListCommentAPIView.as_view(), name='blog-comments'),
#     path("blogger/comment", DetailCommentAPIView.as_view(), name="detail_comment"),
# ]


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


