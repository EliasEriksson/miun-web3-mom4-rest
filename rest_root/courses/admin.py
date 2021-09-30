from django.contrib import admin
from .models import Course

"""
adds the Course model to the django admin panel (https://web3mom5.eliaseriksson.eu/admin/)
so courses can be added via the admin panel if needed.
"""
admin.site.register(Course)
