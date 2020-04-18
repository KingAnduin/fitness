from django.contrib import admin
from news.models import NewsInfo


class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_type','news_level','news_major_muscle','news_other_muscle','news_equipment','news_gif','news_image','news_url')


admin.site.register(NewsInfo, NewsInfoAdmin)
