1from django.db.models import Manager


class ProductManager(Manager):
    """
    Manager for implement by_category method
        in order to get all products in a category and its sub-categories at Category retrieve action
    """
    def by_category(self, category):
        # get the subcategories of the category
        subcategories = category.category_set.all()
        # create a list to store the category ids
        category_ids = [category.id]
        # loop through each subcategory
        for subcategory in subcategories:
            # append the subcategory id to the list
            category_ids.append(subcategory.id)
        # return a queryset of products that have any of the category ids
        return self.filter(category__id__in=category_ids)
