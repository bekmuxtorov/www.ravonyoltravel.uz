from django.contrib import admin
from .models import Travel, Tassurotlar, Rasmlar, Fikrlar, Transport, Order

# Register your models here.
admin.site.register(Travel)
admin.site.register(Tassurotlar)
admin.site.register(Rasmlar)
admin.site.register(Fikrlar)
admin.site.register(Transport)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_payed', 'amount', 'customer_phone_number', 'where_from', 'where_to')


admin.site.register(Order, OrderAdmin)

