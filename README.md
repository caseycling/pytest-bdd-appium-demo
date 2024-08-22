# Project Overview
This is an example repo of mobile-web tests and native mobile app tests for Android and iOs using Python with pytest-BDD and Appium via a sauce labs account on [Sauce Labs](https://saucelabs.com/) infrastructure through [SauceDemo.com](https://www.saucedemo.com/).

# Getting Started
1. Clone the repository `git clone https://github.com/caseycling/pytest-bdd-appium-demo.git`
2. Go to into the repository `cd pytest-bdd-appium-demo`
3. Install the dependencies `pipenv install`

## Installation:

Ensure you have Python 3.12 installed. You can download it from the [official Python website](https://www.python.org/downloads/)

## Instructions on setting up environment variables
If you have these saved as "environment variables" on your local machine, utilizing the logic in our project will work. Alternatively, you can create a .env file and store them there:

```
SAUCE_USERNAME=your_sauce_username
SAUCE_ACCESS_KEY=your_sauce_access_key
````

# Directory Structure

- **`features/`**: Contains your BDD feature files, written in Gherkin syntax. These files define the behavior of the application in a more readable format.

- **`tests/`**:
  - **`mobile-web/`**: Includes test files specific to mobile web testing.
  - **`native-app/`**:
    - **`android/`**: Contains tests and step definitions specific to Android native apps.
    - **`iOS/`**: Contains tests and step definitions specific to iOS native apps.

## Driver Setup in `conftest.py`

The conftest.py file in this project is configured to manage the setup and teardown of WebDriver sessions for different platforms, ensuring that the tests run smoothly on Sauce Labs infrastructure. Here's an overview of the drivers set up:

**1. Mobile Web Driver**

The mobile_web_driver fixture sets up the WebDriver session for running mobile web tests. It uses Selenium's webdriver.Remote to interact with a mobile web browser hosted on Sauce Labs.

**2. Android RDC Driver**

The android_rdc_driver fixture sets up a session for running tests on native Android applications using Appium. It leverages Appium's UiAutomator2Options to interact with the Android device.

**3. iOS RDC Driver**

The ios_driver fixture manages the setup for running tests on native iOS applications. It uses Appium's AppiumOptions to configure the session.

**General workflow:**

Each driver fixture yields a WebDriver session, allowing the test to interact with the respective platform. 
After the test execution, the driver session is terminated (driver.quit()), ensuring that resources are released properly. 

For more information on how to customize these settings to accomodate your usecase, please reference the platform configurator documenation listed at the bottom of this doc.

### Parallel Execution with `pytest-bdd`

- **Pytest-Xdist Integration**: `pytest-bdd` works with `pytest-xdist` to run tests in parallel. The `pytest-xdist` plugin distributes test execution across multiple CPUs or machines, improving performance for large test suites.

- **Running Tests**: When `pytest` is executed with the `-n` option (e.g., `pytest -n auto`), `pytest-xdist` automatically runs tests in parallel. It recognizes the test files and steps definitions across the `tests/` directories and handles parallel execution efficiently.

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
