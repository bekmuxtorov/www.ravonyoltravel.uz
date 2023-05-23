from django.contrib import admin

from .models import Order


# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         'place', 'get_amout', 'is_payed', 'is_approved', 'user', 'customer_full_name', 'customer_phone_number')

#     list_filter = ('is_payed', 'is_approved')

#     list_editable = ('is_approved',)

#     search_fields = ('customer_full_name', 'customer_phone_number')

#     def get_amout(self, obj):
#         return obj.place.narxi

#     get_amout.short_description = 'Narxi'


# admin.site.register(Order, OrderAdmin)
