from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



