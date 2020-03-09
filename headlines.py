import feedparser
from flask import Flask
app = Flask(__name__)
RSS_FEED = {'bbc'   : 'http://feeds.bbci.co.uk/news/england/london/rss.xml',
            'lenta' : 'http://lenta.ru/rss/news' }

def get_news(source):
    feed = feedparser.parse(RSS_FEED[source])
    articles = feed['entries']
    html = "<html><body>"
    html += "<h1>{} Headlines</h1>".format(source)
    for article in articles:
       html += """ 
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
            """.format(article.get("title"),
                       article.get("published"),
                       article.get("summary"))
    html += "</body></html>"
    return html

@app.route("/")
@app.route("/bbc")
def get_bbc():
    return get_news('bbc')

@app.route("/lenta")
def get_lenta():
    return get_news('lenta')

if __name__ == "__main__":
    app.run(port=5000, debug=True)