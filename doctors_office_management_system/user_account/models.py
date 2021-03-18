from django.db import models

class comment(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    doctor_id = models.IntegerField(null=False, blank=False)
    comment = models.Textfield(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=False)

class appointment(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    doctor_id = models.IntegerField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=False)

class working_time(models.Model):
    doctor_id = models.IntegerField(null=False, blank=False)
    day = models.DateField()
    start_time = models.Charfield()
    end_time = models.Charfield()

class favorite(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    doctor_id = models.IntegerField(null=False, blank=False)

