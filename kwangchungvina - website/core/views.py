from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Item, OrderItem, Order, Blogpost, Categories

# Create your views here.

'''class index(View):
	def get(self, request):
		mutual = Item.objects.filter(category__icontains='CHUNG')
		category = Categories.objects.all()
		context = {'mutuals': mutual}
		return render(request, 'homepage/index.html', context)'''


# trang home
class home(View):
	def get(self, request):
		mutual = Item.objects.filter(category__icontains='CHUNG')
		listcategory = Categories.objects.all()
		context = {'mutuals': mutual, 'listcategories': listcategory}
		return render(request, 'homepage/home.html', context)



# tao trang chi tiet sp co lien ket duong dan con theo tcsdl slug
class single_product(DetailView):
	model = Item
	template_name = 'homepage/product-page.html'



# tao trang bai viet (blog)
class blog_post(View):
	def get(self, request):
		blog = Blogpost.objects.all()
		bp = {'blogs': blog}
		return render(request, 'homepage/blog.html', bp)


# tao trang chi tiet bai viet (single blog)
class blog_single(DetailView):
	model = Blogpost
	template_name = 'homepage/blog_single.html'



# trang lien he
class contact_page(View):
	def get(self, request):
		return render(request, 'homepage/contact.html')


# trang lien he
class about_page(View):
	def get(self, request):
		return render(request, 'homepage/about.html')



def productcat(request, id):
	listcategory = Categories.objects.all()
	productcat = Item.objects.filter(categories_id= id)
	context = {'productcats': productcat, 'listcategories': listcategory}
	return render(request, 'homepage/products.html', context)



# tao phan backend search item
def search_item(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		searchitem = Item.objects.filter(title__icontains=q)
		listcategory = Categories.objects.all()
		si = {'searchitems': searchitem, 'listcategories': listcategory}
		template = 'homepage/search-item.html'
	else:
		si = {}
		template = 'homepage/search-item.html'
	return render(request, template, si)