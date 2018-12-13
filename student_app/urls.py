from django.urls import path
from . import views

app_name = 'student_app'
app_name = 'university'


urlpatterns = [
path('students', views.index, name='students'),
path('student/<int:student_id>/', views.details , name='student'),
path('teachers', views.teachers, name='teachers'),
path('teachers/<int:teacher_id>/', views.teacher , name='teacher'),
path('teachers/<int:teacher_id>/', views.teacher , name='teacher'),
path('create_teacher', views.createNewTeacher, name='create_teacher'),
]