
# <a href="https://ecommerce-10.herokuapp.com/"> Three Peaks Sports </a>
<h4>Ecommerce Stream3: Code Institute Project</h4>

<h3> <b> About </b> </h3>

<h3> This is an Ecommerce web application created for Stream 3 of Code Institute's Bootcamp course.  Live link to project: <a href="https://ecommerce-10.herokuapp.com/"> Ecommerce website </a> 
 </h3>



<h3> <b> Tools and Frameworks </b> </h3>

 <ol>
  <li> <a href="https://www.python.org/downloads/release/python-376/"> Python </a>  - The main language used for this project is Python, the version of Python that was used to write the applications is 3.7.6. <br>
  
```
python --version
Python 3.7.6 
```

  </li>
  <li> <a href ="https://docs.djangoproject.com/en/3.0/">Django</a>  - This is a 'Python-based free and open-source web framework that follows the model-template-view architectural pattern'.  </li>
  <li> HTML+CSS - Basic HTML+CSS was used to format the webpage </li>
  <li> <a href= "https://getbootstrap.com/docs/4.5/getting-started/introduction/">Bootstrap</a> - The main framework for building the webpage HTML/CSS layout for the application </li>
  <li> JavaScript - Javascript was used for communication with Stripe API - with files 'Stripe.js' (JS library for providing purchasing and card authentification for Stripe); additional javascript scripts were included for manipulating the website header and footer functionality.  </li>  
  <li> Database  - Application retrieves static files from Amazon's AWS S3. The project is also connected to Heroku Postgres database <a href='https://www.postgresql.org/docs/'>. The  PostgresSQL </a> database (that is connected to Heroku) can be modified locally or online and is used to store user's credentials and information. The database is takes new user's registration information and stores it for future logins. Items for purchase within the website are also stored in the database. </li>
<li> Stripe -  The project uses and implements the STRIPE API configurations (that are configured though the JS script 'Stripe.js'). The configurations allows purchases and credit card authentications to be made on the website allowing for users to purchase the products stored in the database online. Purchases are then linked to the my personal stripe account, whereby payements made are stored and funds can be retrieved. </li> 

</ol>  

 

<h3> <b> More about this Application </b> </h3>  
<h4> This project was built using Django. This Django project has five internal applications: </h4>

<h3><a href ="https://docs.djangoproject.com/en/3.0/"> Django </a>  </h3>
<ol>

 <li> <i> Cart </i> - This internal application stores items (Products) in the shopping cart of items that come from the Amazon AWS bucket and enables them to be bought using the checkout App that uses a javascript file Stripe.js on the backend. This internal application also contains and stores all the information that connects the products to the cart and finally, the (last) app 'checkout.' </li>
   
   <li> <i> Accounts </i> - This internal application contains the reference to all the users' information on their accounts and credentials that are used to create, modify, and use login and signup information. </li>
  
  <li> <i> Products</i> - This internal applocation contains and stores all the references to products (id, category, price, and quantity) in the 'stock' database of the website.</li>
  
<li> <i> Checkout </i> - This internal application contains and stores all the information related to products, accounts, and carts so that products can be ordered and purchased using Stripe's API (using Stripe.js). </li>

</ol> 

<h4> Folders and directories contained within the Django Application </h4>
<ul> 

<li> <i> Ecommerce </i> - This folder contains the main settings for the overall application and is an internal application that is used to link all the other internal applications together. </li>


<li> <i> Static </i> - This folder contains the main static files for the overall application - including all CSS and JS files. Files that are specific to the font's used in the app are also contained here. </li>

<li> <i> Templates </i> - This folder contains all the HTML files/templates that are used to render the applications online and that are link the applications by the Django url settings file (that is contained within the urls.py file) </li>


<h3> <b> Requirements </b> </h3>

1. Installation - To install requirements run the command:

```
pip install -r requirements.txt
```

This will install the following pip packages (i.e,requirements to run the project):

2. Listing requirements present in requirments text file in terminal:

```
cat requirements.txt
```
The command above will show the requirements that are listed in the requirements.txt file.

3. Listing pip packages from the current python environment in terminal:
```
pip list
```

The command above will show all the requirments that are currently being used within the Python environment. 




4.  Updating requirements - To update requirements, run the command:
```
pip freeze > requirements.txt
```
The command above will update the requirements.txt file to include any packages that have been modified, updated or included in the project. Any packages that are present within the python environment that are in use will be written onto the requirements.txt file.



<h3> <b> Deployment </b> </h3>


1. Download or pull the repository 

2. Create a new Virtual Environment for the project. You can follow this useful guide on how to do it:  <b> <a href='https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ '> How to create new Virtual Environment</b>


3. Install all requirements and packages

```
pip install -r requirements.txt
```

4. A project can be run locally by then cd'ing into the main project directory (where manage.py is contained). This is the main directory for the project. From there, the project can be run locally by using the command 'python manage.py runserver' on the terminal.

```
python manage.py runserver
```


5. Making modifications to internal Django applications - Modification and updates of internal applications (Cart, Accounts, etc.) should be migrated before local and/or global deployment. This ensures that a change/modification to an internal application is integrated with other internal applications. For example, any changes made to the 'Cart' application must created and migrated to the other internal applications of the project.  In order to do that, the following commands should be run on the terminal window (within the main project directory)

```
python manage.py makemigrations

python manage.py migrate
```


<h3> <b> Versioning </b> </h3>

The project is connected to heroku.git (from which it is automatically deployed). This repo is a new copy of the existing Heroku.git repository. If you desire to see the existing branches of the project, you can see the updates to this project by following this repository.

The full application was deployed and is hosted on Heroku using the gunicorn package (Python). Gunicorn will initialize the HTTP address for the application on a webserver; The Procfile file gives Heroku the information to run the app and requirements.txt is a file that contains all the Python packages that are required to run the application. </h4> 


<h3> <b> Security </b> </h3>
The project has ignored, ommitted or obfuscated any sensitive files and data in order to preserve and secure any data that is sensitive. For that reason, this project is only a skeleton of the main application online </li> 



<h3> <b> Bugs and Issues </b> </h3>

The Header sometimes fails to update status (login successful), but will update with page refresh/reload.


<h3> <b> Acknowledgments </b> </h3>

<h6>Credit to <a href='https://github.com/richardadalton/com-devjoy-ecommerce'> Richard Dalton </a> For providing a preliminary project structure and basic guidelines 
and for <a href='https://github.com/hschafer2017/django-UserTypes'> Haley Shaffer </a> for providing guidelines on how to have different Django user types on the Django application 
</h6> 



