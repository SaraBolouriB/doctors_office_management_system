from django.db import models

class comment(models.Model):
    user_id = models.ForeignKey('normal_user', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('doctor', on_delete=models.CASCADE)
    comment = models.Textfield(max_length=200, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        unique_together = ['user_id', 'doctor_id']

class appointment(models.Model):
    user_id = models.ForeignKey('normal_user', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('doctor', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=False)

    class Meta:
        unique_together = ['user_id', 'doctor_id']

class working_time(models.Model):
    doctor_id = models.ForeignKey('doctor', on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.Charfield()
    end_time = models.Charfield()

class favorite(models.Model):
    user_id = models.ForeignKey('normal_user', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('doctor', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_id', 'doctor_id']
