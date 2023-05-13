import calendar
from datetime import datetime, timedelta


def get_days_of_week(startdate):
    """
    Gets list of 7 days from given start date
    :param startdate: The start of the week in format YYYYMMDD
    :return: A list of date strings in YYYY/MM/DD format
    """
    yesterday = datetime.today() - timedelta(days=1)
    parsed_date = datetime.strptime(startdate, '%Y%m%d')
    dates = []
    for day in range(7):
        weekday = parsed_date + timedelta(days=day)
        if weekday.date() <= yesterday.date():
            dates.append(weekday.strftime('%Y/%m/%d'))
    return dates


def get_year_slash_month(yearmonth):
    """
    Parses YYYYMM string to get YYYY/MM
    :param yearmonth: The given month in format YYYYMM
    :return: The given month in format YYYY/MM
    """
    parsed_date = datetime.strptime(yearmonth, '%Y%m')
    return parsed_date.strftime('%Y/%m')


def get_end_of_week(startdate):
    """
    Get a string representing a date 7 days later than given start date
    :param startdate: The start of the week in format YYYYMMDD
    :return: The end of the week in format YYYYMMDD
    """
    parsed_date = datetime.strptime(startdate, '%Y%m%d')
    end_date = parsed_date + timedelta(days=6)
    return end_date.strftime('%Y%m%d')


def get_end_of_month(yearmonth):
    """
    Get a string representing the last date in the given month
    :param yearmonth: The given month in format YYYYMM
    :return: The end of the month in format YYYYMMDD
    """
    month = datetime.strptime(yearmonth, '%Y%m')
    month_range = calendar.monthrange(month.year, month.month)

    return "{month}{end}".format(month=yearmonth, end=month_range[1])
