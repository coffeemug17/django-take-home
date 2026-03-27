from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category, Tag


def product_list(request):
    products = Product.objects.select_related('category').prefetch_related('tags')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')
    selected_tags = request.GET.getlist('tags')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if selected_category:
        products = products.filter(category__id=selected_category)

    for tag_id in selected_tags:
        products = products.filter(tags__id=tag_id)

    paginator = Paginator(products, 10)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'products': page,
        'paginator': paginator,
        'categories': categories,
        'tags': tags,
        'query': query,
        'selected_category': selected_category,
        'selected_tags': selected_tags,
    }

    return render(request, 'products/product_list.html', context)