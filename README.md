# Mailchimp FastAPI Server

A FastAPI server for synchronizing subscriptions with Mailchimp.

## Overview
This project provides a FastAPI server implementation to synchronize subscription data with Mailchimp. It's designed to be easy to set up, with clear documentation and a straightforward API.

## Features
- **FastAPI Integration**: Leveraging the speed and ease of FastAPI.
- **Mailchimp API Integration**: Seamless connection with Mailchimp for managing subscriptions.
- **Environment Variable Configuration**: Secure and flexible configuration using `.env` files.

## Getting Started
### Prerequisites
- Python 3.6+
- pip

### Installation

Clone the repository & Install the required packages:
```
pip install -r requirements.txt
```

### Configuration
1. Rename the `.env.example` file to `.env`.
2. Fill in your Mailchimp API Key, Data Center, and List ID in the `.env` file.

```
MAILCHIMP_API_KEY=your_mailchimp_api_key
MAILCHIMP_DATA_CENTER=your_data_center
MAILCHIMP_LIST_ID=your_list_id
```

### Running the Server
Run the FastAPI server with:
```
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

## Usage
### Subscribe to Mailchimp
Make a POST request to `/mailchimp/subscribe` with the following JSON payload:

```
{
  "name": "John",
  "surname": "Doe",
  "email": "john.doe@example.com",
  "number": "1234567890"
}
```

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- FastAPI
- Mailchimp API