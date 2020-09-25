from django.contrib import admin

# Register your models here.
from order.models import OrderDetail, Order, ShopCart



class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

class DetailInline(admin.TabularInline):
    model = OrderDetail



class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'shipname', 'shipphone', 'total','status')
    list_filter = ('status', 'create_at')
    readonly_fields = ('shipname', 'shipphone', 'shipaddress', 'total','user')
    #inlines = [DetailInline]
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'total', 'update_at')
    readonly_fields = ('product', 'quantity', 'price', 'total')




admin.site.register(Order, OrderAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)