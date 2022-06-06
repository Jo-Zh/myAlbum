# myAlbum

<h2>Introduction</h2>
A simple Django App designed to save photos, make picture collections or catch a beautiful moment.
<img src="static/css/myalbumcover.png" width="500"/>
<h3>what you can do</h3>
<p>
In Home page, user can see how many records in total in the app. User need to login to use myalbum, save a moment functions <br>In myalbum site: <br>user sees own records and can simply create ,delete, browser own posts. At this moment user cannot see others' posts. And at this stage, user can only upload images and other files except video. <br>In save a moment site:<br>user can use save a moment link to catch a 5s video and save in local downloads file directory.
</p>

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
The web loading is really slow.
User cannot see others' posts, the sharing function hasn't added yet.

</li>
<ol>
<hr>
<h4>Any ideas would be welcomed and appreciated</h4>
