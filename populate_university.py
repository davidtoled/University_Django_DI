import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_project.settings')
import django
django.setup()


import random
from faker import Faker
from student_app.models import Student, Note, Teacher


fakegen = Faker()
matieres = ["Français", "Maths", "Physique", "Magie"];

def populate_teacher():
    for teacher in range(3):
        newProffesor = Teacher.objects.get_or_create(nom=fakegen.last_name(), prenom=fakegen.first_name(), email=fakegen.email(), matiere=random.choice(matieres), date_naissance=fakegen.date())
        print(teacher)



if __name__ == '__main__':
 print('populate script...')
 populate_teacher()
 print('done populating.')