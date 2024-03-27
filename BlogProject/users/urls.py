from django.urls import path
from .views import RegisterView, LoginView, HomeView, ProfileDetailView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("home/", HomeView.as_view()),
    path("profile/", ProfileDetailView.as_view(), name="profile-detail"),
    # path('<int:id>/', ProfileDetailView.as_view(), name='profile_detail'),
    # user path eklenecek user get ile detail getir. bir put tanımla
]
