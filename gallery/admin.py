from gallery.models import Gallery, Comment
from django.contrib import admin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('image', 'image_thumb', 'user')
	inlines = [CommentInline]

admin.site.register(Gallery, GalleryAdmin)
