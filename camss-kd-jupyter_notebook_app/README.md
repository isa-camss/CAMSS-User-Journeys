# Microservices Template
This repository provides the basic skeleton to get a robust and reusable API endpoint, implemented in docker.

This template is designed under the following criteria:
- Rapid microservices development and delivery,
- Separate logic for back-end and front-end.
- Containerization so that each application resides in its own environment and its requirements are managed separately.

## Technologies
The following technologies are included in this template:
- The Flask micro framework,
- Swagger UI that automatically generates documentation that allows to viewing and interacting with API resources.
- Docker to replicate a microservice on servers with the minimal configuration
- Coverage to execute automated test.

## Getting Started
These instructions will give you a complete functional environment of the project. 
This is a guide on how to install and deploy the solution. You can adapt it to 
your operating system and/or your specific needs.

### Pydoc
Consult the Pydoc documentation about the projetc's modules, classes, functions and methods saved to HTML files.

#### Generate a Pydoc
To generate the Pydoc documentation about the projetc's modules, classes, functions and methods follow the steps below:
##### Generate HTML file
- $(name_env)>  *python -m pydoc -w <file_name or project_route>*

##### Generate a Served HTML
- $(name_env)>  *python -m pydoc -b>*

Terminate the service pressing "q" button.

### Prerequisites
This project has some requirements that must be fulfilled before starting the installation:
- Python 3.9.12
- Pip 10.0.1
- Libraries dependencies (install requirements.txt)
- Docker engine 
- Running the tests

## Running the tests
All the functions of the project have associated unit tests to verify that everything works correctly. These tests can be executed in several ways:
- By going to the test file and running them one by one.
- Through the coverage library:
  - *pip install coverage*
  - *coverage run -m unittest discover*
  - To obtain the test report: *coverage report*

## Running the Flask Application
Run the wsgi.py file or through the command line go to the "dev" folder and run the following command:
 - *python -m flask run*

## Running the Flask Application with Docker
Open the Ubuntu terminal and execute the following commands:
- *sudo service docker start*
- *docker build -t  kf_template .*
- *docker run kf_template*
- *docker run -p 5000:5000 kf_template*
