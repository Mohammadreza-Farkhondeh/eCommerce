from django.contrib.auth.models import Group
from .permissions import add_permission, change_permission, delete_permission

# Create a new group called "Product Editors"
product_editors = Group.objects.create(name="Product Editors")

# Assign the permissions to the group
product_editors.permissions.add(add_permission, change_permission, delete_permission)
