from django.contrib import admin
from andch_back_app.models import Client, Andi, Project, ProjectAndis, ProjectImages, ProjectTechnologyStacks

# Register your models here.

admin.site.register(Client)
admin.site.register(Andi)
admin.site.register(Project)
admin.site.register(ProjectAndis)
admin.site.register(ProjectImages)
admin.site.register(ProjectTechnologyStacks)