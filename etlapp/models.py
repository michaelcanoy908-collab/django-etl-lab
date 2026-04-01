from django.db import models

class RawStudent(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.student_id

class CleanStudent(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    loaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"