from django.contrib import admin
from User.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated_at')
    search_fields = ('text__startswith', 'user__username__startswith')

    list_filter = [('user')]

    fieldsets = (
        ('Post Details', {'fields': ('user', 'text')}),
        ('Important Dates', {'fields':('created_at', 'updated_at')}),
        
    )

    readonly_fields = ['created_at', 'updated_at']
