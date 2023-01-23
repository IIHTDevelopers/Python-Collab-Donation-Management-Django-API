from django.db import models

class NGOModel(models.Model):
    ngo_id=models.AutoField(primary_key=True)
    ngo_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    phone_number=models.IntegerField()
    started_in=models.DateField()
    documents=models.CharField(max_length=100)

class DonorModel(models.Model):
    donar_id=models.AutoField(primary_key=True)
    ngo_id=models.IntegerField()
    donar_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    address=models.TextField(max_length=100)
    def __str__(self):
        return str(self.donar_id)

class DonationModel(models.Model):
    donation_id=models.AutoField(primary_key=True)
    donar_id=models.IntegerField()
    #donar_id=models.ForeignKey(DonorModel,on_delete=models.CASCADE)
    ngo_id=models.IntegerField()
    donation_type=models.CharField(max_length=100)
    amount=models.DecimalField(decimal_places=2,max_digits=100)
    donation_date=models.DateField()

class DonationRequestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    amount=models.DecimalField(decimal_places=2,max_digits=100)
    donar_id=models.IntegerField()
    ngo_id=models.IntegerField()
    donation_end_date=models.DateField()
