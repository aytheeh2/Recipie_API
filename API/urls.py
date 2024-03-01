from django.urls import include, path
from .import views
from rest_framework import routers
router =routers.SimpleRouter()
router.register('user',views.UserAPI)
urlpatterns = [
    # path('', views.get_all_recipies,),
    # path('create_recipie/', views.create_recipie,),
    # path('edit_recipie/<int:pk>/', views.edit_recipie,),
    # path('delete_recipie/<int:pk>/', views.delete_recipie,),
    # path('user/',views.User_ListCreate.as_view()),
    # path('user/',views.UserAPI.as_view({'get': 'list','post':'list'})),


    path('recipie/', views.recipie_ListCreate.as_view()),
    path('recipie/<int:pk>/', views.recipie_RetrieveUpdateDestroy.as_view()),
    path('review/',views.Review_or_Comment_view.as_view()),
    path('review/<int:pk>/',views.Review_or_Comment_view_RetrieveUpdateDestroy.as_view()),
    path('',include(router.urls)),# "user/"
    path('search/<str:q>',views.search_recipies)



]
