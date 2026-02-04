from django.db import models

class Territory(models.Model):
    pct_code = models.CharField(primary_key=True, max_length=6)
    territory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.territory_name


class Account(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('MedRep', 'MedRep'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=64)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    pct_code = models.ForeignKey(Territory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name


class Prescriber(models.Model):
    md_code = models.CharField(primary_key=True, max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    pct_code = models.ForeignKey(Territory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name


class Prescription(models.Model):
    md_code = models.ForeignKey(Prescriber, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField()
    rx_count = models.PositiveSmallIntegerField()
    remarks = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('md_code', 'employee_id', 'date_time_created')
