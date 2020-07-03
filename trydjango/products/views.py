from django.http import Http404 # one way to handle exception
from django.shortcuts import render, redirect, get_object_or_404 # another way to handle get exception
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def render_initial_data(request):
    # initial_data = {
    #     'title': "this is my awesome title"
    # }
    obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, initial=initial_data) # to set something initially
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# using Pure Django Form
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':    
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now my form is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, 'products/product_create.html', context)

# create view for raw html
# def product_create_view(request):
#     # print(request.GET['title'])
#     # print(request.POST)
#     if request.method == "POST":
#         title = request.POST.get('title')
#         Product.objects.create(title= title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

# create view using non-pure django form
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # to re-render so that form becomes empty after submit
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)