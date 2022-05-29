# myAlbum
A simple Django App for users login and upload or save their moment, videos, picutres etc. files. Besides with integraed video record function.

This app is deployed on heroku. 
Here is just a quick summary about the deployment I would like to share:
1. set App ready to deploy:
   1.1 modify SECRET_KEY, and change DEBUG to False in setting.py
   1.2 add STATIC_ROOT in setting.py, run static collection.
   1.3 install gunicorn, sqlurl, whitenose etc. 
   1.4 create requirement.txt, runtime.txt, Procfile in root
   1.5 install heroku cli, under project directory, run git init and heroku create (if you want give your app a certain name then maybe run heroku apps:create example (refer to: https://devcenter.heroku.com/articles/creating-apps))
   1.6 set heroku config:set DISABLE_COLLECTSTATIC=1, set allowedhost =['*'] actually these can be done after push 1.5, but during my building process, there were couple of issues related to static collect, so I did it before and also ran static collection on my local at earlier stage 1.2. (refer to https://devcenter.heroku.com/articles/django-assets)
   also when I opened my app at my first trial with allowedhost = ['my domain name'], I got 400 bad request. So  I set allowedhost =['*'].
   
   1.5 create heroku project, run heroku migrate, from local git push to heroku main

my app is running on https://safe-atoll-49171.herokuapp.com/. most of functions are working except uploading files.
when I click new album go to the new site create new one. I can fill the form with title, description, style, author, choose media file, a picture for example, from my local computer. but the file will not show on the website or actually it will not be uploaded.
I checked the heroku document, and cannot find a free way to do this. I only find to add a add-on with extra cost, refer to: https://devcenter.heroku.com/articles/simple-file-upload.
