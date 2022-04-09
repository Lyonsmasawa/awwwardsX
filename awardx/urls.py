from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('submit-site/', views.submitSite, name="submit-site"),
    path('update-user/', views.updateUser, name="update-user"),
    path('register/', views.register, name="register")
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 