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
    client_path = 'clientLogos/'
    cni = Client(clientName='Condé Nast International',
                         clientImagePath=client_path + 'CondeNast.jpg')
    cni.save()
    allen_and_overy = Client(clientName='allen_and_overy',
                             clientImagePath=client_path + 'AllenAndOvery.jpg')
    allen_and_overy.save()
    eshopworld = Client(clientName='eShopWorld', clientImagePath=client_path + 'eshopworld.jpg')
    eshopworld.save()
    granger = Client(clientName='Granger', clientImagePath=client_path + 'granger.jpg')
    granger.save()
    talk_talk = Client(clientName='TalkTalk', clientImagePath=client_path + 'TalkTalk.png')
    talk_talk.save()
    print('done!')

    print('Importing Projects...', end=' ')
    peerpoint = Project(client=allen_and_overy, projectTitle='Peer Point',
                        projectDescription='Peer point is a legal app which is'
                        +'fun and good, blah blah blah, blah')
    peerpoint.save()
    vogue_app = Project(client=cni, projectTitle='Front Row (Fashion Show CMS)',
                         projectDescription='vogue'+
                         'Initially the application managed content for the US Vogue fashion shows, now the current application manages content  for all markets. For Global markets, Global content editors are able to manage central data, schedule new fashion shows and much more. Local market editors can add localised content, add reviews, hide fashion shows and promote content. Throughout the fashion season the solution maintained a 100% uptime.That this site is not just static - the content is constantly up to date with the very latest fashion show content: “From the catwalk to being live on our fashion shows experience within mere moments, when the hype is at its greatest and user interest is at its peak”')
    
    vogue_app.save()
    un_app = Project(client=eshopworld, projectTitle='UN Payment Site',
                     projectDescription='A personalised storefront for customers who have registered'+
                     'an interest for a new model of watch'+
                     'Accepts a deposit to guarantee the customer recieves the watch as soon as its avilable'+
                     'for shipping')
    un_app.save()
    
    clipper_quay = Project(client=granger, projectTitle='Clipper Quay',
                        projectDescription='The aim was to deliver a new marketing site for Grainger’s flagship development, Clipper Quay.'+ 
                           'To also deliver an entirely digital leasing journey for new tenants, from requesting an apartment through to referencing and acceptance.')
    clipper_quay.save()
    
    digi_repair = Project(client=talk_talk, projectTitle='Digital Repair',
                          projectDescription='this project is a talk talk'+
                         ' project here is some text about this talk talk'+
                         ' project')
    digi_repair.save()
    print('done!')

    print('Importing ANDis...', end=' ')
    andi_photos='andis/'
    sam_c = Andi(andiName='Sam Clewlow',andiPhotoPath=andi_photos+'SamClewlow.png')
    sam_c.save()
    James_g = Andi(andiName='James Grant',andiPhotoPath=andi_photos+'JamesGrant.png')
    james_g.save()
    dami_o = Andi(andiName='Dami Olufemi',andiPhotoPath=andi_photos+'DamiOlufemi.png')
    dami_o.save()
    chris_m = Andi(andiName='Chris Mason',andiPhotoPath=andi_photos+'ChrisMason.png')
    chris_m.save()
    ola_a = Andi(andiName='Ola Abolarinwa',andiPhotoPath=andi_photos+'OlaAbolarinwa.png')
    ola_a.save()
    
    christian = Andi(andiName='Christian',andiPhotoPath=andi_photos+'ChristianChatteron.png')
    christian.save()
    james_b = Andi(andiName='James Beck',andiPhotoPath=andi_photos+'JamesBeck.png')
    james_b.save()
    james = Andi(andiName='James Tiffin', andiPhotoPath=andi_photos+'JamesTiffin.png')
    james.save()
    nate = Andi(andiName='Nate',andiPhotoPath=andi_photos+'Nate.png')
    nate.save()
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
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=james_g)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=dami_o)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=chris_m)
    
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james_b)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=nate)
    
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=phil)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=christian)
    
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=rapps)
    print('done!')

    print('Importing project images...', end=' ')
    proj_img = 'site_images/'
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
    tp = 'tech_images/'
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
