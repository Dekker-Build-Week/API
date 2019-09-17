#!/usr/bin/env python3
## populate.py
##
## script to populate django's models with dummy data

## run script with:      python populate.py to run
## If data is corrupted, then first use:     python manage.py flush

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andch_back.settings')
django.setup()

from andch_back_app.models import Client, Project, Andi, ProjectAndis
from andch_back_app.models import ProjectImages, ProjectTechnologyStacks

def import_clients():
    print('Importing clients... ', end=' ')
    client_path = 'andch_back_app/static/clientLogos/'
    cni = Client(clientName='Condé Nast International',
                         clientImagePath=client_path)
    cni.save()
    allen_and_overy = Client(clientName='allen_and_overy',
                             clientImagePath=client_path)
    allen_and_overy.save()
    eshopworld = Client(clientName='eShopWorld', clientImagePath=client_path)
    eshopworld.save()
    talk_talk = Client(clientName='TalkTalk', clientImagePath=client_path)
    talk_talk.save()
    print('done!')

    print('Importing Projects...', end=' ')
    peerpoint = Project(client=allen_and_overy, projectTitle='Peer Point',
                        projectDescription='Peer point is a legal app which is'
                        +'fun and good, blah blah blah, blah')
    peerpoint.save()
    vogue_app = Project(client=cni, projectTitle='Vogue Runway App',
                         projectDescription='vogue'+
                         'project AND made for cni?? I hope it was good')
    vogue_app.save()
    un_app = Project(client=eshopworld, projectTitle='UN Payment Site',
                     projectDescription='Text about this app, blahblahblahblah'+
                     'more text goes here')
    un_app.save()
    digi_repair = Project(client=talk_talk, projectTitle='Digital Repair',
                          projectDescription='this project is a talk talk'+
                         ' project here is some text about this talk talk'+
                         ' project')
    digi_repair.save()
    print('done!')

    print('Importing ANDis...', end=' ')
    andi_photos='andch_back_app/static/andis/'
    sam_c = Andi(andiName='Sam Clewlow',andiPhotoPath=andi_photos+'SamClewlow.png')
    sam_c.save()
    christian = Andi(andiName='Christian',andiPhotoPath=andi_photos+'ChristianChatteron.png')
    christian.save()
    james_b = Andi(andiName='James Beck',andiPhotoPath=andi_photos+'JamesBeck.png')
    james_b.save()
    james = Andi(andiName='James Tiffin', andiPhotoPath=andi_photos+'JamesTiffin.png')
    james.save()
    phil = Andi(andiName='Phil',andiPhotoPath=andi_photos+'PhilSmith.png')
    phil.save()
    jerome = Andi(andiName='Jerome', andiPhotoPath=andi_photos+'JeromeTosoni.png')
    jerome.save()
    rapps = Andi(andiName='Richard Apps',
                        andiPhotoPath=andi_photos+'RichardApps.png')
    rapps.save()
    print('done!')

    print('Linking ANDis to projects...', end=' ')
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=sam_c)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james_b)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=phil)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=christian)
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=rapps)
    print('done!')

    print('Importing project images...', end=' ')
    proj_img = 'andch_back_app/static/site_images/'
    ProjectImages.objects.get_or_create(position=0, project=vogue_app,
                                        projectImagePath=proj_img+'vogue1.jpeg')
    ProjectImages.objects.get_or_create(position=1, project=vogue_app,
                                        projectImagePath=proj_img+'vogue2.jpg')
    ProjectImages.objects.get_or_create(position=0, project=peerpoint,
                                        projectImagePath=proj_img+'peerpoint1.jpg')
    ProjectImages.objects.get_or_create(position=1, project=peerpoint,
                                        projectImagePath=proj_img+'peerpoint2.jpg')
    ProjectImages.objects.get_or_create(position=2, project=peerpoint,
                                        projectImagePath=proj_img+'peerpoint3.jpg')
    ProjectImages.objects.get_or_create(position=3, project=peerpoint,
                                        projectImagePath=proj_img+'peerpoint4.jpg')

    print('done!')
    tp = 'andch_back_app/static/tech_images'
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='Angular',
                                                  technologyImagePath=tp+'angular.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=un_app,
                                                  technologyName='Java',
                                                  technologyImagePath=tp+'java.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=vogue_app,
                                                  technologyName='Swift',
                                                  technologyImagePath=tp+'swift.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=peerpoint,
                                                  technologyName='Azure',
                                                  technologyImagePath=tp+'azure.jpg',
                                                  important=True)

def main():
    # Set up environment

    import_clients()

if __name__ == '__main__':
    main()
