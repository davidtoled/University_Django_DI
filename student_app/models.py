from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	date_naissance = models.DateField()

	def __str__(self):
		return self.first_name


class Note(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	matiere = models.CharField(max_length=20)
	note = models.PositiveIntegerField(default=0)
	coefficient = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.matiere

class Teacher(models.Model):
	prenom = models.CharField(max_length=20)
	nom = models.CharField(max_length=20)
	email = models.EmailField()
	date_naissance = models.DateField()
	matiere = models.CharField(max_length=20)
	
	def __str__(self):
		return self.prenom