from flask import Flask, jsonify
import requests
import config.db_config as db
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server():
    return "Server is running"

def scrape_and_store_books(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            # print(book)
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            rating = ' '.join(book.find('p', class_='star-rating')['class'][1:])
            
            # Insert book attributes into database
            sql = "INSERT IGNORE INTO books (title, price, availability, rating) VALUES (%s, %s, %s, %s)"
            values = (title, price, availability, rating)
            db.cursor.execute(sql, values)
        
        db.connection.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/scrape', methods=['GET'])
def scrap_books():
    try:
        for page_num in range(1, 51):
            url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
            scrape_and_store_books(url)
        
        # Close cursor and connection
        db.cursor.close()
        db.connection.close()
        
        return jsonify({'message': 'Books scraped and stored successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True)
