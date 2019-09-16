## populate.py
##
## script to populate django's models with dummy data

## run script with:      python populate.py to run
## If data is corrupted, then first use:     python manage.py flush

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andch_back.settings')
django.setup()

from andch_back_app.models import Client

def import_clients():
    Client.objects.get_or_create(clientName='Shawbrook',
                         clientLogo='andch_back/static/img')
    Client.objects.get_or_create(clientName='British Airways',
                         clientLogo='andch_back/static/img')

def main():
    #Set up environment

    print('Importing clients... ', end='')
    import_clients()
    print('done!')

if __name__ == '__main__':
    main()
