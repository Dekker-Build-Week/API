from django.contrib import admin
from andch_back_app.models import Client, Andi, Project, ProjectAndis, ProjectImages, ProjectTechnologyStacks

# Register your models here.

admin.site.register(Client)
admin.site.register(Andi)

admin.site.site_header = "ANDchievements Admin"
admin.site.site_title = "ANDchievements Admin Portal"
admin.site.index_title = "Welcome to the ANDchievements Admin Portal"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['projectTitle', 'client']
    ordering = ['projectTitle']
    list_filter = ['client']

# Register the admin class with the associated model
admin.site.register(Project, ProjectAdmin)

class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ['project', 'projectImagePath']
    list_filter = ['project']

admin.site.register(ProjectImages, ProjectImagesAdmin)

class ProjectAndisAdmin(admin.ModelAdmin):
    list_display = ['projectAndi', 'project']
    list_filter = ['project']
    ordering = ['projectAndi']

admin.site.register(ProjectAndis, ProjectAndisAdmin)

class ProjectTechnologyStacksAdmin(admin.ModelAdmin):
    list_display = ['technologyName', 'project', 'important']
    list_filter = ['project', 'important']
    ordering = ['technologyName']

admin.site.register(ProjectTechnologyStacks, ProjectTechnologyStacksAdmin)