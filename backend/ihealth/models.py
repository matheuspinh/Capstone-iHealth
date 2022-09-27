from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.


class Appointement(models.Model):
    patient = models.ForeignKey('users.User', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='doctor')
    date = models.DateTimeField(default=timezone.now)
    reason = models.TextField(max_length=500)
    status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return self.patient.email + ' ' + self.doctor.email + ' ' + self.date.strftime('%Y-%m-%d %H:%M:%S') + ' ' + self.reason + ' ' + self.status
