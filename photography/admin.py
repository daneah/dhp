from django.contrib import admin
from django import forms

from photography.models import Photograph, Album, Tag, Service

class PhotographAlbumInline(admin.TabularInline):
  model = Photograph.albums.through

class PhotographTagInline(admin.TabularInline):
  model = Photograph.tags.through

class PhotographAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Photograph Information', {'fields': ['title', 'image']}),
    ('Publishing', {'fields': ['public', 'published_date']}),
  ]
  inlines = [PhotographAlbumInline, PhotographTagInline]
  list_display = ('admin_thumbnail', 'title', 'size', 'orientation', 'published_date', 'public', 'user', 'uuid')
  date_hierarchy = 'published_date'
  search_fields = ['title']

  def save_model(self, request, obj, form, change):
    obj.user = request.user
    obj.save()

class AlbumAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Album Information', {'fields': ['title', 'sort_order']}),
    ('Publishing', {'fields': ['public', 'published_date']}),
  ]
  list_display = ('title', 'sort_order', 'photos', 'published_date', 'public', 'uuid')
  date_hierarcy = 'published_date'

class TagAdmin(admin.ModelAdmin):
  pass

class ServiceForm(forms.ModelForm):
  description = forms.CharField(widget=forms.Textarea)
  class Meta:
    model = Service

class ServiceAdmin(admin.ModelAdmin):
  form = ServiceForm

  def admin_price(self, obj):
    return '$' + str(obj.price)
  admin_price.admin_order_field = 'price'
  admin_price.short_description = 'Price'

  list_display = ('title', 'description', 'admin_price')

admin.site.register(Photograph, PhotographAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
