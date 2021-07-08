from django.db import models

# Create your models here.

class createQ(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)

    def __str__(self):
        return self.question 

class staff_reg(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class stud_reg(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email_id=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email_id

class stud_res(models.Model):
    question = models.CharField(max_length=200)
    youranswer=models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class stu_rec(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)

    def __str__(self):
        return self.question