from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=8, default=None, null=True)
    city = models.CharField(max_length=16, default=None, null=True)
    street = models.CharField(max_length=64, default=None, null=True)


class People(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    telephone = models.CharField(max_length=16)
    url = models.CharField(max_length=256, default=None, null=True)
    image = models.FileField(default=None, upload_to='static/people', null=True)

    address = models.ForeignKey(
        to=Address, on_delete=models.CASCADE, null=True,
        default=None
    )

    def __str__(self):
        return self.surname

    class Meta:
        ordering = ['name']
