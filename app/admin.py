from django.contrib import admin

from app.models import GeneralInfo

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display=[
        'company_name',
        'location',
        'email',
        'open_hours',
    ]

    # def has_add_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
    readonly_fields=['email']
    
    
