
from django.contrib import admin
from django.urls import path,include
from api import views
# from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken

#creating Router Object
router=DefaultRouter()

# Registering MovieViewset With Router
# router.register('movieapi', views.movieModelViewSet , basename='movie')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieapi/', views.movieList.as_view()),
    path('collectiondatadelete/',views.collection_api),
    path('collectionapi/', views.collectionList.as_view()),
    path('',include((router.urls))),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('register/',CustomAuthToken.as_view()),
    # path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh_pair'),

]
