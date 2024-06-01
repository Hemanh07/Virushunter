from django.urls import path
from. import views

urlpatterns = [
    path('file_scan', views.upload_and_scan_file, name='upload_and_scan'),path("url_scan", views.url_result,name='url_result'),
    
    path('',views.home,name='home',),
    
    path('home',views.home_page,name='home_page',)

]
## want to add this 
#path('url_scan',views.url_scanner,name='url_scan'),