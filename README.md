# Personal-Gallery

A virtual gallery of images, using django

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, **clone** this repository into a **virtual environment** and install the package manager, **pip**.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Use the package manager pip to install all project requirements. 
1. Git Clone the project with: ```git clone https://github.com/ABERT-NOLA/personal-gallery-```.

2. Move to the base directory: ```cd Images```

3. Create a new python environment with: ```$ python3.6 -m 2 --without-pip virtual```.

4. Activate enveronment with: ```source virtual/bin/activate``` on  Linux.

5. Upgrade pip using: ```(virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python```

6. Install required dependencies with: ```pip install -r requirements.txt```.

7. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

8. Run the app locally  ```python manage.py runserver```.


## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43) to see it live or simply run it locally
 ```
 (virtual) $ python3 manage.py runserver
 ```

## Built With
* [MDB](https://mdbootstrap.com/) - The Frontend platform 
* [Django 3.0.8](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.6](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


## Authors

* [ABERT NOLA](https://github.com/ABERT-NOLA)


## License
**[MIT](./LICENSE)** (c) 2020 **[ABERT NOLA]()**