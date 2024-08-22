# Project Overview
This is an example repo of mobile-web tests and native mobile app tests for Android and iOs using Python with pytest-BDD and Appium via a sauce labs account on [Sauce Labs](https://saucelabs.com/) infrastructure through [SauceDemo.com](https://www.saucedemo.com/).

# Getting Started
1. Clone the repository from github `[https://github.com/caseycling/pytest-bdd-appium-demo.git`
2. Go to into the repository `cd pytest-bdd-appium-demo`

## Installation:

Ensure you have Python 3.12 installed. You can download it from the [official Python website](https://www.python.org/downloads/)

## Create a virtual environment(optional but recommended):

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

To install individual packages instead of using .txt file, simply use:

`pip install pytest-xdist` or `pip install pytest` etc...

Verify the installation of packages (optional):

`pip list`


## Instructions on setting up environment variables
If you have these saved as "environment variables" on your local machine, utilizing the logic in our project will work. If not, you can create a .env file and store them there also.

`$SAUCE_USERNAME`
`$SAUCE_ACCESS_KEY`

## Method 1: Setting Environment Variables Directly
On Windows:

Open the Start menu and search for "Environment Variables."
Select "Edit the system environment variables."
In the System Properties window, click "Environment Variables."
In the Environment Variables window, click "New" under "User variables" or "System variables."
Add the variable name (`SAUCE_USERNAME` and `SAUCE_ACCESS_KEY`) and value.
Click OK to save and close all windows.

On macOS/Linux:
Open a terminal.

Edit your shell profile file (~/.bashrc, ~/.bash_profile, or ~/.zshrc (i.e. vim .zshrc) depending on your shell).

Add the following lines:

```
export SAUCE_USERNAME="your_sauce_username"
export SAUCE_ACCESS_KEY="your_sauce_access_key"
```
Save the file and run source ~/.bashrc (or the appropriate file) to apply the changes.


## Method 2: Using a .env File
Create a .env file:

In your project directory, create a file named `.env`

Open the .env file and add the following lines:

```
SAUCE_USERNAME=your_sauce_username
SAUCE_ACCESS_KEY=your_sauce_access_key
```
Load/reload the .env file.

Install the python-dotenv package if it's not already installed:

`pip install python-dotenv`

In your Python code, load the environment variables at the start of your script or configuration file:
```
from dotenv import load_dotenv
import os

load_dotenv()

sauce_username = os.getenv('SAUCE_USERNAME')
sauce_access_key = os.getenv('SAUCE_ACCESS_KEY')
```
This method ensures that sensitive information is kept separate from your code and is easier to manage across different environments.

--Tips:
Ensure your .env file is added to .gitignore to prevent it from being committed to version control.
Use environment variables to keep sensitive information secure and configurable without modifying your codebase.

#Certainly! Here’s a brief explanation of the directory structure and how `pytest-bdd` operates with it:

# Directory Structure

- **`features/`**: Contains your BDD feature files, written in Gherkin syntax. These files define the behavior of the application in a more readable format.

- **`tests/`**:
  - **`mobile-web/`**: Includes test files specific to mobile web testing.
  - **`native-app/`**:
    - **`android/`**: Contains tests and step definitions specific to Android native apps.
    - **`iOS/`**: Contains tests and step definitions specific to iOS native apps.

### How `pytest-bdd` Runs in Parallel

1. **Feature Files**: Located in the `features/` directory, these files describe scenarios and steps that need to be tested.

2. **Step Definitions**: These are Python functions that implement the steps described in the feature files. They are usually placed in the corresponding test directories under `tests/`, such as `mobile-web/`, `native-app/android/`, and `native-app/iOS/`.

3. **Test Files**: These files include the test logic and use the step definitions to execute the scenarios. They are found in the same directories as step definitions or in a subdirectory as needed.

### Parallel Execution with `pytest-bdd`

- **Pytest-Xdist Integration**: `pytest-bdd` works with `pytest-xdist` to run tests in parallel. The `pytest-xdist` plugin distributes test execution across multiple CPUs or machines, improving performance for large test suites.

- **Running Tests**: When `pytest` is executed with the `-n` option (e.g., `pytest -n auto`), `pytest-xdist` automatically runs tests in parallel. It recognizes the test files and steps definitions across the `tests/` directories and handles parallel execution efficiently.

This structure ensures a clean separation between different types of tests and platforms while enabling parallel test execution to optimize testing efficiency.

# Running the Tests

You can start individual non parallel tests by using .ex `pipenv run pytest tests/mobile-web/test_add_item_to_cart.py`

or you can use the provided "parallel" [scripts] found in the Pipfile:

```
mobile-web = "pipenv run pytest -n5 tests/mobile-web"
native-app = "pipenv run pytest -n8 tests/native-app"
native-app-android = "pipenv run pytest tests/native-app/android"
native-app-iOs = "pipenv run pytest -n3 tests/native-app/iOS"
```



# Sauce Documentation & Resources 📚
- `User Credentials Environment Variables` Using Sauce user credential environment variables in your app [User Cred Environment Variables](https://docs.saucelabs.com/secure-connections/sauce-connect/setup-configuration/environment-variables/#user-credentials-environment-variables)
- `Platform Configurator` Tool developed by Sauce Labs to help you correctly configure test capabilities for your Appium and Selenium tests. [Platform Configurator](https://saucelabs.com/products/platform-configurator#/)
- `SauceLabs Blog` Test automation tutorials, guides, learnings, and insights [Sauce Blog](https://saucelabs.com/resources/blog)
