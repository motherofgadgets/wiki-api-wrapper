import datehelpers
import pandas as pd
import requests
import exceptions

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
    try:
        dates = datehelpers.get_days_of_week(startdate)
    except ValueError:
        raise exceptions.BadRequest(startdate)

    if not dates:
        raise exceptions.MyDataNotFound(startdate)

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
        if response.status_code == 200:
            if 'items' in data and len(data['items']) == 1:
                article_data.append(pd.json_normalize(data['items'][0]['articles']))
        else:
            return data, response.status_code

    # combines all results into single DataFrame
    merged_articles = pd.concat(article_data)

    # Groups articles by 'article' and adds up 'view's
    grouped_articles = merged_articles.groupby('article')['views'].sum().reset_index()

    # Sorts articles by number of views
    ranked_articles = grouped_articles.sort_values('views', ascending=False).reset_index(drop=True)

    # Sets 'rank' value to index
    ranked_articles['rank'] = ranked_articles.index + 1

    response_dict = {
        "items": [
            {
                "articles": ranked_articles[:1000].to_dict(orient='records'),
                "project": project,
                "access": "all-access",
                "timestamp_start": startdate + "00",
                "timestamp_end": datehelpers.get_end_of_week(startdate) + "00",
            }
        ],
    }
    return response_dict


def get_top_articles_by_month(project, yearmonth):
    """
    Get the top 1000 articles ranked by pageview numbers for a given month
    :param project: The wikimedia project
    :param yearmonth: The given month in format YYYYMM
    :return: a sorted list of articles
    """
    try:
        month = datehelpers.get_year_slash_month(yearmonth)
    except ValueError:
        raise exceptions.BadRequest(yearmonth)

    url = '/'.join([
            wiki_endpoints['top'],
            project,
            'all-access',
            month,
            'all-days'
        ])
    response = requests.get(url=url, headers=headers)

    data = response.json()
    if response.status_code == 200:
        response_dict = {
            "items": [
                {
                    "articles": data['items'][0]["articles"],
                    "project": project,
                    "access": "all-access",
                    "timestamp_start": yearmonth + "0100",
                    "timestamp_end": datehelpers.get_end_of_month(yearmonth) + "00",
                }
            ],
        }
        return response_dict
    else:
        return data, response.status_code


def get_article_views_by_week(project, article, startdate):
    """
    Get the total number of views for a given article for 7 days following a given start date
    :param project: The wikimedia project
    :param article: The name of the article
    :param startdate: The start of the week in format YYYYMMDD
    :return: The total view count
    """
    try:
        enddate = datehelpers.get_end_of_week(startdate)
    except ValueError:
        raise exceptions.BadRequest(startdate)

    url = '/'.join([
        wiki_endpoints['article'],
        project,
        'all-access',
        'all-agents',
        article,
        'daily',
        startdate,
        enddate
    ])
    total_views = 0
    response = requests.get(url=url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        if 'items' in data:
            for day in data['items']:
                total_views += day['views']

        response_dict = {
              "access": "all-access",
              "agent": "all-agents",
              "article": article,
              "granularity": "daily",
              "project": project,
              "timestamp_start": startdate + "00",
              "timestamp_end": enddate + "00",
              "views": total_views
            }

        return response_dict
    else:
        return data, response.status_code


def get_article_views_by_month(project, article, yearmonth):
    """
    Get the total number of views for a given article for a given month
    :param project: The wikimedia project
    :param article: The name of the article
    :param yearmonth: The given month in format YYYYMM
    :return: The total view count
    """
    try:
        monthend = datehelpers.get_end_of_month(yearmonth)
    except ValueError:
        raise exceptions.BadRequest(yearmonth)

    url = '/'.join([
        wiki_endpoints['article'],
        project,
        'all-access',
        'all-agents',
        article,
        'monthly',
        yearmonth + "01",
        monthend
    ])
    response = requests.get(url=url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        response_dict = {
            "access": "all-access",
            "agent": "all-agents",
            "article": article,
            "granularity": "daily",
            "project": project,
            "timestamp_start": yearmonth + "0100",
            "timestamp_end": monthend + "00",
            "views": data["items"][0]["views"]
        }
        return response_dict
    else:
        return data, response.status_code


def get_article_top_day_in_month(project, article, yearmonth):
    """
    Get the day in a given month when an article had the most views.
    :param project: The wikimedia project
    :param article: The name of the article
    :param yearmonth: The given month in format YYYYMM
    :return: Article data with the date and number of views
    """
    try:
        monthend = datehelpers.get_end_of_month(yearmonth)
    except ValueError:
        raise exceptions.BadRequest(yearmonth)
    url = '/'.join([
        wiki_endpoints['article'],
        project,
        'all-access',
        'all-agents',
        article,
        'daily',
        yearmonth + "01",
        monthend
    ])
    response = requests.get(url=url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        return max(data['items'], key=lambda ev: ev['views'])
    else:
        return data, response.status_code
