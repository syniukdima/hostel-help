from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),

    path('profile/<int:dormitory>/', views.profile, name='profile'),
    path('folders/', views.folders, name='folders'),

    path('delete/<int:dormitory>/<int:report_id>/', views.delete_report, name='delete_report'),
    path('report/', views.report, name='report'),
    path('change_status/<int:dormitory>/<int:report_id>/', views.change_status, name='change_status'),
    path('reply/', views.reply, name='reply'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),  
]

