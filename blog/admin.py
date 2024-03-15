from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ['title', 'created_at', 'updated_at']
    
