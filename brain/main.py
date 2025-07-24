from finviz_scrapper import get_finviz_news
from parser import parse_news
from sentiment import analyze_sentiment
from plotter import plot_sentiment
import pandas as pd

def main(ticker):
    news_table = get_finviz_news(ticker)
    parsed_news = parse_news(news_table)
    analyzed_news = analyze_sentiment(parsed_news)

    df = pd.DataFrame(analyzed_news, columns=['date', 'time', 'title', 'sentiment'])
    avg_sentiment = df['sentiment'].mean()

    plot_sentiment(df, ticker, avg_sentiment)

    print(df)
    print(f"\nAverage sentiment: {avg_sentiment:.2f}")

if __name__ == "__main__":
    ticker = input("Enter a stock ticker: ")
    main(ticker)
