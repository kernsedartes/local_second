# Create your models here.
import uuid
from django.db import models
from django.urls import reverse


class ProductLink(models.Model):
    product_id = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default="RUB")
    image_base64 = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("product_view", kwargs={"uuid": str(self.uuid)})
