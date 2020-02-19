from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.course_name)

class Task(models.Model):
    discription = models.CharField(max_length=200)
    time_due = models.DateTimeField

    def __str__ (self):
        return "%s due: %s" % (self.discription, self.time_due)