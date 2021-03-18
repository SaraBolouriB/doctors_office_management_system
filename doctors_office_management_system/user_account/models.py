from django.db import models

class comment(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    comment = models.Textfield(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=False)

class appointment(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=False)

class working_time(models.Model):
    doctor_id = models.IntegerField()
    day = models.DateField()
    start_time = models.Charfield()
    end_time = models.Charfield()

class favorite(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()