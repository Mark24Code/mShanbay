cd initDB
mysql -u atom --password=atom mShanbay < rebuild_database.sql
cd ..
python3 manage.py makemigrations
python3 manage.py migrate
pause
