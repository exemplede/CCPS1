from django.contrib import admin
from .models import User, SiteVisit, Article
# Register your models here.
admin.site.register(
    [
        User,
        SiteVisit,
        Article
    ]
)