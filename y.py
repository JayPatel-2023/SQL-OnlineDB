import subprocess

# Specify the path to your PHP file
php_file_path = "path/to/your/example.php"

# Run the PHP script and capture the output
result = subprocess.run(["php", php_file_path], capture_output=True, text=True)

# Print the output from the PHP script
print("Output from PHP:", result.stdout)
