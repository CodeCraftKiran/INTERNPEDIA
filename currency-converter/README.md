**Currency Converter Application Documentation**

This is a simple Flask web application that allows users to convert currency from one code to another using the Free Currency API.

**Requirements:**

- Python 3.x
- Flask
- Requests

**Installation:**

1. Clone the repository or download the source code files.

2. Install Python 3.x if you haven't already. You can download it from the official Python website: [Python Official Website](https://www.python.org/downloads/)

3. Install Flask and Requests libraries using pip:

   ```bash
   pip install Flask requests
   ```

**Configuration:**

Before running the application, make sure to set up your API key for the Free Currency API. You can obtain an API key by signing up on the Free Currency API website: [Free Currency API](https://freecurrencyapi.com/)

Set your API key as an environment variable named `APIKEY`. 
or just replace 

"apikey = os.environ.get('APIKEY')"
```bash
apikey="Your-API-Key"
```
**Running the Application:**

1. Navigate where the `main.py` file is located.

2. Run the Flask application. 

3. click on local host link `* Running on http://127.0.0.1:5000` to access the application.

**Usage:**

- Choose the base currency from the dropdown menu labeled "Base Currency".
- Enter the amount you want to convert in the "Amount to be converted" field.
- Select the target currency from the dropdown menu labeled "Target Currency".
- Click on the "Convert" button.
- The converted amount will be displayed on the page.

If you enter an invalid amount (non-numeric), an error message will be displayed prompting you to enter the amount in numbers.

**Notes:**

- This application requires an active internet connection to fetch currency conversion rates from the Free Currency API.
- Ensure that your API key is properly configured as an environment variable before running the application.

That's it! You now have a simple currency converter web application up and running.
