from django.contrib import admin
from order.models import Order, OrderTimePeriod, OrderStatus


class OrderAdmin(admin.ModelAdmin):
    list_display = ('create_time','order_date','order_time_period','order_status','user_account','good_id')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderTimePeriod)
admin.site.register(OrderStatus)
