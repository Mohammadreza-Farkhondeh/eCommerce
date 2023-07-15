from django.contrib.auth.models import Group


try:
    from .permissions import add_permission, change_permission, delete_permission

    # Create a new group called "Product Editors"
    product_editors, _ = Group.objects.get_or_create(name="Product Editors")

    # Assign the permissions to the group
    product_editors.permissions.add(add_permission, change_permission, delete_permission)
except Exception as err:
    print(err)
