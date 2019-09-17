import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from andch_back_app.models import Client, Project, Andi, ProjectAndis, ProjectImages

# Create your views here.

def all_clients(request):
    clients = Client.objects.all()
    clientList = []
    for client in clients:
        clientList.append({'clientName': client.clientName, 'imagePath': client.clientImagePath},)
    data = {'clients' : clientList}

    return JsonResponse(data)

def all_projects(request):
    projects = Project.objects.all()
    all_projects =[]

    if projects:
        for project in projects:
            andis = []
            imagePaths = []
            andi_list = ProjectAndis.objects.filter(project=project)
            project_images_list = ProjectImages.objects.filter(project=project)
            for andi in andi_list:
                andis.append({'ANDiName': andi.projectAndi.andiName, 'ANDiPhoto': andi.projectAndi.andiPhotoPath})
            for image in project_images_list:
                imagePaths.append(image.projectImagePath)
            all_projects.append(
                {
                    'projectTitle': project.projectTitle,
                    'clientName': project.client.clientName,
                    'clientLogo': project.client.clientImagePath,
                    'projectDescription': project.projectDescription,
                    'team': andis,
                    'images': imagePaths,
                }
            )

    projectList = {'projects': all_projects}
    return HttpResponse(json.dumps(projectList), content_type="application/json")