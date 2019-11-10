from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='466f16c5dc2445eabe6a30991514a281')
top_topics = ['Impeachment', 'Vape', 'Election', 'Hong Kong']
news_source_stats = {
    "CNN": {'Credibility': 0.59, 'Locality': 0.56, 'Liberal Bias': 0.42, 'Updatedness': 0.34, 'Sensationalism': 0.48},
    "BBC": {'Credibility': 0.90, 'Locality': 0.10, 'Liberal Bias': 0.50, 'Updatedness': 0.87, 'Sensationalism': 0.74},
    "Spectator": {'Credibility': 0.40, 'Locality': 0.90, 'Liberal Bias': 0.88, 'Updatedness': 0.74, 'Sensationalism': 0.72}}


@app.route('/')
def main():
    articles = []
    for topic in top_topics:
        articles.append(get_topic(topic))
    # print(articles)
    return render_template('index.html', articles_list=articles, topics_list=top_topics)


@app.route('/topic/<topic_name>')
def render_topic(topic_name):
    topic_articles = get_topic(topic_name)
    return render_template('topic.html', topic=topic_name, articles_list=topic_articles, topics_list=top_topics)


@app.route('/viz')
def viz():
    return render_template('sourceGraphs.html', topics_list=top_topics)


@app.route('/get_topic/<topic_name>')
def get_topic(topic_name):
    encoded = topic_name.encode("ascii")
    if isinstance(topic_name, str):
        topic_str = topic_name
    else:
        topic_str = encoded
    myobj = newsapi.get_everything(q=topic_str, language='en', page_size=20).get('articles')
    return myobj


@app.route('/view-source-stats/<query>')
def view_news_source_stats(query):
    data = get_news_source_stats(query)
    return render_template('sourceSpiderGraph.html', source_data=data, source=query)


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
