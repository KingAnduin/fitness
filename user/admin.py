from django.contrib import admin
from user.models import UserInfo, UserAccount, UserToken


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_account','nickname','sex','birthday','head_image','contact_phone')


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('phone', 'password')


class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user_account','token')


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserToken)
