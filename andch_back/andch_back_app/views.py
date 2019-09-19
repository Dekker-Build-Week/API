import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from andch_back_app.models import Client, Project, Andi, ProjectAndis, ProjectImages, ProjectTechnologyStacks, ProjectVideos

# Create your views here.

def all_projects(request):
    serverURL = request.META.get('HTTP_HOST', '127.0.0.1:8000')
    
    projects = Project.objects.all()
    all_projects =[]

    if projects:
        for project in projects:
            andis = []
            imagePaths = []
            techStacks = []
            andi_list = ProjectAndis.objects.filter(project=project)
            project_images_list = ProjectImages.objects.filter(project=project)
            project_stack_list = ProjectTechnologyStacks.objects.filter(project=project)
            
            for andi in andi_list:
                andis.append({'ANDiName': andi.projectAndi.andiName, 'ANDiPhoto': serverURL + andi.projectAndi.andiPhotoPath.url})
            for image in project_images_list:
                imagePaths.append({'source': serverURL + image.projectImagePath.url, 'position':image.position})
            for tech in project_stack_list:
                techStacks.append({'name': tech.technologyName, 'image': serverURL + tech.technologyImagePath.url, 'important': tech.important})
            
            videoURL = ''
            if ProjectVideos.objects.filter(project=project).exists():
                videoURL = serverURL + ProjectVideos.objects.filter(project=project).first().projectVideoPath.url
            
            all_projects.append(
                {
                    'projectTitle': project.projectTitle,
                    'clientName': project.client.clientName,
                    'clientLogo': serverURL + project.client.clientImagePath.url,
                    'projectDescription': project.projectDescription,
                    'team': andis,
                    'techStack': techStacks,
                    'images': imagePaths,
                    'video': videoURL,
                }
            )

    projectList = {'projects': all_projects}
    return HttpResponse(json.dumps(projectList), content_type="application/json")