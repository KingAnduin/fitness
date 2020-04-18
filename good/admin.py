from django.contrib import admin
from good.models import Good, GoodType


class GoodAdmin(admin.ModelAdmin):
    list_display = ('good_number', 'good_name', 'good_image', 'good_content','good_location','good_type','good_owner')


admin.site.register(Good, GoodAdmin)
admin.site.register(GoodType)