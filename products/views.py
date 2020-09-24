from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from analytics.mixins import ObjectViewedMixin
from carts.models import Cart
from .models import Product

# Create your views here.
class ProductFeaturedListView(ListView):
    """Product Featured List View"""
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return  Product.objects.all().featured()

class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
    """Product Featured Detail View"""
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return  Product.objects.featured()

class ProductListView(ListView):
    """Product List View"""
    # queryset = Product.objects.all()
    template_name = 'products/list.html'
    def get_context_data(self, *args, **kwargs):
        """Add context data"""
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return  Product.objects.all()

def product_list_view(request):
    instance    = Product.objects.all()
    context     = {
        'object_list': instance,
    }
    template    = 'products/list.html'
    return render(request, template, context)

class ProductDetailSlugView(ObjectViewedMixin, DetailView):
    """Product Detail View"""
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        """Add context data"""
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug = slug, active = True)
        # print(instance)
        try:
            instance = Product.objects.filter(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found....')
        except Product.MultipleObjectsReturned:
            instance = Product.objects.filter(slug=slug, active=True)
        except:
            raise Http404('uhmmmm')
        return instance.first()

class ProductDetailView(ObjectViewedMixin, DetailView):
    """Product Detail View"""
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)

        if instance is None:
            raise Http404('Product Doest Exist')
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(id=pk)

def product_detail_view(request, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=kwargs['pk'])
    # try:
    #     instance = Product.objects.get(pk=kwargs['pk'])
    # except Product.DoesNotExist:
    #     print('no products here')
    #     raise Http404('Product Doest Exist')
    # except:
    #     print('huh?')

    instance = Product.objects.get_by_id(kwargs['pk'])
    print(instance)
    if instance == None:
        raise Http404('Product Doest Exist')

    # qs = Product.objects.filter(id=kwargs['pk'])
    #
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404('Product Doest Exist or More than one')

    context = {
        'object': instance,
    }
    template = 'products/detail.html'
    return render(request, template, context)
