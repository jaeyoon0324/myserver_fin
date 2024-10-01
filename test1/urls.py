from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.make_new, name = 'make_new_post'),
    path('<int:pk>/', views.single_post_page, name='single_post_page'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),  # 게시물 삭제 URL
]
