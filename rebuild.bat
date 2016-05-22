cd initDB
mysql -u atom --password=atom mShanbay < rebuild_database.sql
cd ..
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py init_dev_words_db
pause
