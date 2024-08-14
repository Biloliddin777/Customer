from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='customers/', blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def joined(self):
        return

    class Meta:
        db_table = 'customer'