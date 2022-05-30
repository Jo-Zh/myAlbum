# myAlbum

<h2>Introduction</h2>
A simple Django App for users login and upload or save their moment, videos, picutres etc. files. Besides with integraed video record function.

<h2>Deployment process</h2>
This app is deployed on heroku http://myalbum-djangoapp.herokuapp.com/. 
Here is just a short summary about the deployment experience I would like to share:
<ol>
<li> set App ready to deploy:
   1.1 modify SECRET_KEY, and change DEBUG to False in setting.py
   1.2 add STATIC_ROOT in setting.py, run static collection.
   1.3 install gunicorn, sqlurl, whitenose etc. 
   1.4 create requirement.txt, runtime.txt, Procfile in root
</li>
<li> build on heroku:
   2.1 install heroku cli, under project directory, run git init and heroku create (if you want give your app a certain name then maybe run heroku apps:create example (refer to: https://devcenter.heroku.com/articles/creating-apps))
   2.2 set heroku config:set DISABLE_COLLECTSTATIC=1, set allowedhost =['*'] actually these can be done after first build on heroku, but during my first building process, there were couple of issues related to static collect, so I did it before and also ran static collection locally at earlier stage 1.2. (refer to https://devcenter.heroku.com/articles/django-assets)
   also when I opened my app at my first trial with allowedhost = ['my domain name'], I got 400 bad request. So  I set allowedhost =['*'].
   
   2.3 run git add . and git commit -m "ready to deploy" save app to your local repo. Then run git push main heroku. 
    
   
   2.4 After successfully building, run heroku run python3 manage.py migrate, heroku run python3 manage.py createsuperuser
</li>
<li>Issues:
   3.1 uploading files:
   Most of functions are working except uploading files.
   when I click new album go to the new site create new one. I can fill the form with title, description, style, author, choose media file, a picture for example, from my local computer. but the file will not show on the website or actually it will not be uploaded.
   I checked the heroku document, and cannot find a free way to do this. I only find to add a add-on with extra cost, refer to: https://devcenter.heroku.com/articles/simple-file-upload.

3.2 the web loading is slow.

</li>
<ol>
<hr>
<h5>Any ideas would be welcomed and appreciated</h5>
