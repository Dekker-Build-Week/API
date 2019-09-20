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
from andch_back_app.models import ProjectVideos

def import_clients():
    print('Importing clients... ', end=' ')
    client_path = 'clientLogos/'
    cni = Client(clientName='Condé Nast International',
                         clientImagePath=client_path + 'CondeNast.jpg')
    cni.save()
    allen_and_overy = Client(clientName='Allen and Overy',
                             clientImagePath=client_path + 'AllenAndOvery.jpg')
    allen_and_overy.save()
    eshopworld = Client(clientName='eShopWorld', clientImagePath=client_path + 'eshopworld.jpg')
    eshopworld.save()
    #granger = Client(clientName='Granger', clientImagePath=client_path + 'granger.jpg')
    #granger.save()
    santander = Client(clientName='Santander', clientImagePath=client_path + 'santander.jpg')
    santander.save()
    talk_talk = Client(clientName='TalkTalk', clientImagePath=client_path + 'TalkTalk.png')
    talk_talk.save()
    print('done!')

    print('Importing Projects...', end=' ')
    peerpoint = Project(client=allen_and_overy, projectTitle='Peer Point',
                        projectDescription='Peer point allows Lawyers to talk to other Lawyers. Arrange meetings. Have lunch.'
                        +'  Discuss clients, discuss cases. Peerpoint is the intermediary between you and other lawyers. '
                        +'PeerPoint is the next generation in Lawyer contracting.')
    peerpoint.save()

    vogue_app = Project(client=cni, projectTitle='Fashion Shows',
                     projectDescription='Initially the application managed content for the US Vogue fashion shows, '+ 
                    'the launch of Fashion Shows, an extensive resource of '+
                    '12,000-plus collections, over 100 seasons, and more '+
                    'than 1 million runway looks. To coincide with the big '+
                    'debut, we’re introducing a new app that will appeal to '+
                    'the over-scheduled and the under-stimulated alike. Meet '+
                    'Fashion Shows, the app that provides style-minded ' +
                    'smartphone users with unlimited access to fashion shows '+
                    'from around the globe. Whenever. Wherever.')
    
    vogue_app.save()
    
    peerpoint = Project(client=allen_and_overy, projectTitle='Peer Point',
                        projectDescription='Peer point is a legal app which is'
                        +'fun and good, blah blah blah, blah')
    peerpoint.save()

    un_app = Project(client=eshopworld, projectTitle='UN Payment Site',
                     projectDescription='A personalised storefront for customers who have registered '+
                     'an interest for a new model of watch. '+
                     'Accepts a deposit to guarantee the customer recieves the watch as soon as its avilable '+
                     'for shipping')
    un_app.save()
    
    #clipper_quay = Project(client=granger, projectTitle='Clipper Quay',
                        #projectDescription='The aim was to deliver a new marketing site for Grainger’s flagship development, Clipper Quay.'+ 
                        #   'To also deliver an entirely digital leasing journey for new tenants, from requesting an apartment through to referencing and acceptance.')
    #clipper_quay.save()
    
    asto_io = Project(client=santander, projectTitle='Asto.io',
                          projectDescription='The aim was to create an app that gives back time to those leading and managing SMEs. '+
                      'Enable users to capture, tag and export receipts, aggregate all their banking / financial information, '+ 
                      'create invoices and access insights. Create a service, featured in the Asto app, '+ 
                      'that allows users to finance their invoices to fill their cash flow gaps.')
    asto_io.save()
    
    digi_repair = Project(client=talk_talk, projectTitle='Digital Repair',
                          projectDescription='TalkTalk Telecom Group plc (commonly known as NotTalk Coup, trading as TalkTalk) ' +
                          'is a company which provides pay television, telecommunications, Internet access, and mobile network services' +
                          ' to businesses and consumers in the United Kingdom. It was founded in 1853 as a subsidiary of Ferrari ' +
                          ' and was demerged as a standalone company in March 1895. Its headquarters are in London.' +
                            ' TalkTalks infrastructure has not been updated since 1870.')
    digi_repair.save()
    print('done!')

    print('Importing ANDis...', end=' ')
    andi_photos='andis/'
    sam_c = Andi(andiName='Sam Clewlow',andiPhotoPath=andi_photos+'SamClewlow.png')
    sam_c.save()
    eggy_b = Andi(andiName='Egdar Bune',andiPhotoPath=andi_photos+'easteregg.png')
    eggy_b.save()
    anna_lucking = Andi(andiName='Anna Lucking',andiPhotoPath=andi_photos+'AnnaLucking.png')
    anna_lucking.save()
    matt_rosenquist = Andi(andiName='Matt Rosenquist',andiPhotoPath=andi_photos+'MattRosenquist.png')
    matt_rosenquist.save()
    ola_olufemi = Andi(andiName='Ola Olufemi',andiPhotoPath=andi_photos+'OlaOlufemi.png')
    ola_olufemi.save()
    james_g = Andi(andiName='James Grant',andiPhotoPath=andi_photos+'JamesGrant.png')
    james_g.save()
    dami_o = Andi(andiName='Dami Olufemi',andiPhotoPath=andi_photos+'DamiOlufemi.png')
    dami_o.save()
    chris_m = Andi(andiName='Chris Mason',andiPhotoPath=andi_photos+'ChrisMason.png')
    chris_m.save()
    ola_a = Andi(andiName='Ola Abolarinwa',andiPhotoPath=andi_photos+'OlaAbolarinwa.png')
    ola_a.save()
    diana_d = Andi(andiName='Diana Donca',andiPhotoPath=andi_photos+'DianaDonca.png')
    diana_d.save()
    david_g = Andi(andiName='David Garvie',andiPhotoPath=andi_photos+'DavidGarvie.png')
    david_g.save()
    jemal_a = Andi(andiName='Jemal Ahmedov',andiPhotoPath=andi_photos+'JemalAhmedov.png')
    jemal_a.save()
    jabari_h = Andi(andiName='Jabari Holder',andiPhotoPath=andi_photos+'JabariHolder.png')
    jabari_h.save()
    sabah_p = Andi(andiName='Sabah Peter',andiPhotoPath=andi_photos+'SabahPeter.png')
    sabah_p.save()

    
    christian_c = Andi(andiName='Christian Chatterton',andiPhotoPath=andi_photos+'ChristianChatteron.png')
    christian_c.save()
    james_b = Andi(andiName='James Beck',andiPhotoPath=andi_photos+'JamesBeck.png')
    james_b.save()
    james = Andi(andiName='James Tiffin', andiPhotoPath=andi_photos+'JamesTiffin.png')
    james.save()
    nate = Andi(andiName='Nate',andiPhotoPath=andi_photos+'Nate.png')
    nate.save()
    phil = Andi(andiName='Phil Smith',andiPhotoPath=andi_photos+'PhilSmith.png')
    phil.save()
    jerome = Andi(andiName='Jerome Tosoni', andiPhotoPath=andi_photos+'JeromeTosoni.png')
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
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=david_g)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=james_g)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=dami_o)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=ola_a)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=anna_lucking)
    ProjectAndis.objects.get_or_create(project=vogue_app, projectAndi=matt_rosenquist)
    
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=james_b)
    ProjectAndis.objects.get_or_create(project=un_app, projectAndi=nate)
    
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=phil)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=christian_c)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=jemal_a)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=jabari_h)
    ProjectAndis.objects.get_or_create(project=peerpoint, projectAndi=sabah_p)



    
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=james)
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=rapps)
    ProjectAndis.objects.get_or_create(project=digi_repair, projectAndi=eggy_b)

    ProjectAndis.objects.get_or_create(project=asto_io, projectAndi=christian_c)
    ProjectAndis.objects.get_or_create(project=asto_io, projectAndi=david_g)
    ProjectAndis.objects.get_or_create(project=asto_io, projectAndi=chris_m)

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
    ProjectImages.objects.get_or_create(position=0, project=asto_io,
                                        projectImagePath=proj_img+'asto.jpg')
    ProjectImages.objects.get_or_create(position=1, project=asto_io,
                                        projectImagePath=proj_img+'asto1.jpg')
    ProjectImages.objects.get_or_create(position=2, project=asto_io,
                                        projectImagePath=proj_img+'asto2.jpg')
    ProjectImages.objects.get_or_create(position=0, project=un_app,
                                        projectImagePath=proj_img+'eshopworldun.jpg')
    #ProjectImages.objects.get_or_create(position=0, project=clipper_quay,
                                        #projectImagePath=proj_img+'grainger.jpg')
    ProjectImages.objects.get_or_create(position=0, project=digi_repair,
                                        projectImagePath=proj_img+'talktalkDigiRepair.jpg')

    print('done!')
    tp = 'tech_images/'
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='Angular',
                                                  technologyImagePath=tp+'angular.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='HTML5',
                                                  technologyImagePath=tp+'html5.svg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='Javascript',
                                                  technologyImagePath=tp+'jsicon.png',
                                                  important=True)    
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='Android',
                                                  technologyImagePath=tp+'android.png',
                                                  important=True)      
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='MySQL',
                                                  technologyImagePath=tp+'mysql.png',
                                                  important=True)     
    ProjectTechnologyStacks.objects.get_or_create(project=digi_repair,
                                                  technologyName='Swift',
                                                  technologyImagePath=tp+'swift.png',
                                                  important=True)                                                                                                                                                     
    ProjectTechnologyStacks.objects.get_or_create(project=un_app,
                                                  technologyName='Java',
                                                  technologyImagePath=tp+'java.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=un_app,
                                                  technologyName='MySQL',
                                                  technologyImagePath=tp+'mysql.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=vogue_app,
                                                  technologyName='Swift',
                                                  technologyImagePath=tp+'swift.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=vogue_app,
                                                  technologyName='Fortran',
                                                  technologyImagePath=tp+'fortran.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=peerpoint,
                                                  technologyName='Azure',
                                                  technologyImagePath=tp+'azure.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=peerpoint,
                                                  technologyName='React',
                                                  technologyImagePath=tp+'reactjs.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=peerpoint,
                                                  technologyName='Node.js',
                                                  technologyImagePath=tp+'nodejs.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=asto_io,
                                                  technologyName='iOS',
                                                  technologyImagePath=tp+'azure.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=asto_io,
                                                  technologyName='nodejs',
                                                  technologyImagePath=tp+'nodejs.jpg',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=asto_io,
                                                  technologyName='aws',
                                                  technologyImagePath=tp+'aws.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=asto_io,
                                                  technologyName='reactjs',
                                                  technologyImagePath=tp+'reactjs.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=vogue_app,
                                                  technologyName='AWS',
                                                  technologyImagePath=tp+'aws.png',
                                                  important=True)
    ProjectTechnologyStacks.objects.get_or_create(project=vogue_app,
                                                  technologyName='Kubernetes',
                                                  technologyImagePath=tp+'kubernetes.png',
                                                  important=False)
    ProjectVideos.objects.get_or_create(project=vogue_app,
                                        projectVideoPath='project_videos/Vogue.mp4')
    ProjectVideos.objects.get_or_create(project=asto_io,
                                        projectVideoPath='project_videos/Asto_new.mp4')

def main():
    # Set up environment

    import_clients()

if __name__ == '__main__':
    main()
