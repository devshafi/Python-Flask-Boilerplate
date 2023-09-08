# 🐍 Python Fullstack Boilerplate 🐍

This is a simple python boilerplate that includes a bare minimum backend and front-end page. There are only two files that run the application.
- app.py
- templates/index.html

### app.py
This file contains code to create the API's and run the server.

### templates/index.html
This file contains code to render the view

## Prepare Environment
Please make sure python is installed in your system. We recommend the latest version of Python (3.10 or above). 
After installing Python,

1. Navigate to the root directory of your project like this:

    ```bash
    cd /path/to/my_project
    ```
2. Create the Virtual Environment: Run the following command to create a virtual environment:

    ```bash
    python -m venv venv
    ```
    - The first python is the Python interpreter you want to use. You may need to use python3 instead if you have both Python 2 and Python 3 installed.
    - venv is the module for creating virtual environments.
    - The second venv is the name of the directory where the virtual environment will be created. You can choose any name you like.

3. Activate the Virtual Environment:

    - Windows:
        ```bash
        source venv\Scripts\activate
        ```
    - macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

When the virtual environment is activated, you will see its name in your command prompt or terminal, indicating that you are now working within the virtual environment.

5. Install Dependencies: You can now use pip to install Python packages within the virtual environment. For example:

    ```bash
    pip install package_name
    ```
6. Deactivate the Virtual Environment: To exit the virtual environment when you're done, simply run the deactivate command:

    ```bash
    deactivate
    ```

## Run Application:
To run the application, run the following command from the root of the application:
```bash
python app.py
```



