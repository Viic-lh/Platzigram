"""Post admin classes."""

# Django
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    
    list_display = ('user', 'title', 'photo')
    list_display_links = ('user', 'title')
    list_editable = ('photo',)

    search_fields = (
        'user__username',
        'title'
    )

    list_filter = ('modified',)

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'photo'),),
        }),
        ('Post', {
            'fields': (('title'),),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )    

    readonly_fields = ('created', 'modified')


