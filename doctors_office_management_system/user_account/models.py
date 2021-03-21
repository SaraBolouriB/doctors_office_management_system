from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class all_users(models.Model):
    username = models.CharField(max_length=50,null=False, blank=False, primary_key=True)
    password = models.CharField(max_length=32)
    role = models.IntegerField(null=False, blank=False)

class normal_user(models.Model):
    user_id = models.ForeignKey(all_users, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50,null=False, blank=False)
    lname = models.CharField(max_length=50,null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=300,null=False, blank=False)

class doctor(models.Model):
    user_id = models.ForeignKey(all_users, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)
    address = models.CharField(max_length=500,null=False, blank=False)
    education = models.CharField(max_length=300,null=False, blank=False)
    dNumber = models.IntegerField(null=False, blank=False, unique = True)

class comment(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=False, blank=False, null=False)

class appointment(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=False)
    time = models.CharField(max_length=2, blank=False, null=False)

class working_time(models.Model):
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=False)
    start_time = models.CharField(max_length=2, blank=False, null=False)
    end_time = models.CharField(max_length=2, blank=False, null=False)

class favorite(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_id', 'doctor_id']
