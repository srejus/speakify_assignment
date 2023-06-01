from django.contrib import admin
from . models import UserProfile,Interest

# Admin customization
class InterestAdmin(admin.ModelAdmin):
    list_display = ['interest']
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Interest,InterestAdmin)