from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    donation_name = models.CharField(max_length=50)
    donation_type = models.CharField(max_length=50)
    donation_amount = models.CharField(max_length=50)
    donation_reference = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    donor_name = models.CharField(max_length=50)
    donor_address = models.CharField(max_length=50)
    donor_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.donation_name} {self.donation_reference}"


