from django.db import models

class comment(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    comment = models.Textfield(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)