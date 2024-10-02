# Backend Training 2024

This project is designed specifically for programs related to FastAPI. It aims to allow students to focus on learning FastAPI without worrying about environment setup. The project includes the necessary configurations and dependencies to start quickly and easily.

## Prerequisites

Make sure you have the following software installed on your machine:

- Git
- Docker Desktop or Docker Engine

## Project Structure

The project is structured as follows:

- `requirements.txt`: Lists the Python dependencies required for the project.
- `Dockerfile`: Contains the instructions to build the Docker image for the FastAPI application.
- `docker-compose.yaml`: Defines the services and configurations for running the project using Docker Compose.
- `app/`: Directory containing the FastAPI application code.
- `members/`: Directory for storing each participant's assignments as Git submodules. Each participant should add their own repository as a submodule under `members/` using the following steps in [members/README.md](members/README.md).

## Setup Instructions

### 1. **Clone the repository**

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. **Make your own compose and requirements**

```bash
cp docker-compose.yaml.example docker-compose.yaml
```

### 3. **Make sure your requirements file and project with main.py are in the app direcotry**

```bash
mkdir -p app
touch app/requirements.txt
touch app/main.py
```

> [!TIP]
> You can **copy** `requirements.txt.example` file into `app` directory and rename to `app/requirements.txt`

> [!NOTE]
> Please make sure that `main.py` is not empty.

### 4. **Build and start the application using Docker Compose**

```bash
docker-compose up --build -d
```

### 5. **Access the FastAPI application**

The FastAPI application will be available at `http://localhost:8080`.

## Dockerfile

The `Dockerfile` sets up the environment for the FastAPI application. It includes the following key steps:

- Use an official Python base image.
- Set the working directory.
- Copy the necessary files.
- Install the required Python packages.
- Specify the command to run the FastAPI application.

## Docker Compose

The `docker-compose.yaml` file defines the services required for the application. It includes:

- The FastAPI service, built from the Dockerfile.
- Configuration for environment variables and port mappings.
- MariaDB database service and PHPMyAdmin.

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine.
3. Create a new branch (`git checkout -b feature/your-feature`).
4. Make your changes and commit them (`git commit -am 'Add new feature'`).
5. Push the changes to your forked repository (`git push origin feature/your-feature`).
6. Go to the original repository on GitHub and create a Pull Request from your forked repository.

## Contact

For any questions or issues, please contact the project maintainer at [nycu1sdc@gmail.com](mailto:nycu1sdc@gmail.com).
