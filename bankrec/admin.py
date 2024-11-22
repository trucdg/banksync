from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(BusinessActivity)
admin.site.register(Category)
admin.site.register(BusinessActivityLink)
admin.site.register(BusinessCategory)
admin.site.register(TransactionEntry)
