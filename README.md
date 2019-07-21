## ABOUT django-project-template
django-project-template is a project template created with django to save the creation and setup time of django projects. There is one includes a debug bar, and two parameters to load depending on whether you are in production or in development.

## REQUIREMENTS
to use django-project-template, you need to install the following packages:

- Django               2.2.3
- django-debug-toolbar 2.0
- pip                  19.1.1
- python-decouple      3.1
- pytz                 2019.1
- setuptools           41.0.1
- sqlparse             0.3.0
- wheel                0.33.4

## INSTALLATION

***First thing you have to install python 3.7.3, here is the link to download python
[https://www.python.org/downloads/release/python-373/](https://www.python.org/downloads/release/python-373/ "Python 3.7.3").***

We will install pip if it did not come directly with python or update if it is already installed:

	pip intall --upgrade pip

 
> For windows

Then we install mkvirtualenv to create a virtual environment

    pip install mkvirtualenv

To create the virtual environment, type the following command:

	mkvirtualenv venv

When creating the virtual environment, windows automatically activates it.

We will now define our workspace of our project:

	setprojectdirectory venv

From now on, we can access the folder of our project by typing the following command anywhere in a shell:

	workon venv

To install the dependencies of our projects, type the following command:

	pip install -r requirements.txt

Now we are ready to start working on our project :)


> Linux / Mac

Then we install mkvirtualenv to create a virtual environment

	pip install virtualenv  

To create the virtual environment, type the following command:

	virtualenv venv

Activate your virtualenv:

	source bin/activate

