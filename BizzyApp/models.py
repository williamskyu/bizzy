from django.db import models

class DiscountData(models.Model):
    #email = models.CharField(max_length = 50)
    #currency = models.CharField(max_length = 3)
    couponType = models.CharField(max_length = 1)
    couponVal = models.DecimalField(decimal_places = 2, max_digits = 10)
    minimumAmt = models.DecimalField(decimal_places = 2, max_digits = 10)
    couponCode = models.CharField(max_length = 8, null = True)
    #actDate = models.DateField()
    #expDate = models.DateField()
    #limit = models.IntegerField()

    def __str__(self):
        return self.couponCode
