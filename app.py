from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='466f16c5dc2445eabe6a30991514a281')


@app.route('/')
def main():
    articles = []
    impeachment_articles = newsapi.get_top_headlines(q='impeachment', language='en',
                                                     page_size=1).get('articles')
    vaping_articles = newsapi.get_top_headlines(q='politics', language='en', page_size=1).get('articles')
    election_articles = newsapi.get_top_headlines(q='election', language='en', page_size=1).get('articles')
    hong_kong_articles = newsapi.get_top_headlines(q='hong kong', language='en', page_size=1).get('articles')
    articles.append(impeachment_articles)
    articles.append(vaping_articles)
    articles.append(election_articles)
    articles.append(hong_kong_articles)
    print(articles)
    return render_template('index.html', articles_list=articles)


@app.route('/news-source-stats<query>', methods=['GET'])
def get_news_source_stats(query):
    return


@app.route('/votes<query>', methods=['GET'])
def get_votes(query):
    return


@app.route('/target-audience<query>', methods=['GET'])
def get_target_audience(query):
    return


@app.route('/locality<query>', methods=['GET'])
def get_locality(query):
    return


@app.route('/reporting-topics<query>', methods=['GET'])
def get_reporting_topics(query):
    return


if __name__ == '__main__':
    app.run()
