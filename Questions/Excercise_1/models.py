from django.db import models

# Create your models here.


class RoutorDetail(models.Model):
    Ip_address = models.GenericIPAddressField(unique=True)
    Loopback = models.GenericIPAddressField(null=False)
    Hostname = models.CharField(max_length=30, null=False)
    sap_id = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.Ip_address)