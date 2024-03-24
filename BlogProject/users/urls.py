from django.urls import path
from .views import RegisterView, LoginView, HomeView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("home/", HomeView.as_view()),
    # user path eklenecek user get ile detail getir. bir put tanımla
]
