import datehelpers
import pandas as pd
import requests

headers = {"User-Agent": "https://github.com/motherofgadgets"}
wiki_endpoints = {
    'top': 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top',
    'article': 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article',
}


def get_top_articles_by_week(project, startdate):
    """
    Get the top 1000 articles ranked by pageview numbers for 7 days following a given start date
    :param project: The wikimedia project
    :param startdate: The start of the week in format YYYYMMDD
    :return: a sorted list of articles
    """
    dates = datehelpers.get_days_of_week(startdate)
    urls = [
        '/'.join([
            wiki_endpoints['top'],
            project,
            'all-access',
            date
        ])
        for date in dates
    ]

    article_data = []
    for url in urls:
        response = requests.get(url=url, headers=headers)
        data = response.json()
        if 'items' in data and len(data['items']) == 1:
            article_data.append(pd.json_normalize(data['items'][0]['articles']))

    # combines all results into single DataFrame
    merged_articles = pd.concat(article_data)

    # Groups articles by 'article' and adds up 'view's
    grouped_articles = merged_articles.groupby('article')['views'].sum().reset_index()

    # Sorts articles by number of views
    ranked_articles = grouped_articles.sort_values('views', ascending=False).reset_index(drop=True)

    # Sets 'rank' value to index
    ranked_articles['rank'] = ranked_articles.index + 1
    return ranked_articles[:1000].to_dict(orient='records')


def get_top_articles_by_month(project, yearmonth):
    """
    Get the top 1000 articles ranked by pageview numbers for a given month
    :param project: The wikimedia project
    :param yearmonth: The given month in format YYYYMM
    :return: a sorted list of articles
    """
    month = datehelpers.get_year_slash_month(yearmonth)
    url = '/'.join([
            wiki_endpoints['top'],
            project,
            'all-access',
            month,
            'all-days'
        ])
    response = requests.get(url=url, headers=headers)

    data = response.json()
    return data


def get_article_views_by_week(project, article, startdate):
    """
    Get the total number of views for a given article for 7 days following a given start date
    :param project: The wikimedia project
    :param article: The name of the article
    :param startdate: The start of the week in format YYYYMMDD
    :return: The total view count
    """
    end_date = datehelpers.get_end_of_week(startdate)

    # Make API call here

    views = 0
    return views


def get_article_views_by_month(project, article, yearmonth):
    """
    Get the total number of views for a given article for a given month
    :param project: The wikimedia project
    :param article: The name of the article
    :param yearmonth: The given month in format YYYYMM
    :return: The total view count
    """
    start_and_end = datehelpers.get_start_slash_end_of_month(yearmonth)

    # Make API call here

    views = 0
    return views


def get_article_top_day_in_month(project, article, yearmonth):
    """
    Get the day in a given month when an article had the most views.
    :param project: The wikimedia project
    :param article: The name of the article
    :param yearmonth: The given month in format YYYYMM
    :return: Article data with the date and number of views
    """
    start_and_end = datehelpers.get_start_slash_end_of_month(yearmonth)

    # Make API call here

    maxday = None
    return maxday
