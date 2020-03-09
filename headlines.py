import feedparser
from flask import Flask
app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/england/london/rss.xml"

@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    html = "<html>"
    html += "<body>"
    html += "<h1>BBC Headlines</h1>"
    for article in feed['entries']:
        html += """<b>{0}</b> </br>
                    <i>{1}</i> </br>
                    <p>{2}</p> </br>""".format(
            article.get("title"),
            article.get("published"),
            article.get('summary'))
    html += "</body>"
    html += "</html>"

    return html

if __name__ == "__main__":
    app.run(port=5000, debug=True)