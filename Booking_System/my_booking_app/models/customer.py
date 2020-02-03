from django.db import models
#customer table
class Customer(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True)
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    Mobile = models.CharField(max_length=15)
    Password = models.CharField(max_length=50)

    class Meta:
        db_table = "customer"