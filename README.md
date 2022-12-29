# Challenge Greenole

This API allows for background storage of measurement data that would otherwise originate from sensors.

# Technologies
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/)
- Unitary Tests

# Installation

To access the API, first, clone this repository.
```bash
git clone https://github.com/filipenascimento98/challenge-greenole.git
```

# How to use
This project depends on [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/). With the dependencies resolved, navigate to the project directory that contains the __docker_compose.yml__ file and run the following command that will build and deploy the application:
```bash
docker-compose up -d
```
Thus, the application will run in a Docker container.

# Endpoints
In this API we store measurement data in the background. We have the following endpoints:

* /api/user/
* /api/login/
* /api/measurement/
* /api/measurement/?value=24&time=hour

For more details, you can consult the documentation for this API on the endpoint:
```bash
/api/docs/
```

# Project structure
A brief explanation of some structural elements of this project.
* api: Only app in this project.
    * views: Contains the files in which the views called by the defined routes.
    * domain: Layer responsible for the business rule and data manipulation to be passed on to the views.
    * serializers: Directory that stores the serializers that are responsible for validating the input data of each route.
    * data_access: Layer responsible for data access.
    * tests: Directory that stores automated tests.

# Automated Tests
To run the automated tests navigate to the directory where the __manage.py__ file is located and execute the following command:
```bash
python manage.py test -b
```


