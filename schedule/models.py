from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=64)

    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=64, blank=True)

    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64, default="Belgium")

    def __str__(self):
        string = self.street + ", " + self.city

        if self.naam != "":
            string += " (" + self.name + ")"

        return string


class Class(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    vak = models.ForeignKey(Course)
    teacher = models.ForeignKey(Teacher, null=True)

    activity = models.CharField(max_length=64, blank=True)
    topic = models.TextField(blank=True)

    location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return self.vak.__str__()

    class Meta:
        ordering = ['start_date_time']


class Subject(models.Model):
    name = models.CharField(max_length=128)

    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
