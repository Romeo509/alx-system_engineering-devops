Project: 0x1A-application_server

For the successful deployment of our AirBnB clone v2 web application on server web-01, several key steps were necessary, including the installation of essential networking tools and the configuration of the Flask application.
Installation of Net Tools

The initial phase of the project required the installation of net-tools, a crucial package in Linux systems providing a suite of command-line utilities for network administration and monitoring. This step was executed with the following command:

bash

sudo apt install -y net-tools

Deployment Process

    Clone AirBnB Clone v2 Repository
        Utilizing Git, we cloned the AirBnB clone v2 repository onto our server web-01.

    bash

git clone <repository_url>

Configure Flask Application

    Within the cloned repository, we located the file web_flask/0-hello_route.py and made necessary modifications to ensure the application serves its content from the route /airbnb-onepage/ on port 5000. Additionally, we ensured that the Flask application object was correctly named 'app' as required for validation purposes.

Run Flask Application

    After configuring the Flask application, we initiated the application using the following command:

bash

python3 -m web_flask.0-hello_route

Verify Application

    To ensure proper functionality, we sent a request to the Flask application using curl in a separate terminal window, confirming that the content was served correctly.

bash

    curl 127.0.0.1:5000/airbnb-onepage/

Through meticulous execution of these steps, we successfully deployed the AirBnB clone v2 web application on our designated server, paving the way for further development and testing.
