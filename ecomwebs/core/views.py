from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .models import Item, Itemlast, Itemforu, Join, Login, OrderItem, Order
from .forms import JoinIn, LogIn, CheckOut
from django.utils import timezone
from django.contrib.auth import authenticate
# Create your views here.

# cap nhat san pham len website thong qua site admin
class index(View):
	def get(self, request):
		context = {'items': Item.objects.all(), 'itemslast': Itemlast.objects.all(), 'itemsforu': Itemforu.objects.all() }
		return render(request, 'homepage/index.html', context)


# form dang ky
class join_in(View):
	def get(self, request):
		j = JoinIn
		jin = {'ji': j}
		return render(request, 'signup/index.html', jin)


	def post(self, request):
		if request.method == "POST":
			tj = JoinIn(request.POST)
			if tj.is_valid():
				tj.save()
				return HttpResponse('<h2 style="color: red; text-align: center;">BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG</h2>')



# form dang nhap
class log_in(View):
	def get(self, request):
		l = LogIn
		return render(request, 'signin/signin.html')



	def post(self, request):
		if request.method == "POST":
			tl = LogIn(request.POST)
			if tl.is_valid():
				signinname = tl.cleaned_data.get('username')
				signinpass = tl.cleaned_data.get('password')
				my_user = authenticate(username=signinname, password=signinpass)
				return redirect('homepage/index.html')
				 
					#return HttpResponse('<h2 style="color: red; text-align: center;">CHÀO MỪNG BẠN TRỞ LẠI %s!</h2>' %(signinname))
			

		if my_user is None:
			return HttpResponse('USER KHÔNG TỒN TẠI!')


# tao trang detailview cho san pham (dung chinh xac sp)

class detail_product(DetailView):
	'''def get(self, request):
		return render(request, 'product/product-detail.html/')'''
	model = Item
	template_name = 'product/product-detail.html'


class detail_productlast(DetailView):
	model = Itemlast
	template_name = 'product/product-detail.html'


class detail_productforu(DetailView):
	model = Itemforu
	template_name = 'product/product-detail.html'
 

# thong tin don hang
class order_summary_view(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
			context = {'object': order}
			return render(self.request, 'ordersummary/order-summary.html', context)
		except ObjectDoesNotExist:
			return redirect('/')
		




# them san pham vao gio hang
def add_to_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_item, created	 = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False) 
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.items.filter(item__slug=item.slug).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item quantity was updated!")
			return redirect('core:detail-product', slug=slug)
		else:
			order.items.add(order_item)
			messages.info(request, "This item was added to your cart!")
			return redirect('core:detail-product', slug=slug)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart!")
	return redirect('core:detail-product', slug=slug)


# bot san pham ra khoi gio hang
def remove_from_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_qs = Order.objects.filter(user=request.user, ordered=False) 
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.items.filter(item__slug=item.slug).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			order_item.save()	
			order.items.remove(order_item)
			messages.info(request, "This item was removed from your cart!")
			return redirect('core:order-summary')
		else:
			messages.info(request, "This item was not in your cart!")
			return redirect('core:detail-product', slug=slug)
	else:
		messages.info(request, "You do not have an active order!")
		return redirect('core:detail-product', slug=slug)	
	



# bot san pham ra khoi gio hang tai trang thong tin don hang
def remove_single_item_from_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_qs = Order.objects.filter(user=request.user, ordered=False) 
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.items.filter(item__slug=item.slug).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order.items.remove(order_item)
			messages.info(request, "This item was removed from your cart!")
			return redirect('core:order-summary')
		else:
			messages.info(request, "This item was not in your cart!")
			return redirect('core:order-summary', slug=slug)
	else:
		messages.info(request, "You do not have an active order!")
		return redirect('core:order-summary', slug=slug)		
			


# trang checkout thanh toan 
class check_out(View):
	def get(self, request):
		c = CheckOut
		check = {'co': c}
		return render(request, 'homepage/checkout.html', check)

	def post(self, requeste):
		if request.method == "POST":
			tp = CheckOut(request.POST)
			if tp.is_valid():
				street_address = tp.cleaned_data.get('street_address')
				apartment_address = tp.cleaned_data.get('apartment_address')
				country = tp.cleaned_data.get('country')
				zip = tp.cleaned_data.get('zip')
				telephone = tp.cleaned_data.get('telephone')
				same_billing_address = tp.cleaned_data.get('same_billing_address')
				save_info = tp.cleaned_data.get('save_info')
				payment_option = tp.cleaned_data.get('payment_option')
				content = {'st': street_address, 'ap': apartment_address, 'co': country, 'zi': zip, 'te': telephone}
				