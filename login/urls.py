from django.urls import path
from login.views import index, login, logout, registration

app_name = 'login'

urlpatterns = [

    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),

]