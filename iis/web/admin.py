from django.contrib import admin

# Register your models here.
from web.models import *

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
 
class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline 外键
    list_display=('name','email','age')
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
 
    )
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('user','pwd')

class UserListAdmin(admin.ModelAdmin):
    list_display=('username','age')
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserList, UserListAdmin)
admin.site.register(Test)