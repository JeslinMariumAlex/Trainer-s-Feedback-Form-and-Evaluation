from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class Batch(models.Model):
    batch_name=models.CharField(max_length=30)

    def __str__(self):
        return self.batch_name
    
class Course(models.Model):
    course_name=models.CharField(max_length=30)

    def __str__(self):
        return self.course_name
    
class Feedback(models.Model):
    RATING=((5,'5'),
            (4,'4'),
            (3,'3'),
            (2,'2'),
            (1,1))
    student_name=models.CharField(max_length=30,default=None)
    # student_name=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name='student',limit_choices_to={'groups__name':"Students"})
    trainer_name=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,limit_choices_to={'groups__name':"Trainers"})
    batch_name=models.ForeignKey(Batch,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    rating=models.IntegerField(choices=RATING,default=None,verbose_name="Rating out of 5")
    suggestion=models.TextField()

    def __str__(self):
        return self.suggestion
    