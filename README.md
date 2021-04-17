# Fit and Lift

Stream Three Project: Data Centric Development - Milestone Project

![alt text](https://github.com/chris92vr/Milestone4-Fit-and-Lift/blob/master/project-documentation/images/Fit&Lift.gif "Fit & Lift")

Welcome to Fit and Lift,

Website of a gym developed using Django with funtionality of blog and membership options available.

This is my final Milestone Project on the Full Stack Web Developer Code Institute course.

## Table of Contents

1. [Demo](#Demo)

2. [UX](#ux)
    - [Project purpose](#Project-purpose)
    - [Strategy](#Strategy)
    - [User stories](#User-stories)
    - [Admin stories](#Admin-stories)
    - [Design and colors](#Design-and-colors)
    - [Wireframes](#Wireframes)

4. [Database](#Database)

4. [Features](#Features)

5. [Technology Used](#Technology-Used)

6. [Testing](#Testing)

7. [Deployment](#Deployment)

8. [Credits](#Credits)

9. [Disclaimer](#Disclaimer)

[Back to Top](#table-of-contents)

## Demo

A live demo is available [here](https://fit-and-lift.herokuapp.com/ "Fit & Lift").

## UX

### Project purpose: 

The purpose of the project is to build a full-stack site for a gym.

The site allows users to subscribe to the gym by choosing various plans available, consult the blog and add comments, contact the gym via a form for any information.

The project has the following sections:

* Home page
Contains a background with a "Join Us" button in the top. A gallery contains pictures of the gym.


* Membership  
Contains all the membership plans available. If the user is already registered he can choose to extend his subscription.

* Blog  
You can view the Blog and search keywords from all post.

* Contact Us page  
You can contact Fit & Lift staff.

* Login / Register page  
Login page with option to register if someone is not a member yet.

* Profile page  
If the user is logged in there is a Profile page, where the user can check their information and delete account.

* Checkout  
After a membership plan is choosed, the user can proceed to the payment.

[Back to Top](#table-of-contents)

### Strategy

My goal in the design was to create a simple and intuitive interface to be able to easily access through the various pages of the site.



### User stories:

* As a user I would like to be able to view the site on any device I may have, including mobile, tablet, desktop.

* As a user I would like to subscribe to the gym by choosing various plans available.

* As a user I would like to be able to find information about my subscription on my profile page.

* As a user I would like to extend my gym subscription.

* As a user I would like to be able to contact Fit & Lift with my questions.

* As a user I would like to be able to register on the site.

* As a user I would like to be able to search to a keyword to find on the blog.

* As a user I would like to read more details about a post after clicking on it.

* As a user I would like to be able to comment a post.


### Admin stories:

* As an admin I would like to be able to login to an administration panel.

* As an admin I would like to be able to add a post on the blog.

* As an admin I would like to be able to edit or delete a post on the blog.

* As an admin I would like to be able to check comments before they are posted.

* As an admin I don't want a user to be able to add a post on the blog.

* As an admin I would like expired subscriptions to be automatically removed from the database.


[Back to Top](#table-of-contents)

### Design and colors:

#### Fonts:

I used RocknRoll One, from Google Fonts.

Sans-serif is used as the default backup font in case when RocknRoll One was not possible to load.

#### Colors:

* `#8BC3A3` - main color; used for text, logo background, contact us form, background loading overlay and social link icons

* `#000000` - nav background color, applied 0.6 opacity

* `#ccc` - nav text color

* `#222`- footer background colors

[Back to Top](#table-of-contents)


### Wireframes

The following [wireframe](https://github.com/chris92vr/book-mania/tree/master/project-documentation/wireframes)  were created to design the project layout options for large, medium and mobile displays.

[Back to Top](#table-of-contents)



## Database

![alt text](https://github.com/chris92vr/Milestone4-Fit-and-Lift/blob/master/project-documentation/images/DB%20Diagram.jpg "DB Diagram")


During development, I worked with the standard sqlite3, database that comes installed with Django. In the production version, "Fit and Lift" is backed by a PostgreSQL database, hosted and provided by Heroku.

It supports full CRUD functionality with its models.

The custom models created for the database are: User profile, Membership, User membership, Subscription, Post, Comment.

The 'User profile' model saves the users information and displays it in Profile section of the website.

The 'User membership' model uses User profile and Membership as foreign key. 

The 'Subscription' model uses User membership as foreign key. 

'Post' uses User profile as One to One relationship. 

'Comment' model uses Post as foreign key. 



## Features:

### Existing Features

#### Buttons

- **Join Now!** - buttons that redirects user from the homepage to the membership page;

- **Extend Subscription** - button that redirects user  to extend subscription page, visible only to user with gym membership;

- **Read More** - link redirecting a user to another age for read all post from the blog;

- **Edit / Delete buttons** - buttons that enable editing and deleting post, visible only from the superusers;

- **Delete account button** - button that performs action of deleting an account and all votes, comments and reviews associated with it;

- **Back to top button** - dynamic back to top button  so user can go back to the top of the page without scrolling back.


#### Forms

- **Register form** - Django allauth register form that enables user to use the app. User input includes username, email address, password, first name and last name;

- **Log in form** - Django allauth login form that enables user to sig into the user account;

- **Post comment form** - form that enables user to post a comment for a post on blog;

- **Add post form** - form that enable superusers to add a new post to the blog;

- **Edit post form** - form that pulls information about the existing post and enable superusers to edit it;

- **Payment form** - form that enables user to submit payment;

- **Contact Us form** - form that enables user to contact Fit & Lift staff;

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices.  The navbar contains links to associated sections i.e. Home, All Reviews, Add Book, Profile, Log Out;

- **Footer** - contains disclaimer copiright Fit and lift, above social link icons;

#### Other

- **Pagination** - Used to paginate post on Blog, so users view 3 post per page;

- **Search bar** - Search bar that enables users to search any keyword on the blog.

- **Remove expired subscriptions** - Once a registered user goes to the memebership or profile page, the expired subscriptions are removed from the database.

[Back to Top](#table-of-contents)

### Features left to implement

Perform removal of expired subscriptions via cronjob once a day.

[Back to Top](#table-of-contents)

## Technology Used:

### Programming languages

- **HTML** 

- **CSS** 

- **JavaScript** 

- **Python** 


#### Libraries, frameworks, tools used

* <a href="https://getbootstrap.com/">Bootstrap</a> framework was used for developing a responsive, mobile-first website
* <a href="https://www.djangoproject.com/">Django</a> as python web framework used for rapid development, maintainable, clean design
* <a href="https://jquery.com/">jQuery</a> JavaScript library to simplify HTML DOM manipulation
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a> Used Noto Sans fonts
* <a href="https://fontawesome.com/">FontAwesome</a> as icon provider
* <a href="https://stripe.com/">Stripe</a> made it possible to receive payments for the eggs
* <a href="https://pypi.org/project/psycopg2/">Psycopg2</a> as database adapter for the Python
* <a href="https://gunicorn.org/">Gunicorn</a> or Green Unicorn, a WSGI server implementation used to run Python web application
* <a href="https://git-scm.com/">Git</a> Version control
* <a href="https://github.com">Github</a> Used as a Git repository hosting service
* <a href="https://www.heroku.com/">Heroku</a> Is a container-based cloud Platform, I used Heroku to deploy this app.
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to check my Python code.
* <a href="https://balsamiq.com">Balsamiq</a> Used to create wireframes.
* <a href="https://aws.amazon.com/s3/">AWS S3 Bucket</a> as a cloud storage
* <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html">Boto3 </a>to make use of Amazon S3
* <a href="https://python-pillow.org/">Pillow</a> for saving image file formats
* <a href="https://miniwebtool.com/django-secret-key-generator/">miniwebtool</a> for generating new SECRET_KEY
* <a href="http://ami.responsivedesign.is/#">Am I Responsive</a> Online tool was used to display the project on various devices;
* <a href="https://www.canva.com">Canva</a> Online tool was used to create Fit & Lift logo;
* <a href="https://app.diagrams.net">Draw.io</a> Online tool was used to create ER database diagram;



#### Databases

* <a href="https://www.postgresql.org/">PostgreSQL</a> database service provided directly by Heroku
* <a href="https://www.sqlite.org/index.html">SQlite3</a> provided by django

[Back to Top](#table-of-contents)


## Testing

### Code validation

In order to to check the validity of the website code, I have used the following:

    - HTML Validation: https://validator.w3.org/ - no errors identified.
    - CSS Validation: https://jigsaw.w3.org/css-validator/ - Identified issues with materializecss not with my project.
    - PYTHON Validation: https://pep8online.com/ no errors identified.


### Functionality Test

All the features were tested manually throughout the application development process. Table below outlines all features and tests performed on them, as well as all resolved and remaining bugs associated with tested features.


| Description | Expected Outcome | Pass/Fail
| ---|:-----------------------------------------:| :---: | 
Join Now! button| On click, the browser navigates to Membership page| pass
Heart Icon home page | Heart icon rotates over the mouse cursor| pass
Fade in text homepage |Once the homepage is loaded, the writing "Fit your body, Lift your soul" fades | pass
Membership| Once logged in, it is possible to join a subscription plan of your choice| pass
Extend Membership | Once registered, you can extend the membership plan as you wish | pass
Remove Expired Subscriptions | Expired subscriptions are removed from the database | pass
Stripe Payment  | The payment system is safe and reliable | pass
Blog | The Blog is accessible to everyone but the details of the posts are visible only to those registered | pass
Pagination Blog| Limit viewing post to 3 per page | pass
Confirmation Email | The user receive an confirmation email once registered or subscribed | pass
Admin Email| Once a user send contact us form , admin receive an email with the information| pass
Comment| User can comment on posts, but they must be approved by the admin before being published | pass
Post| Admin can add posts. Once added, it can be edited or deleted | pass
Search Engine | The search for the keyword in the blog is successful | pass
Back to the Top (Arrow up icon)) | The browser goes back to the top of the page | pass
Contact Us form| User can contact the Fit and Lift staff by email | pass
Register Form| Input fields must be validated and not empty. the data entered is correctly saved in the database with the encrypted password field | pass
Login Form| A user can login only with the right username and password | pass
Navbar | All navbar menu items redirect user to the appropriate page, collapses on smaller devices | pass




### Responsiveness testing

Several tests were carried out to verify the correct functioning of the project with positive results.
The functionality of the site is optimal. Browser compatibility is verified for Firefox and Chrome on Windows 10 home; Firefox, Chrome on Ubuntu 19.10 and Firefox, Chome on Android 10. The responsiveness of the pages is suitable on desktop screens, tablets and mobile phones.
In the folder [project-documentation/testing](https://github.com/chris92vr/book-mania/blob/master/project-documentation/testing/ "testing"), there are screenshots named in the following format: (screen resolution) - Operating system (browser) - screen description.

[Back to Top](#table-of-contents)

## Deployment

#### Running Code Locally


1. Follow this link to my [Repository on Github](https://github.com/chris92vr/Milestone4-Fit-and-Lift) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
python -m .venv venv  
source env/bin/activate

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

import os  
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here")
os.environ.setdefault("STRIPE_SECRET", "secret key here")
os.environ.setdefault("DATABASE_URL", "secret key here")
os.environ.setdefault("SECRET_KEY", "secret key here")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account and create new products.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

AWS_S3_OBJECT_PARAMETERS = {  
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',  
    'CacheControl': 'max-age=94608000'  
}

AWS_STORAGE_BUCKET_NAME = 'fit-and-lift'  
AWS_S3_REGION_NAME = 'us-east-2'  
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")  
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")  

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level:

from django.conf import settings  
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):  
&nbsp;&nbsp;&nbsp;location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):  
&nbsp;&nbsp;&nbsp;location = settings.MEDIAFILES_LOCATION

14. Went to `settings.py` and added:

STATICFILES_LOCATION = 'static'  
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'  
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Returned to `Heroku` and hit `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `fit-and-lift.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.

## Credits



- Images supplied by Pixbay, Upsplash, Pexels.

- I used Stack Overflow for guides in developing my own codes.

- I consulted https://djangocentral.com/ for the creation of the blog.


#### Acknowledgements

Thanks to my mentor Brian Macharia for support and advice throughout the project.

[Back to Top](#table-of-contents)

#### Disclaimer

This project was created for educational use only.

[Back to Top](#table-of-contents)
