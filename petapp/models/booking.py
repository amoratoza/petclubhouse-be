from django.db import models
from .pet     import Pet

class Booking(models.Model):
    id    = models.AutoField(primary_key=True)
    refpet = models.ForeignKey(Pet, related_name='booking', on_delete=models.CASCADE)
    checkin  = models.DateField()
    checkout = models.DateField()
    fee   = models.IntegerField()
    #services = models.ForeignKey(Service, related_name='services', on_delete=models.CASCADE)
    paymenttype  = models.CharField('Payment type', max_length=10)
    bank  = models.CharField('bank',max_length=15)
    accounttype = models.CharField('Account type',max_length=10)
    accountnum   = models.IntegerField('Account number')
    payed= models.BooleanField(default=True)
