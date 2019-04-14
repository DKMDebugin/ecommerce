import random
import string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """Random String Generator"""
    return ''.join(random.choice(chars) for _ in range(size))

def uinque_order_id_generator(instance):
    """Generate unique order id for Order models"""
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return uinque_order_id_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """Generate new slug if current slug already exists"""
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{random_string_generator(size=4)}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
