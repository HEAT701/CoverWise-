from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Warranty(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=100)
    expiry_date = models.DateField(null=True, blank=True)
    qr_data = models.TextField()
    warranty_image = models.ImageField(upload_to='warranty_cards/')

    def __str__(self):
        return f"{self.product_name} ({self.product_id})"
