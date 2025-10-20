from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employee', views.EmployeeViewSet,basename='employee')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('comment', views.CommentViewSet, basename='comment')
urlpatterns = [
    path('student/', views.StudentView),
    path('student/<int:pk>/', views.StudentDetailView),
    # path('employee/', views.EmployeeView.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('', include(router.urls)),
 
]

