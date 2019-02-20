from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    #tests = models.ManyToManyField(Testing, related_name='tests')
    telegram_username = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Test(models.Model):
    stud = models.ForeignKey(Student, related_name='tests', on_delete=models.CASCADE)
    test_name = models.CharField(max_length=50)
    points_for_test = models.IntegerField()

    def __str__(self):
        return self.test_name


