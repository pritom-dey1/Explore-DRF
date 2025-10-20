from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employee', views.EmployeeViewSet,basename='employee')
urlpatterns = [
    path('student/', views.StudentView),
    path('student/<int:pk>/', views.StudentDetailView),
    # path('employee/', views.EmployeeView.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('', include(router.urls)),
    path('blog/', views.BlogViewSet.as_view()),
    path('comment/', views.CommentViewSet.as_view()),
]

