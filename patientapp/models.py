from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.TextField(db_column='name',null=True)
    email=models.TextField(db_column='email',null=True)
    number=models.PositiveBigIntegerField(db_column='number',null=True)
    password=models.TextField(db_column='password',null=True)
    class Meta:
        db_table='patient_registration'
class Booking(models.Model):
    name=models.TextField(db_column='name',null=True)
    number=models.PositiveBigIntegerField(db_column='mob',null=True)
    time=models.TimeField(db_column='time',null=True)
    address=models.TextField(db_column='address',null=True,max_length=500)
    location=models.TextField(db_column='location',null=True)
    specialist=models.TextField(db_column='speciallist',null=True)
    doctors=models.TextField(db_column='doc',null=True)
    msg=models.TextField(db_column='message',null=True)
    status=models.TextField(db_column='status',null=True)
    class Meta:
        db_table='general_booking'
class Contact(models.Model):
    name=models.TextField(db_column='name',null=True)
    email=models.TextField(db_column='email',null=True)
    msg=models.TextField(db_column='msg',null=True)
    class Meta:
        db_table='patient_contact'
    




    