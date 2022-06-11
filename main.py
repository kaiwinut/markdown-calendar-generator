import calendar
import argparse
from datetime import datetime

# Get current year & month as default values
curr_year = datetime.today().year
curr_month = datetime.today().month
DEFAULT_LINK_STYLE = '%Y%m%d'
DEFAULT_LOCALE = 'en_US'
DEFAULT_FORMAT = 'md'

SUPPORTED_LOCALES = ['en_US', 'ja_JP', 'zh_TW']

parser = argparse.ArgumentParser(description='Generates calendar of given month, year in csv format')
parser.add_argument('--year', type=int, default=curr_year, help='Integer specifying the year. Default value is the current year.')
parser.add_argument('--month', type=int, default=curr_month, help='Integer specifying the month. Default value is the current month.')
parser.add_argument('--locale', type=str, default=DEFAULT_LOCALE, help='String specifying the locale. Default value is "en_US". "ja_JP" and "zh_TW" are also available.')
parser.add_argument('--link_style', type=str, default=DEFAULT_LINK_STYLE, help='String specifying the style of the hyperlink. Default value is "%Y%m%d".'.replace(r'%', r'%%'))
parser.add_argument('--format', type=str, default=DEFAULT_FORMAT, help='String specifying the output format. Default value is "md". "csv" is also available.')
parser.add_argument('--start_sunday', default=False, action='store_true', help='Flag that specifys whether a week starts from Sunday.')

args = parser.parse_args()

assert 1 <= args.year <= 99999, '[Error] Invalid year'
assert 1 <= args.month <= 12, '[Error] Invalid month'
assert args.locale in SUPPORTED_LOCALES, '[Error] Locale is not supported'

def linkify(year=args.year, month=args.month, day=1, style=args.link_style):
    return f'[{day}](#{datetime(year, month, day).strftime(style)})'

locale_weekdays = [{'en_US': 'Mon', 'ja_JP': '月', 'zh_TW': '一'},
                   {'en_US': 'Tue', 'ja_JP': '火', 'zh_TW': '二'},
                   {'en_US': 'Wed', 'ja_JP': '水', 'zh_TW': '三'},
                   {'en_US': 'Thu', 'ja_JP': '木', 'zh_TW': '四'},
                   {'en_US': 'Fri', 'ja_JP': '金', 'zh_TW': '五'},
                   {'en_US': 'Sat', 'ja_JP': '土', 'zh_TW': '六'},
                   {'en_US': 'Sun', 'ja_JP': '日', 'zh_TW': '日'},]

def generate_calendar(year=args.year, month=args.month, locale=args.locale, link_style=args.link_style, format=args.format, start_sunday=args.start_sunday):
    weekdays = [locale_weekdays[i][locale] for i in range(6)]
    weekdays = [locale_weekdays[6][locale]] + weekdays if start_sunday else weekdays + [locale_weekdays[6][locale]]

    calendar.setfirstweekday(calendar.SUNDAY if start_sunday else calendar.MONDAY)
    raw_calendar = calendar.monthcalendar(year, month)

    if format == 'csv':
        output = ','.join(weekdays) + '\n' + '\n'.join([','.join([linkify(year=year, month=month, day=d, style=link_style) if d != 0 else '' for d in w]) for w in raw_calendar])

    elif format == 'md':
        full_char = True if locale in ['ja_JP', 'zh_TW'] else False
        width = len(linkify(year=year, month=month, day=10, style=link_style))
        output = ( '| ' + ' | '.join([day.ljust(width if not full_char else width - 1, ' ') for day in weekdays]) + ' |\n' +
                ('| ' + '-' * width + ' ') * 7 + '|\n' + 
                '\n'.join(['| ' + ' | '.join([linkify(year=year, month=month, day=d, style=link_style).ljust(width, ' ') if d != 0 else ''.ljust(width, ' ') for d in w]) + ' |' for w in raw_calendar]))

    return output

if __name__ == '__main__':
    print(generate_calendar())