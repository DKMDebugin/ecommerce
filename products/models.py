from django.db import models
import os
from django.db.models.signals import pre_save, post_save
import random
from django.urls import reverse

from .utils import unique_slug_generator



def get_filename_ext(filepath):
    """Split file path into name & extension"""
    base_name   = os.path.basename(filepath)
    name, ext   = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    """Create New File Name"""
    new_filename    = random.randint(1, 3910209312)
    name, ext       = get_filename_ext(filename)
    final_filename  = f"{new_filename}{ext}"
    return f'products/{new_filename}/{final_filename}'


class ProductQuerySet(models.query.QuerySet):
    """Extend /Override Custom Querysets"""
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, )

class ProductManager(models.Manager):
    '''Extend /Override Product Custom Model Manager (objects)'''

    def get_queryset(self):
        """Add custom query set to Model Manager"""
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        """Override the all() Model Manager method"""
        return self.get_queryset().active()

    def features(self):
        """Add method method to Model Manager """
        return self.get_queryset().featured()

    def get_by_id(self, id):
        """Add method method to Model Manager """
        qs = self.get_queryset().filter(id=id, featured=False) # Product.objects is replaced by self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    """Product Model"""
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)


    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug':self.slug,})

    def __str__(self):
        return self.title


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    """Create slug value for every empty slug field"""
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)
