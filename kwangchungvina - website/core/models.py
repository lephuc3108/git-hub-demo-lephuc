from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

PRODUCT_CATEGORY = (('chung', 'CHUNG'),
					('inox tấm', 'INOX TẤM'),
					('inox cuộn', 'INOX CUỘN'),
	)

AVAILABILITY = (('còn hàng', 'CÒN HÀNG'),
				('tạm hết hàng', 'TẠM HẾT HÀNG'),

	)

# tao danh sach san pham
class Categories(models.Model):
	cat_title = models.CharField(max_length=355)

	def __str__(self):
		return self.cat_title



#bang csdl chua cac san pham
class Item(models.Model):
	title = models.CharField(max_length=355)
	img = models.ImageField(upload_to='images', blank=True, null=True)
	price = models.FloatField(blank=True, null=True)
	discount_price = models.FloatField(blank=True, null=True)
	available = models.CharField(max_length=355, choices=AVAILABILITY, default='còn hàng')
	categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	category = models.CharField(max_length=355, choices=PRODUCT_CATEGORY, default='chung')
	description = RichTextUploadingField(null=True, blank=True)
	slug = models.SlugField(default='sp')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('core:single-product', kwargs={
			'slug':self.slug
			})


#bang csdl chua cac sp duoc dat hang
class OrderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)


#bang csdl chua cac gio hang cua nguoi dung
class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username





#bang csdl trang blog_post
class Blogpost(models.Model):
	title = models.CharField(max_length=355)
	img = models.ImageField(upload_to='posts')
	description = models.CharField(max_length=555)
	content = RichTextUploadingField()
	start_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(default='post')

	def __str__(self):
		return self.title


	def get_single_blog_url(self):
		return reverse('core:blog-single', kwargs={
			'slug': self.slug
			})