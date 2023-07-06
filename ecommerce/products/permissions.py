from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Product
from rest_framework import permissions

# Get the content type for the product model
product_content_type = ContentType.objects.get_for_model(Product)

# Get the permission for adding products
add_permission, _ = Permission.objects.get_or_create(
    content_type=product_content_type,
    codename="products.add_product",
)
# Get the permission for changing products
change_permission, _ = Permission.objects.get_or_create(
    content_type=product_content_type,
    codename="products.change_product",
)
# Get the permission for deleting products
delete_permission, _ = Permission.objects.get_or_create(
    content_type=product_content_type,
    codename="products.delete_product",
)


class IsGrantedOrReadOnlyProduct(permissions.BasePermission):
    """
    Custom permission to only allow admin users or users in "Product Editors" group to edit products.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users or users in "Product Editors" group.
        return request.user.is_authenticated and (
                request.user.is_admin
                or request.user.groups.filter(name="Product Editors").exists())
