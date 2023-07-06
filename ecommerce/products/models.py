from django.db import models


def product_directory_path(instance, filename):
    # Images will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return f'product-{instance.profile.id}/{filename}'
def product_directory_path_head(instance, filename):
    # Head image will be uploaded to MEDIA_ROOT/product_<id>/head-<filename>
    return f'product-{instance.profile.id}/head-{filename}'


class Category(models.Model):
    """
    Category model for products category
    can be and have parent category
    """
    name = models.CharField(max_length=50)

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

    # TODO: replace with ckeditor.fields.RichTextField
    description = models.TextField()
    images = models.ImageField(upload_to=product_directory_path)

    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True, blank=True)
