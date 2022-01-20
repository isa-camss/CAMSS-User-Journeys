This development contain the services that executes the different solutions provided by CAMSS.
The core strength of this microservice is Cellar triplestore's SPARL endpoint query API.This is developed in python and has Swagger to run it without the need to launch a UI.

A UI developed in Jupyter notebook can also be accessed so that users can interact in a guided way to the resources and solutions offered by CAMSS.

---

## Clone a repository using command line

You can use Sourcetree, Git from the command line, or any client you like to clone your Git repository. These instructions show you how to clone your repository using Git from the terminal.

1. From the repository, click + in the global sidebar and select Clone this repository under Get to work.
2. Copy the clone command (either the SSH format or the HTTPS).
If you are using the SSH protocol, ensure your public key is in Bitbucket and loaded on the local system to which you are cloning.
3. From a terminal window, change to the local directory where you want to clone your repository.
4. Paste the command you copied from Bitbucket, for example:

### Clone over HTTPS

$ git clone https://github.com/isa-camss/CAMSS-User-Journeys.git

### Clone over SSH

$ git clone git@github.com:isa-camss/CAMSS-User-Journeys.git

If the clone was successful, a new sub-directory appears on your local drive in the directory where you cloned your repository. This directory has the same name as the Github repository that you cloned. The clone contains the files and metadata that Git requires to maintain the changes you make to the source files.

---

## Execute Microservice

1. To configure the a virtual environment and Kernel for the Jupyter notebook.
2. Download the required libraries and dependencies into the virtual environment created using the requirements.txt file.
3. Launch an IDLE.
4. Open project.
5. Run the app_ontology_tools file.
6. Launch a new terminal on the IDLE and run the command to open jupyter notebook.
7. Select the kernel with the libraries installed.
8. Enjoy this service ;)
