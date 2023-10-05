
'''import requests

# Replace this with the URL of your PHP file on GitHub
github_php_url = "https://github1s.com/JayPatel-2023/SQL-OnlineDB/blob/main/y.php"

# Make an HTTP request to the PHP file
response = requests.get(github_php_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content returned by the PHP file
    print("Output from PHP:", response.text)
else:
    print(f"Error: {response.status_code}")
'''
import requests

# Replace this with the URL of your modified PHP file on GitHub
github_php_url = "https://github.com/JayPatel-2023/SQL-OnlineDB/blob/main/y.php"

# Specify the function to call
function_name = "getData"

# Make an HTTP request to the PHP file with the function parameter
response = requests.get(github_php_url, params={"function": function_name})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    print("Result from PHP function:", result)
else:
    print(f"Error: {response.status_code}")

'''
import requests
import json

# Replace this with the URL of your modified PHP file on GitHub
github_php_url = "https://github.com/JayPatel-2023/SQL-OnlineDB/blob/main/y.php"

# Specify the function to call
function_name = "getData"

# Make an HTTP request to the PHP file with the function parameter
response = requests.get(github_php_url, params={"function": function_name})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()

    # Print the specific data from the function
    if 'message' in result:
        print(result['message'])
    else:
        print("Unexpected JSON format")
else:
    print(f"Error: {response.status_code}")
'''