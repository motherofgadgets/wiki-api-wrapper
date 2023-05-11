def get_top_articles_by_week(project, startdate):
    """
    Get the top 1000 articles ranked by pageview numbers for 7 days following a given start date
    :param project: The wikimedia project
    :param startdate: The start of the week in format YYYYMMDD
    :return: a sorted list of articles
    """
    result = []
    return result


def get_top_articles_by_month(project, yearmonth):
    """
    Get the top 1000 articles ranked by pageview numbers for a given month
    :param project: The wikimedia project
    :param yearmonth: The given month in format YYYYMM
    :return: a sorted list of articles
    """
    result = []
    return result


def get_article_views_by_week(project, article, startdate):
    """
    Get the total number of views for a given article for 7 days following a given start date
    :param project: The wikimedia project
    :param article: The name of the article
    :param startdate: The start of the week in format YYYYMMDD
    :return: The total view count
    """
    views = 0
    return views


def get_article_views_by_month(project, article, yearmonth):
    """
    Get the total number of views for a given article for a given month
    :param project: The wikimedia project
    :param article: The name of the article
    :param startdate: The given month in format YYYYMM
    :return: The total view count
    """
    views = 0
    return views


def get_article_top_day_in_month(project, article, yearmonth):
    """
    Get the day in a given month when an article had the most views.
    :param project: The wikimedia project
    :param article: The name of the article
    :param startdate: The given month in format YYYYMM
    :return: Article data with the date and number of views
    """
    maxday = None
    return maxday
