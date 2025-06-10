# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

from django.contrib import admin
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
