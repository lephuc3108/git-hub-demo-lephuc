from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django_countries.fields import CountryField

# Create your models here.


class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	slug = models.SlugField(default='item')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('core:detail-product', kwargs={
			'slug': self.slug
		})

	def get_add_to_cart_url(self):
		return reverse('core:add-to-cart', kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse('core:remove-from-cart', kwargs={
			'slug': self.slug
		})

class Itemlast(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	slug = models.SlugField(default='item')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('core:detail-productlast', kwargs={
			'slug': self.slug
		})



class Itemforu(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	slug = models.SlugField(default='item')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('core:detail-productforu', kwargs={
			'slug': self.slug
		})

# item

class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False) 
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	
	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

	def get_total_item_price(self):
		return self.quantity * self.item.price


	def get_total_item_discount_price(self):
		return self.quantity * self.item.discount_price


	def get_amount_saved(self):
		return self.get_total_item_price - self.get_total_item_discount_price

	def get_final_price(self):
		if self.item.discount_price:
			return self.get_total_item_discount_price()
		return self.get_total_item_price()


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_final_price()
		return total


# from dang ky
class Join(models.Model):
	username = models.CharField(max_length=155)
	password = models.CharField(max_length=100)
	password_again = models.CharField(max_length=100)

	def __str__(self):
		return self.username

#form dang nhap
class Login(models.Model):
	username = models.CharField(max_length=155)
	password = models.CharField(max_length=100)
	remember = models.BooleanField()

	def __str__(self):
		return self.username


