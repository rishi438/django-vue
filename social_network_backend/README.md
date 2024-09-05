# Project Name

## Description

This project is a Django application managed with Poetry for dependency management. It includes common development tasks such as installing dependencies, applying migrations, creating a superuser, and running the development server.

## Requirements

- Python 3.8 or higher
- Poetry

## Setup

1. **Install Dependencies**

   Use Poetry to install the required dependencies:
   ```sh
   make install

   make migrations
   make migrate
   make superuser
   make run-server
   make update
   ```

## Environmental Variables
1. **Create .env file in social_network_backend/social_network_backend/settings/.env**
    ```
    SECRET_KEY=<your_secret_key>
    DEBUG=<True_or_False>
    DB_NAME=<your_database_name>
    DB_USER=<your_database_user>
    DB_PASSWORD=<your_database_password>
    DB_HOST=<your_database_host>
    DB_PORT=<your_database_port>
    ```
