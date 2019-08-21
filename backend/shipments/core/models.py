from django.db import models

# Create your models here.


class Shipment(models.Model):

    expedition = models.DateTimeField(verbose_name="Expedition", auto_now_add=True)
    sender_name = models.CharField(verbose_name="Sender Name", max_length=150)
    recipient_name = models.CharField(verbose_name="Recipient Name", max_length=150)
    sender_address = models.TextField(verbose_name="Sender")
    recipient_address = models.TextField(verbose_name="Recipient")
    postal_code = models.CharField(verbose_name="Postal Code", max_length=36)
    shipment_code = models.CharField(verbose_name="Product Code", max_length=36)

    def __str__(self):
        return self.shipment_code

    class Meta:
        ordering = ['shipment_code', 'id']
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"
