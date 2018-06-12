import bottle as b
import json
import feedparser
import random
from datetime import datetime


@b.get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return b.static_file(filename, root='js')


@b.get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return b.static_file(filename, root='css')


@b.get('/getNews')
def retrieve_news():
    feed = feedparser.parse("http://www.fifa.com/rss/index.xml")
    articles = []
    art_indexes = []
    i=0
    while i<10:
        num = random.randint(0, len(feed["entries"]) - 1)
        if num not in art_indexes:
            art_indexes.append(num)
            i+=1
    for i in art_indexes:
        article = {}
        article["title"] = feed["entries"][i]["title"]
        article["link"] = feed["entries"][i]["links"][0]["href"]
        articles.append(article)
    last_time = b.request.get_cookie("invoked_at", str(datetime.now()))
    b.response.set_cookie("invoked_at", str(datetime.now()), max_age=30)
    return json.dumps([articles, last_time])

@b.get("/")
def serve_html():
    return b.template("soccer_news.html")


def main():
    b.run(host='localhost', port=7007)


if __name__ == '__main__':
    main()
