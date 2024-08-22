## Getting Started
1. Clone the repository fro github `[https://github.com/caseycling/pytest-bdd-appium-demo.git`
2. Go to into the repository `cd pytest-bdd-appium-demo`

## Installation:

Ensure you have Python 3.12 installed. You can download it from the [official Python website](https://www.python.org/downloads/)

## Create a virtual environment:

`python -m venv venv`

On Windows:
`venv\Scripts\activate`

On macOS/Linux:
`source venv/bin/activate`

## Install the required packages:

Create a requirements.txt file with the following content:

``` 
python_version==3.12
pytest
pytest-bdd
pytest-xdist
appium-python-client==4.1.0
selenium
```

Then, install the dependencies using:

`pip install -r requirements.txt`

To install individual packages needed simply use:

`pip install pytest-xdist` or `pip install pytest`

## Running the Tests

You can start individual non parallel tests by using .ex `pipenv run pytest tests/mobile-web/test_add_item_to_cart.py`

or you can use the parallel [scripts] found in the Pipfile:

```
mobile-web = "pipenv run pytest -n5 tests/mobile-web"
native-app = "pipenv run pytest -n8 tests/native-app"
native-app-android = "pipenv run pytest tests/native-app/android"
native-app-iOs = "pipenv run pytest -n3 tests/native-app/iOS"
```



## Sauce Documentation & Resources 📚
- `User Credentials Environment Variables` Using Sauce user credential environment variables in your app [User Cred Environment Variables](https://docs.saucelabs.com/secure-connections/sauce-connect/setup-configuration/environment-variables/#user-credentials-environment-variables)
- `Platform Configurator` Tool developed by Sauce Labs to help you correctly configure test capabilities for your Appium and Selenium tests. [Platform Configurator](https://saucelabs.com/products/platform-configurator#/)
- `SauceLabs Blog` Test automation tutorials, guides, learnings, and insights [Sauce Blog](https://saucelabs.com/resources/blog)
