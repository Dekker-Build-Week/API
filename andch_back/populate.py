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

def import_clients():
    print('Importing clients... ', end=' ')
    client_path = 'andch_back_app/static/clientLogos/'
    cni = Client(clientName='Condé Nast International',
                         clientLogo=client_path)
    cni.save()
    allen_and_overy = Client(clientName='allen_and_overy',
                             clientLogo=client_path)
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
    un_app = Project(client=eshopworld projectTitle='UN Payment Site',
                     projectDescription='Text about this app, blahblahblahblah'+
                     'more text goes here')
    un_app.save()
    print('done!')

    print('Importing ANDis...', end=' ')
    sam_c = Andi(andiName='Sam C',andiPhotoPath='static/whatever')
    sam_c.save()
    christian = Andi(andiName='Christian',andiPhotoPath='static/whatever')
    christian.save()
    james = Andi(andiName='James',andiPhotoPath='static/whatever')
    james.save()
    james_b = Andi(andiName='James B',andiPhotoPath='static/whatever')
    james_b.save()
    phil = Andi(andiName='Phil',andiPhotoPath='static/whatever')
    phil.save()
    jerome = Andi(andiName='Jerome',andiPhotoPath='static/whatever')
    jerome.save()
    richard_apps = Andi(andiName='Richard Apps',andiPhotoPath='static/whatever')
    richard_apps.save()
    print('done!')

    print('Linking ANDis to projects...', end='')
    ProjectAndis.objects.get_or_create(project=cni, projectAndi=sam_c)
    ProjectAndis.objects.get_or_create(project=cni, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james_b)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=phil)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=christian)
    print('done!')

    print('adding project images...')

def main():
    #Set up environment

    import_clients()

if __name__ == '__main__':
    main()
