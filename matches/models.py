from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Match(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
        ('cancelled', 'Cancelled'),
    ]

    # id=models.AutoField(primary_key=True)
    location=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    futsal_name=models.CharField(max_length=100)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')  #open, full, cancelled
    total_slots=models.IntegerField()

class MatchPlayer(models.Model):
    # id=models.AutoField(primary_key=True)
    match=models.ForeignKey(Match, on_delete=models.CASCADE)
    player=models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at=models.DateTimeField(auto_now_add=True)