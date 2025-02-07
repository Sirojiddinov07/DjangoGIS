from django.urls import path, include
from . import views as user_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', user_views.register_user),
    path('token/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_account_password/',
         user_views.change_account_password, name='change_password'),
    path('send_verify_email/', user_views.send_verify_email,
         name='send_verify_email',),
    path('verify_email/', user_views.verify_email, name='verify_email',),
    path('password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),

]
