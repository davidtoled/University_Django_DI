from django.shortcuts import render
from student_app.models import Student, Note, Teacher
from student_app.forms import TeacherForm
import datetime

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students':students})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request,'students/details.html',{'student':student})

def teachers(request):
	teachers = Teacher.objects.all()[:10]
	return render(request, 'teachers/index.html', context={ 'teachers': teachers })

def teacher(request, teacher_id):
	teacher = Teacher.objects.get(id=teacher_id)
	return render(request, 'teachers/teacherDetails.html', context={ 'teacher': teacher })

def createNewTeacher(request):
	if request.method == 'POST':
		prenom = request.POST.get('prenom')
		nom = request.POST.get('nom')
		email = request.POST.get('email')
		matiere = request.POST.get('matiere')
		date_naissance = datetime.datetime.now()
		Teacher.objects.get_or_create(prenom=prenom, nom=nom, email=email,matiere=matiere, date_naissance=date_naissance)[0]


	return render(request, 'teachers/createTeacher.html', context={ 'createTeacher': TeacherForm() })