from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,default='',null=True,blank=True)
    email=models.EmailField()



#refreal Link 
# models.py
import uuid
from django.db import models
from django.contrib.auth.models import User

class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)
    signups = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:8]  # Generate a unique 8-character code
        super().save(*args, **kwargs)

    def track_click(self):
        self.clicks += 1
        self.save()

    def track_signup(self):
        self.signups += 1
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.referral_code}"
