from django.contrib import admin
from .models import contact
# Register your models here.
admin.site.register(contact)

# class PostInline(admin.TabularInline):
#     model = Post
#     extra = 5
#     min_num = 3
#     max_num = 5
#     verbose_name = '이름'

# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'number', 'body')
#     search_fields = ('id', 'writer__username')
#     inlines = [PostInline]
    
#     actions = []
    
    