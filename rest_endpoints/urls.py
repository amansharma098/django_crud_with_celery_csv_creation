from django.urls import path,include
from . views import StudentList,StudentDetails

urlpatterns = [
    path('student/',StudentList.as_view()),
    path('student/<int:pk>', StudentDetails.as_view()),
]