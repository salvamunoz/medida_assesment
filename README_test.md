# Project Documentation

## Introduction

Welcome to the documentation for our project! This guide will help you understand the structure, components, and functionality of our application. 

## Table of Contents

1. Getting Started
2. Project Structure
3. Installation
4. Usage
5. Testing

## Getting Started

Before diving into the code, let's get acquainted with the project's purpose and goals. Our application get the events from an external API and show the desired events depending on the league and dates you are looking for.

## Project Structure

Our project follows a structured layout to organize the codebase efficiently. Here's an overview of the main directories and files:

- **app/:** Contains the source code for the Flask application.
- - **__init__.py:** Initializes the Flask app and sets up routes.
- - **routes.py:** Defines the API routes and their corresponding handlers.
- - **utils.py:** Houses utility functions used across the application.
- - **models.py:** Contains data models used by the application.
- **tests/:** Stores unit tests for the application.
- - **test_routes.py:** Tests for API routes.
- - **test_utils.py:** Tests for utility functions.
- - **test_models.py:** Tests for data models.

## Installation

To run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip install -r requirements.txt.

## Usage

Once installed, you can start the Flask application by running the following command:

``` bash 
flask run
```
This will start the server, and you can access the API endpoints using a tool like Postman or by sending HTTP requests programmatically.

## Testing

Our application comes with a suite of tests to ensure its functionality remains intact. To run the tests, use the following command:

``` bash
python -m unittest
```
This will execute all the tests defined in the tests/ directory and provide feedback on their success or failure.
