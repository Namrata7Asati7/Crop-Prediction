from app import app
from urllib.parse import quote as url_quote


app = app()

if __name__ == '__main__':
    app.run(debug=True)