rm -f db.sqlite3
python andch_back/manage.py migrate --run-syncdb
./andch_back/populate.py
