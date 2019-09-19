rm -f db.sqlite3
python andch_back/manage.py migrate --run-syncdb
python andch_back/manage.py flush -noinput
./andch_back/populate.py
