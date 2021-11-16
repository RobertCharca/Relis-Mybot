from django.db import models

# Create your models here.
#Students
class Alumnos(models.Model):
    id_alumno = models.IntegerField(db_column='Id_Alumno', primary_key=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=20)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=20)  # Field name made lowercase.
    dni = models.IntegerField(db_column='DNI')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=30)  # Field name made lowercase.
    cod_carrera = models.CharField(db_column='Cod_Carrera', max_length=3)  # Field name made lowercase.
    correo_alumno = models.CharField(db_column='Correo_Alumno', max_length=30)  # Field name made lowercase.
    password_alumno = models.CharField(db_column='Password_Alumno', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alumnos'

#Career
class Carreras(models.Model):
    cod_carrera = models.CharField(db_column='Cod_Carrera', primary_key=True, max_length=3)  # Field name made lowercase.
    nom_carrera = models.CharField(db_column='Nom_Carrera', max_length=70)  # Field name made lowercase.
    capacidad = models.IntegerField(db_column='Capacidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carreras'

#CAI_Questions
class Preguntas(models.Model):
    id_pregunta = models.IntegerField(db_column='Id_Pregunta', primary_key=True)  # Field name made lowercase.
    pregunta = models.CharField(db_column='Pregunta', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preguntas'

#Teachers
class ProfesoresEncargados(models.Model):
    id_profesor = models.IntegerField(db_column='Id_Profesor', primary_key=True)  # Field name made lowercase.
    nom_profesor = models.CharField(db_column='Nom_Profesor', max_length=20)  # Field name made lowercase.
    ape_profesor = models.CharField(db_column='Ape_Profesor', max_length=20)  # Field name made lowercase.
    dni_profesor = models.IntegerField(db_column='DNI_Profesor')  # Field name made lowercase.
    celular_profesor = models.IntegerField(db_column='Celular_Profesor')  # Field name made lowercase.
    correo_profesor = models.CharField(db_column='Correo_Profesor', max_length=30)  # Field name made lowercase.
    cod_carrera = models.CharField(db_column='Cod_Carrera', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profesores_encargados'

#CAI_Answers
class Respuestas(models.Model):
    id_respuesta = models.IntegerField(db_column='Id_Respuesta', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='Respuesta', max_length=50)  # Field name made lowercase.
    id_pregunta = models.IntegerField(db_column='Id_Pregunta')  # Field name made lowercase.
    cantidad_respondida = models.IntegerField(db_column='Cantidad_respondida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'respuestas'