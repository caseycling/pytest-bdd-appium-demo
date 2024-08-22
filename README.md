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

`python_version==3.12`
`pytest-bdd`
`pytest`
`appium-python-client==4.1.0`
`selenium`
`pytest-xdist`

Then, install the dependencies using:

`pip install -r requirements.txt`


## Sauce Documentation & Resources 📚
- `User Credentials Environment Variables` Using Sauce user credential environment variables in your app [User Cred Environment Variables](https://docs.saucelabs.com/secure-connections/sauce-connect/setup-configuration/environment-variables/#user-credentials-environment-variables)
- `Platform Configurator` Tool developed by Sauce Labs to help you correctly configure test capabilities for your Appium and Selenium tests. [Platform Configurator](https://saucelabs.com/products/platform-configurator#/)
- `SauceLabs Blog` Test automation tutorials, guides, learnings, and insights [Sauce Blog](https://saucelabs.com/resources/blog)
