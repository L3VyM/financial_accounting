from django.db import models

# Create your models here.

# Account Equation variables i.e ASSETS, LIABILITIES, OWNERS EQUITY
class Acceqtn(models.Model):
	eqtn = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return f"{self.eqtn}"

# Currency Model
class Ccy(models.Model):
	ccy_code = models.CharField(max_length=3, primary_key=True)
	ccy_desc = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.ccy_code}"

# Account Model
class Account(models.Model):
	eqtn = models.ForeignKey('Acceqtn', on_delete=models.CASCADE)
	acc_desc = models.CharField(max_length=50, unique=True, primary_key=True)
	ccy_code = models.ForeignKey('Ccy', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.acc_desc}"


class Journal(models.Model):
	acc_desc_dr = models.ForeignKey('Account', verbose_name="Account Dr", related_name="Dr", on_delete=models.CASCADE)
	acc_desc_cr = models.ForeignKey('Account', verbose_name="Account Cr", related_name="Cr", on_delete=models.CASCADE)
	ccy_code = models.ForeignKey('Ccy', on_delete=models.CASCADE)
	amount_dr = models.IntegerField()
	amount_cr = models.IntegerField()
	# cre_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.acc_desc_cr}"




