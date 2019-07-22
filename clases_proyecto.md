# Clases para el proyecto

El proyecto consiste en una plataforma para conectar personas que desean aprender X con personas que pueden ense;ar X.

## Clases principales
- Persona (quien aprende o quien ensena)
- Tema (lo que se aprende o se ensena)

```py

def decirHola(nombre):
  print "Hola " + nombre

class Person():
  name = ''
  last_name = ''
  email = ''
  interested_topics = ''
  password = ''
  facebook_id = ''
  profile_pic = ''

  @staticmethod
  def comer():
    """ Metodo de clase o metodo estatico"""
    print "Yo como"

  def nombreCompleto(self):
    """ Metodo de instancia"""
    return self.name + self.last_name

  def __init__(self, name, last_name):
    """ Metodo magico """
    print "Construyendo persona: " + name + last_name
    self.name = name
    self.last_name = last_name

  def __add__(self, other):
    return "Estoy sumando a "+self.nombreCompleto() + "con " + other.nombreCompleto()

  def __str__(self):
    return "Soy una persona y me llamo " + self.nombreCompleto()

class Teacher(Person):
  courses
  rating
  teaching_schedule

  def __str__(self):
    return "Soy un maestro y me llamo " + self.nombreCompleto()

class Student(Person):
  courses

  def __str__(self):
    print super(Student, self).__str__() # Manda a llamar la funcion __str__ de Person
    return "Soy un estudiante y me llamo " + self.nombreCompleto()

class Course():
  subject
  teachers
  students
  exams
  homework

class Exam():
  course
  student
  content
  grade
  date

class Homework():
  date
  student
  course
  grade
```
