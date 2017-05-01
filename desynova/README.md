# The follwing are instructions for how to user these three apps in desynova directory
# Navigate to desyonva directory after taking git pull

# install pip
apt-get install pip ( Ubuntu systems. I don't care about windows. ) .

# install virtualenv
pip install virtualenv

# make a virtual env dir
virtualenv env

# activate it
source env/bin/activate

# install all dependencies
pip install -r requirements.txt

# login to mysql and make a database called desynova and set it's password to 'root' and username to 'root'.  if you want to change
# that, you must make correct changes in settings.py then.
mysql -uroot -proot ( assuming your mysql has username and password set to 'root' )
create database desynova  ( execute this  in Mysql Shell )

# run django server
python manage.py runserver

# run migrations
python manage.py migrate

# run redis server
redis-server

# add cron job to crontab ( required for third app ). I am using django-crontab to schedule the job to fetch data from server
python manage.py crontab add

# verify that the job is discovered by crontab
python manage.py crontab show

let url = 'http://0.0.0.0:8000' or whatever your server address is. Replace {{url}} in following
paragraphs with whatever address your django server is running.

# First app 'shortly' instructions

1.  visit  {{url}}/shortly/url-shortener/  . This will open a basic html form in which you will be prompted for a url
to enter. Hit submit after entering the url.
2. You will be given a shorter version of the url after you press submit. click on that url and you will be redirected to
original url you entered in step 1.

# Second app 'paste_lockly' instructions

1. visit {{url}}/paste-lockly/message/.   This will open a basic html form in which you are asked to enter the message you want
to optionally encrypt. After you have entered the message, you can chose to provide a secret key to encrypt the message. Since i have
used AES algorithm to encrypt the message, the key has to be either 16, 24 or 32 bytes long. The code does these kinds of checks for
you if you enter invalid key. After giving key, hit submit.

2. On submit button, you will be redirected to a url of form {{url}}/paste-lockly/encrypted-message/xx/ where 'xx' is unique number given
to each message you enter in step1. You can copy this url and give to anyone. At this url a read only form of the encrypted
message is shown and a space to enter key is asked. The user must provide correct key in order to decrypt the message. Various kinds
of error checks have been made in backend to handle such cases.

3. In case you enter the correct key, you are redirected to a page where your decrypted message is shown. In case you enter incorrect key,
a valid error is thrown.

# Third app 'web_scrapper' instructions

1. Make sure 'redis-server' is running on port configured in settings.py
2. Make sure you have run python manage.py crontab add command which adds the cron i have defined to list of active crons.
3. Make sure python manage.py runserver has been run
4. open /path to desynova folder/desynova/desynova/web_scrapper/templates/stock_data.html in chrome. 'stock_data' is name of the file,
open it.
5. You will see a page that shows top 10 gainers data in HTML card layout. You can chose which type of data you want to look
by chosing options "gainers", "losers" from dropdown. The data will be updated in 120 seconds. You can change this to whatever
you want by changing 'sec' variable in 'stock_data.js'.
6. Make sure the variable 'base_url' in 'stock_data.js' is same url on which you django server is running.














