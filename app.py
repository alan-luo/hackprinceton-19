from flask import Flask, render_template
from newsapi import NewsApiClient
import math
import datetime
import json

app = Flask(__name__)
newsapi = NewsApiClient(api_key='c25beebd44994e62a96ff204cad8043f')
top_topics = ['impeachment', 'vaping', 'election', 'hong kong']
news_source_stats = {
    "cnn": {'Name': 'CNN', 'Credibility': 0.59, 'Locality': 0.56, 'Writing Quality': 0.42, 'Updatedness': 0.34, 'Sensationalism': 0.48, 'Bias': -74},
    "bbc": {'Name': 'BBC', 'Credibility': 0.90, 'Locality': 0.10, 'Writing Quality': 0.50, 'Updatedness': 0.87, 'Sensationalism': 0.74, 'Bias': 6},
    "spectator": {'Name': 'Spectator', 'Credibility': 0.40, 'Locality': 0.90, 'Writing Quality': 0.88, 'Updatedness': 0.74, 'Sensationalism': 0.72, 'Bias': -84}}


@app.route('/')
def main():
    articles = []
    for topic in top_topics:
        articles.append(get_topic(topic))
    # print(articles)
    return render_template('index.html', articles_list=articles, topics_list=top_topics)

def process_dates(arts):
    articles = arts
    for article in articles:
        article['publishedAt'] = article['publishedAt'][:19]
        mydate = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%S")
        mydelta = datetime.datetime.utcnow()-mydate
        # for now do this in python, in the future want to do this on jinja side
        if mydelta.days == 0:
            hours = math.floor(mydelta.seconds / 3600)
            if hours == 0:
                minutes = math.floor(mydelta.seconds / 60)
                if minutes == 0:
                    article['timesince'] = str(int(mydelta.seconds)) + " second" + ("s" if mydelta.seconds > 1 else "")
                else:
                    article['timesince'] = str(int(minutes)) + " minute" + ("s" if minutes > 1 else "")
            else: 
                article['timesince'] = str(int(hours)) + " hour" + ("s" if hours > 1 else "")
        else: 
            article['timesince'] = str(mydelta.days) + " day" + ("s" if mydelta.days > 1 else "")
        
    return articles

@app.route('/topic/<topic_name>')
def render_topic(topic_name):
    articles = []
    messages = []

    topic_articles = get_topic(topic_name)
    articles.append(topic_articles)
    messages.append("All articles about <b>"+topic_name+"</b>")

    if(topic_name == "impeachment"):
        left_articles = get_topic(topic_name, alignment="left", sort_by="publishedAt")
        articles.append(left_articles)
        messages.append("Views from the left")
        right_articles = get_topic(topic_name, alignment="right", sort_by="publishedAt")
        articles.append(right_articles)
        messages.append("Views from the right")
    if(topic_name == "vaping"):
        articles_1 = get_topic("vaping AND cdc", alignment="left", sort_by="publishedAt")
        articles.append(articles_1)
        messages.append("keyword: <b>cdc</b>")
        articles_2 = get_topic("vaping AND death", alignment="right", sort_by="publishedAt")
        articles.append(articles_2)
        messages.append("keyword: <b>death</b>")
    if(topic_name == "election"):
        articles_1 = get_topic("election AND bernie sanders", alignment="left", sort_by="publishedAt")
        articles.append(articles_1)
        messages.append("keyword: <b>bernie sanders</b>")
        articles_2 = get_topic("election AND donald trump", alignment="right", sort_by="publishedAt")
        articles.append(articles_2)
        messages.append("keyword: <b>donald trump</b>")
    if(topic_name == "hong kong"):
        articles_1 = get_topic("hong kong AND police", alignment="left", sort_by="publishedAt")
        articles.append(articles_1)
        messages.append("keyword: <b>police</b>")
        articles_2 = get_topic("hong kong AND china", alignment="right", sort_by="publishedAt")
        articles.append(articles_2)
        messages.append("keyword: <b>china</b>")
    
        # return render_template('topic.html', topic=topic_name, articles_list=topic_articles, topics_list=top_topics, articles_left=left_articles, articles_right=right_articles)        
    return render_template('topic.html', topic=topic_name, article_lists=articles, message_list = messages)


@app.route('/viz')
def viz():
    return render_template('sourceGraphs.html', topics_list=top_topics)


@app.route('/get_topic/<topic_name>')
def get_topic_view(topic_name):
    return json.dumps(get_topic(topic_name))
def get_topic(topic_name, **kwargs):
    encoded = topic_name.encode("ascii")
    if isinstance(topic_name, str):
        topic_str = topic_name
    else:
        topic_str = encoded


    alignment_list = "cnn,the-new-york-times,bbc-news,the-huffington-post"
    if kwargs.get("alignment") != None:
        if kwargs.get("alignment") == "right":
            alignment_list = "fox-news,the-washington-times,breitbart-news,bloomberg"
        # articles = newsapi.get_everything(q=topic_str, language='en', page_size=20, sources=alignment_list).get('articles')
        # return process_dates(articles)

    articles = newsapi.get_everything(q=topic_str, language='en', page_size=20, 
        sources=alignment_list if kwargs.get("alignment") != None else None,
        sort_by=kwargs.get("sort_by") if kwargs.get("sort_by") != None else None).get('articles')
    return process_dates(articles)
        


@app.route('/view-source-stats/<query>')
def view_news_source_stats(query):
    data = get_news_source_stats(query)
    source_dict = news_source_stats[query]
    name = source_dict.get('Name')
    return render_template('sourceSpiderGraph.html', source_data=data, source=name)


@app.route('/get-source-stats/<query>')
def get_news_source_stats(query):
    return news_source_stats.get(query)


@app.route('/votes/<query>', methods=['GET'])
def get_votes(query):
    return


@app.route('/target-audience/<query>', methods=['GET'])
def get_target_audience(query):
    return


@app.route('/locality/<query>', methods=['GET'])
def get_locality(query):
    return


@app.route('/reporting-topics/<query>', methods=['GET'])
def get_reporting_topics(query):
    return


if __name__ == '__main__':
    app.run()
