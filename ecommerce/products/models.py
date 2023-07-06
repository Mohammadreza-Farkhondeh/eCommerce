from django.db import models
from .managers import ProductManager
from autoslug import AutoSlugField
from django.utils.crypto import get_random_string

def product_directory_path(instance, filename):
    # Images will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return f'product-{instance.profile.id}/{filename}'
def product_directory_path_head(instance, filename):
    # Head image will be uploaded to MEDIA_ROOT/product_<id>/head-<filename>
    return f'product-{instance.profile.id}/head-{filename}'
def get_slug(instance):
    # if the category has a parent, prepend the parent name
    if instance.parent:
        return f"{instance.parent.name} - {instance.name}"
    # otherwise, return only the name
    else:
        return instance.name


class Category(models.Model):
    """
    Category model for product category
    can be and have parent category
    """

    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=get_slug,
                        unique=True, unique_with="parent", always_update=True, null=True)

    # TODO: replace models.ForeignKey with mptt.TreeForeignKey to have more flexibility
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model
    each may have category or not
    two fields Image and Images, Image for list page and Images for detail page
    """
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=32, unique=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=product_directory_path_head)

    def save(self, *args, **kwargs):
        if not self.slug:  # if the slug is not set
            self.slug = get_random_string(8, '0123456789')  # generate a random slug of 8 digits
        super().save(*args, **kwargs)  # call the save method of the parent class

    # TODO: replace with ckeditor.fields.RichTextField
    description = models.TextField()
    images = models.ImageField(upload_to=product_directory_path)

    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    objects = ProductManager()
