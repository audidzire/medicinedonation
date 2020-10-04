from django.db import models
#from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db import models
from django.conf import settings




class m_donation(models.Model):
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    description = models.TextField()
    availability_status = models.BooleanField(default=True)

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.brand_name



