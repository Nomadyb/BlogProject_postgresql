from django.urls import path
from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

# urlpatterns = [
#     path("blogger/blog", BlogCreateView.as_view(), name="blog_create"),
#     # path("blogger/blog/detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
#     path("blogger/blog/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
#     path("blogger/blog/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
#     # path("blogger/blog/delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
#     # URL'den id parametresi alınmıyor
#     path("blogger/blog/", BlogDeleteView.as_view(), name="blog_delete"),


# ]


# from django.urls import path
# from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("blogger/blog", BlogCreateView.as_view(), name="blog_create"),
    path("blogger/blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    #path("blogger/blog/", BlogDetailView.as_view(), name="blog_detail"),
    # path("blogger/blog/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    # path("blogger/blog/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
    path('blogger/blog/<int:pk>/update/',
         BlogUpdateView.as_view(), name='blog-update'),
    path('blogger/blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    ]


# urlpatterns = [
#     path("blogger/blog", BlogCreateView.as_view(), name="blog_create"),
#     path("blogger/blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
#     path("blogger/blog/<int:pk>/update/",
#          BlogUpdateView.as_view(), name="blog_update"),
#     path("blogger/blog/<int:pk>",
#          BlogDeleteView.as_view(), name="blog_delete"),
# ]


