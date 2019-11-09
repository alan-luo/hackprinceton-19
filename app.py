from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='466f16c5dc2445eabe6a30991514a281')


@app.route('/')
def main():
    articles = []
    top_topics = ['Impeachment', 'Vaping', 'Election', 'Hong Kong']
    for topic in top_topics:
        articles.append(get_topic(topic))
    print(articles)
    return render_template('index.html', articles_list=articles, topics_list=top_topics)


@app.route('/topic_page/<topic_name>')
def render_topic(topic_name):
    topic_articles = get_topic(topic_name)
    return render_template('topic.html', topic=topic_name, articles_list=topic_articles)


@app.route('/viz')
def viz():
    return render_template('sourceGraphs.html')


@app.route('/topic/<topic_name>')
def get_topic(topic_name):
    return newsapi.get_top_headlines(q=topic_name, language='en', page_size=1).get('articles')


@app.route('/news-source-stats/<query>', methods=['GET'])
def get_news_source_stats(query):
    return


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
