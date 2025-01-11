from django.db import models

# Create your models here.


class Transcation(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    checkout_id=models.CharField(max_length=100,unique=True)
    mpesa_code=models.CharField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.mpesa_code} + {self.amount} kes'





