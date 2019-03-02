from django.contrib import admin

from .models import Artiste, Solex, Notification, Description

# Register your models here.
class ArtisteAdmin(admin.ModelAdmin):
  list_display = ('id', 'nom', 'pays', 'description', 'scene', 'jour', 'horaire_debut', 'horaire_fin', 'rs_link_1', 'rs_link_2','rs_link_3')
  list_display_links = ('id', 'nom')
  search_fields = ('id','nom', 'scene', 'jour')
  list_per_page = 25

admin.site.register(Artiste, ArtisteAdmin)

# Register your models here.
class SolexAdmin(admin.ModelAdmin):
  list_display = ('id', 'type', 'jour', 'heure_debut', 'heure_fin', 'description')
  list_display_links = ('id', 'type')

admin.site.register(Solex, SolexAdmin)

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
  list_display = ('id', 'titre', 'type', 'message', 'lien', 'date_pop')
  list_display_links = ('id', 'titre')
  search_fields = ('id','titre', 'type', 'message')
  list_per_page = 25

admin.site.register(Notification, NotificationAdmin)

# Register your models here.
class DescriptionAdmin(admin.ModelAdmin):
  list_display = ('id', 'sujet', 'page', 'message')
  list_display_links = ('id', 'sujet')
  search_fields = ('id','titre', 'page', 'message')
  list_per_page = 25

admin.site.register(Description, DescriptionAdmin)