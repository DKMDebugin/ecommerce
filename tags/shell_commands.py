Last login: Tue Mar 26 15:40:23 on ttys002
[~]$ cd repos/eCommerce/
[eCommerce (master)]$ source ec_env/bin/activate
(ec_env) [eCommerce (master)]$ python manage.py shell
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: T-shirt>, <Tag: T-shirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Shoe>, <Tag: Boot>, <Tag: Sneakers>]>
>>> tag = Tag.objects.first()
>>> tag
<Tag: T-shirt>
>>> tag.title
'T-shirt'
>>> tag.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x105970240>
>>> tag.products.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ManyRelatedManager' object has no attribute 'objects'
>>> tag.products.all()
<ProductQuerySet [<Product: Summer T-Shrit>]>
>>> tag.products.all().first()
<Product: Summer T-Shrit>
>>> exit()
(ec_env) [eCommerce (master)]$ python manage.py shell
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> Product.objects.all()
<ProductQuerySet [<Product: Shirt>, <Product: Summer Short>, <Product: Summer T-Shrit>, <Product: trouser>, <Product: blue jean>, <Product: Female blue jean>, <Product: smiley tshirt>, <Product: grey shirt>, <Product: black timberland>, <Product: Green timberland>, <Product: Air force 1>]>
>>> product = Product.objects.first()
>>> product
<Product: Shirt>
>>> product.title
'Shirt'
>>> product.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tag'
>>> product.tags
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tags'
>>> product.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x105865240>
>>> product.tag_set.all()
<QuerySet []>
>>> product.tag_set.first()
>>> exit()
(ec_env
