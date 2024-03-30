from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from . import views


urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("posts/", views.PostList.as_view(), name="post-list"),


    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
