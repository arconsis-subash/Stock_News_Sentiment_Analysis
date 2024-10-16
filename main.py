import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date


def get_finviz_news(ticker):
    """
    Fetch the latest news for a given stock ticker from finviz.com
    """
    url = f'https://finviz.com/quote.ashx?t={ticker}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_table = soup.find(id='news-table')
    return news_table


def parse_news(news_table):
    """
    Parse the news table and extract relevant information
    """
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


def analyze_sentiment(parsed_news):
    """
    Perform sentiment analysis on the parsed news
    """
    for news in parsed_news:
        analysis = TextBlob(news[2])
        news.append(analysis.sentiment.polarity)
    return parsed_news


def plot_sentiment(df, ticker, avg_sentiment):
    """
    Plot the sentiment analysis results on separate figures
    """
    # Scatter plot of sentiment vs news number
    plt.figure(figsize=(12, 6))
    df['news_num'] = range(1, len(df) + 1)  # Add a news number column
    plt.scatter(df['news_num'], df['sentiment'], alpha=0.6, label='News Sentiment')
    plt.plot(df['news_num'], df['sentiment'], alpha=0.4)  # Adding a line for trend visibility
    plt.axhline(y=avg_sentiment, color='g', linestyle='--', alpha=0.8, label=f'Average Sentiment: {avg_sentiment:.2f}')
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.3, label='Neutral Sentiment')
    plt.title(f'Sentiment Analysis of {ticker} News')
    plt.xlabel('News Number (Chronological Order)')
    plt.ylabel('Sentiment Polarity')
    for i, (news_num, sentiment, title) in enumerate(zip(df['news_num'], df['sentiment'], df['title'])):
        if i % 5 == 0:  # Annotate every 5th point to avoid clutter
            plt.annotate(f"{news_num}", (news_num, sentiment), textcoords="offset points", xytext=(0, 10), ha='center')
    plt.legend()
    plt.show()  # Show the first plot on a separate page

    # Histogram of sentiment distribution
    plt.figure(figsize=(12, 6))
    plt.hist(df['sentiment'], bins=20, edgecolor='black')
    plt.axvline(x=avg_sentiment, color='r', linestyle='--', label=f'Average: {avg_sentiment:.2f}')
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()  # Show the second plot on a separate page

    # Pie chart of positive vs negative sentiments
    plt.figure(figsize=(12, 6))
    positive = (df['sentiment'] > 0).sum()
    negative = (df['sentiment'] < 0).sum()
    neutral = (df['sentiment'] == 0).sum()
    plt.pie([positive, negative, neutral], labels=['Positive', 'Negative', 'Neutral'], autopct='%1.1f%%')
    plt.title('Proportion of Positive vs Negative Sentiments')
    plt.show()  # Show the third plot on a separate page


def main(ticker):
    """
    Main function to run the sentiment analysis
    """
    news_table = get_finviz_news(ticker)
    parsed_news = parse_news(news_table)
    analyzed_news = analyze_sentiment(parsed_news)

    df = pd.DataFrame(analyzed_news, columns=['date', 'time', 'title', 'sentiment'])

    # Calculate average sentiment
    avg_sentiment = df['sentiment'].mean()

    # Plot sentiments including average
    plot_sentiment(df, ticker, avg_sentiment)

    print(df)
    print(f"\nAverage sentiment: {avg_sentiment:.2f}")


if __name__ == "__main__":
    ticker = input("Enter a stock ticker: ")
    main(ticker)