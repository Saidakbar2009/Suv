from django.db import models

# Create your models here.
class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    litr = models.PositiveSmallIntegerField()
    batafsil = models.TextField()

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.PositiveSmallIntegerField()
    manzil = models.CharField()
    qarz = models.CharField()
    user = models.CharField()

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqti = models.PositiveSmallIntegerField()
    user = models.CharField()

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.PositiveSmallIntegerField()
    kiritilgan_sana = models.DateField()

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narx = models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

 