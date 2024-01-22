from django.db import models

# Create your models here.
class Adddoctor(models.Model):
    username=models.TextField(db_column='user',null=True)
    password=models.TextField(db_column='pass',null=True)
    doc_id=models.PositiveBigIntegerField(db_column='doc_id',null=True)
    age=models.PositiveIntegerField(db_column='age',null=True)
    image=models.ImageField(upload_to='images', db_column='image',null=True)
    gender=models.TextField(db_column='gen',null=True)
    number=models.PositiveBigIntegerField(db_column='number',null=True)
    class Meta:
        db_table="add_doctor"
    
    



