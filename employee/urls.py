from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Catalog.employee import views

# urlpatterns = [
#     path('', views.employee_list, name='employee_list'),
# ]

urlpatterns = [
    path('', views.employee_list, name='employee_list')
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
