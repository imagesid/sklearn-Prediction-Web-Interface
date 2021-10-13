# sklearn-Prediction-Web-Interface
Simple script to help you to bridge sklearn prediction with another software such PHP and javascript etc. It uses TCP request.
There are two files in here, serve-web.py is python script to serve TCP port 8080 and after that the model can be used by another interface such PHP, Javascript, CURL, etc. File example-client.php is an example to connect into your sklearn model.

# How to use:
1. Upload file serve-web.py into your server
2. Don't forget to install sklearn: pip install sklearn
3. Run the file: python server-web.py
4. Upload file example-client.php into your web server
5. Edit IP address in this file and it should be matched with python server
6. Done. You can check this file via your web browser

Notes:

If you have a firewall in your system, please allow port 8080.

In this file, I implemented Linear Regression model of sklearn. You can implement another model into this script.

Please let me know if you have any questions
