import uuid
from django.db import models

# Modelo para el prodcuto flan
class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name

# Modelo para el formulario de contacto
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name =  models.CharField(max_length=64)
    message = models.TextField()

