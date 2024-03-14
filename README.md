Book Scraper

This Flask application scrapes book attributes from the website "http://books.toscrape.com" and stores them in a MySQL database.

Installation
1. Clone the repository to your local machine:
    git clone <repository_url>
2. Install the required dependencies:
    pip install Flask requests mysql-connector-python beautifulsoup4
3. Set up the MySQL database by creating a database and table named books. Update the 'config/db_config.py' file with your MySQL database connection details.

4. Run the Flask application:
  python app.py
Usage
Once the Flask application is running, you can access the following endpoints:

>> '/': Returns a message indicating that the server is running.

>> '/scrap': Initiates the scraping process. The application scrapes book attributes from all 50 pages of "http://books.toscrape.com/catalogue/" and stores them in the MySQL database.

Dependencies
 Flask: A lightweight web framework for Python.
 
 requests: A library for making HTTP requests.
 
 mysql-connector-python: A connector library for MySQL databases.
 
 beautifulsoup4: A library for web scraping.
Contributors
Pintu Kumar
License
This project is licensed under the MIT License - see the LICENSE file for details.
