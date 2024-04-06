

# from django.urls import path
# from rest_framework.routers import SimpleRouter
# from .views import AdminBlogViewSet

# router = SimpleRouter()
# router.register('blogs', AdminBlogViewSet, basename='blogs')

# urlpatterns = router.urls


# from .views import BloggerViewSet

# from django.urls import path
# from .views import *
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('admin/blogger', BloggerViewSet.as_view({
#         'get': 'list',
#         'post': 'create',
#     }), name='blogger'),
#     path('admin/blogger/blog', BloggerViewSet.as_view({
#         'get': 'retrieve',
#         'patch': 'update',
#         'delete': 'destroy',
#     }), name='blogger_blog'),
# ]


# urlpatterns = [
#     path('admin/blogger', BloggerViewSet.as_view(), name='blogger'),
#     path('admin/blogger/blog', BloggerViewSet.as_view()),
#     # path('blog_approve', views.blog_approve, name='blog_approve'),
# ]



# from .views import AdminBlogViewSet

# router = DefaultRouter()
# router.register(r'blogs', AdminBlogViewSet, basename='blog')

# urlpatterns = router.urls


# router = DefaultRouter()
# router.register(r'blogger', BloggerViewSet, basename='blogger')

# urlpatterns = router.urls


from django.urls import path

from .views import *

urlpatterns = [
    path('admin/blogger', BloggerViewSet.as_view(), name='admin_blogger_list'),
    path('administration/blogger', BloggerViewSet.as_view(), name='blogger-list'),
    path('administration/blogger',
         BloggerViewSet.as_view(), name='blogger-detail'),
    # path('administration/blogger',
    #      BloggerDetailView.as_view(), name='blogger-detail'),
    path('administration/blogger/blogs_waiting',
         SetBlogsView.as_view(), name='waiting-blogs'),
    path('administration/blogger/blog_approve',
         SetBlogsView.as_view()),
]
