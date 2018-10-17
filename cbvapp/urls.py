from django.urls import path
from cbvapp import views

app_name='cbvapp'

urlpatterns = [
    path('',views.collageList.as_view(),name='list'),
    path('<int:pk>/',views.collageDetail.as_view(),name='detail'),
    path('create/',views.CollageCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.CollageUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.CollageDeleteView.as_view(),name='delete'),


]
