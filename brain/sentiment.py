from textblob import TextBlob

def analyze_sentiment(parsed_news):
    for news in parsed_news:
        analysis = TextBlob(news[2])
        news.append(analysis.sentiment.polarity)
    return parsed_news
