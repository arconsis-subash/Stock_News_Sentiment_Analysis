from datetime import date

def parse_news(news_table):
    parsed_news = []
    current_date = None
    for row in news_table.findAll('tr'):
        title = row.a.text
        date_data = row.td.text.split(' ')

        if len(date_data) == 1:
            time = date_data[0]
        else:
            current_date = date_data[0]
            time = date_data[1]

        if current_date is None:
            current_date = date.today().strftime("%b-%d-%y")

        parsed_news.append([current_date, time, title])
    return parsed_news
