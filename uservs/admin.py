from django.contrib import admin

from .models import Uservs

# Register your models here.
class UservsAdmin(admin.ModelAdmin):
  list_display = ('id', 'prenom', 'email', 'feedback', 'date_inscription', 'date_feedback')
  list_display_links = ('id', 'prenom')
  search_fields = ('id','prenom', 'email')
  list_per_page = 25

admin.site.register(Uservs, UservsAdmin)
