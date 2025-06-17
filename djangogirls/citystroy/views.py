from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home_view(request):
    promotions = Product.objects.filter(is_promotion=True)[:4]
    regular_products = Product.objects.filter(is_promotion=False)[:8]
    return render(request, 'home.html', {
        'promotions': promotions,
        'products': regular_products,
    })


@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'Товар "{product.name}" добавлен в корзину.')
    return redirect('home')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # или на другую страницу
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def catalog_view(request):
    # Получение параметров фильтрации из запроса
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 100000)

    try:
        min_price = float(min_price)
        max_price = float(max_price)
    except ValueError:
        min_price = 0
        max_price = 10000

    # Фильтрация товаров по цене
    products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

    # Пагинация: 18 товаров на страницу
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'min_price': int(min_price),
        'max_price': int(max_price),
    }
    return render(request, 'catalog.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Получаем любые 4 другие товара, кроме текущего
    related_products = Product.objects.exclude(pk=product.pk)[:4]

    return render(request, 'product_detail.html', {
        'product': product,
        'products': related_products,  # используем тот же ключ, что в шаблоне
    })