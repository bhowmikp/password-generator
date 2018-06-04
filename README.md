[![Build Status](https://travis-ci.org/bhowmikp/password-generator.svg?branch=master)](https://travis-ci.org/bhowmikp/password-generator)[![Coverage Status](https://coveralls.io/repos/github/bhowmikp/password-generator/badge.svg?branch=master)](https://coveralls.io/github/bhowmikp/password-generator?branch=master)

# Password Generator

Generates a password for the user once provided name of website and username. Stores the password in a .txt file, containing all the user's information and the randomly generated password.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
sh install.sh
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Testing exists for the backend of the application which is located in password_generator.py. No testing exists for the gui portion of the application.

In the folder of the app. Enter the command
```
pip3 install pytest pytest-cov
pytest
```

### And coding style tests

Pylint is used for the coding style.

In the folder of the app. Enter the command (replace the filename with the name of the file to be tested)
```
pip3 install pylint
pylint [filename].py
```

## Deployment

```
python3 password_generator_gui.py
```

## Authors

* **Prantar Bhowmik** - *Initial work* - [bhowmikp](https://github.com/bhowmikp)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
