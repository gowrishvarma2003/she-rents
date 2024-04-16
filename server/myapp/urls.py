from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static  


urlpatterns = [
    path('xxx/', views.printname.as_view()),
    path('signup/', views.signup.as_view()),
    path('login/', views.login.as_view()),
    path('register/', views.renter.as_view()),
    path('city/', views.citylist.as_view()),
    path('search/', views.searchcity.as_view()),
    path('detailes/', views.details.as_view()),
    path('request/', views.request.as_view()),
    path('getreq/', views.getrequests.as_view()),
    path('accept/', views.accept.as_view()),
    path('myreq/', views.myrequests.as_view()),
    path('getto/', views.getto.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)