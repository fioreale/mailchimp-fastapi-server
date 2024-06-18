# Mailchimp FastAPI Server

A robust and efficient FastAPI server designed for synchronizing subscriptions with Mailchimp, this project stands as a testament to the seamless integration between FastAPI's asynchronous capabilities and Mailchimp's powerful subscription management features.

[![Stars](https://img.shields.io/github/stars/fioreale/mailchimp-fastapi-server.svg)](https://github.com/fioreale/mailchimp-fastapi-server/stargazers)

If you find this project helpful, please consider giving it a star. Thanks!

## Overview

This project showcases a state-of-the-art implementation of a FastAPI server, specifically tailored to synchronize subscription data with Mailchimp. The primary goal of this project is to offer an easy-to-setup, well-documented, and straightforward API that bridges the gap between your application and Mailchimp's subscription management. The server is designed with scalability and ease of use in mind, making it an ideal solution for both small projects and large-scale applications.

## Features

- **FastAPI Integration**: This project is built on FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. The key features of FastAPI are its speed and its ability to handle asynchronous requests, making it a perfect choice for this kind of application.
- **Mailchimp API Integration**: We provide a seamless integration with the Mailchimp API, allowing for efficient management of subscription data. This integration is crucial for businesses and developers looking to automate their email marketing and audience engagement strategies.
- **Environment Variable Configuration**: Security and configuration flexibility are at the forefront of this project. The server utilizes `.env` files for environment variable management, ensuring sensitive information such as API keys are securely stored.

## Getting Started

### Prerequisites

This project requires Python 3.6 or newer and pip. These prerequisites are fundamental as they ensure the project runs on a stable and widely-supported base of the Python programming language.

### Installation

To get started with this project, clone the repository and install the necessary dependencies. We have streamlined this process to make it as straightforward as possible:

```
git clone https://github.com/yourusername/mailchimp-fastapi-server.git
cd mailchimp-fastapi-server
pip install -r requirements.txt
```

### Configuration

The project uses a `.env` file for managing environment variables, allowing you to easily configure your Mailchimp API integration:

1. Start by renaming the `.env.example` file to `.env`.
2. Next, fill in your Mailchimp API Key, Data Center, and List ID in the `.env` file. This step is crucial for ensuring your API integration works correctly.

```
MAILCHIMP_API_KEY=your_mailchimp_api_key
MAILCHIMP_DATA_CENTER=your_data_center
MAILCHIMP_LIST_ID=your_list_id
```

### Running the Server

You have two options to run the server: using Poetry or the classic local way with Uvicorn.

- **With Poetry**: If you're using Poetry, simply run `poetry run uvicorn main:app --reload`.
- **With Uvicorn**: For a more traditional approach, `uvicorn main:app --reload` will suffice.

The API will be available at `http://localhost:8000`, providing a local platform for testing and development.

### Docker Support

For users who prefer Docker, we've included a Dockerfile and a Docker Compose file. These files simplify the process of containerizing the application, making it easy to deploy and run in any environment that supports Docker:

```
docker compose up
```

This command builds and runs the container, abstracting the complexity of environment setup.

## Usage

### Subscribe to Mailchimp

Interacting with the Mailchimp API is straightforward. To subscribe a user to Mailchimp, make a POST request to `/mailchimp/subscribe` with the following JSON payload:

```
{
  "name": "John",
  "surname": "Doe",
  "email": "john.doe@example.com",
  "number": "1234567890"
}
```

This endpoint encapsulates the complexities of the Mailchimp API, providing a simple and intuitive interface for subscription management.

## License

This project is openly licensed under the MIT License. We believe in open source software and the value of community contribution, and the MIT License provides the flexibility and freedom needed to support this belief.

## Contributing

We warmly welcome contributions to the Mailchimp FastAPI Server project! Whether it's bug reports, feature requests, or code contributions, your help is invaluable to making this project better.

### How to Contribute

1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Create a Branch**: Create a branch in your fork for your changes.
3. **Make Your Changes**: Implement your bug fix, feature, or other contributions.
4. **Test Your Changes**: Ensure your changes do not break any existing functionality.
5. **Submit a Pull Request**: Open a pull request against our repository from your branch. Provide a clear description of the changes you've made.

### Contribution Guidelines

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions on how to contribute, coding conventions, and the process for submitting pull requests.

Your contributions are greatly appreciated and will help make this project even better!

## Acknowledgements

- **FastAPI**: For providing a high-performance, easy-to-use framework that forms the backbone of this project.
- **Mailchimp API**: For their robust API, which allows seamless integration of subscription management features.
