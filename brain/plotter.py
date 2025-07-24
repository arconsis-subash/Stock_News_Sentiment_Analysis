import matplotlib.pyplot as plt

def plot_sentiment(df, ticker, avg_sentiment):
    # Scatter plot
    plt.figure(figsize=(12, 6))
    df['news_num'] = range(1, len(df) + 1)
    plt.scatter(df['news_num'], df['sentiment'], alpha=0.6, label='News Sentiment')
    plt.plot(df['news_num'], df['sentiment'], alpha=0.4)
    plt.axhline(y=avg_sentiment, color='g', linestyle='--', label=f'Avg: {avg_sentiment:.2f}')
    plt.axhline(y=0, color='r', linestyle='--', label='Neutral')
    plt.title(f'Sentiment Analysis of {ticker} News')
    plt.xlabel('News Number')
    plt.ylabel('Sentiment Polarity')
    for i, (news_num, sentiment, title) in enumerate(zip(df['news_num'], df['sentiment'], df['title'])):
        if i % 5 == 0:
            plt.annotate(f"{news_num}", (news_num, sentiment), textcoords="offset points", xytext=(0, 10), ha='center')
    plt.legend()
    plt.show()

    # Histogram
    plt.figure(figsize=(12, 6))
    plt.hist(df['sentiment'], bins=20, edgecolor='black')
    plt.axvline(x=avg_sentiment, color='r', linestyle='--', label=f'Average: {avg_sentiment:.2f}')
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # Pie chart
    plt.figure(figsize=(12, 6))
    positive = (df['sentiment'] > 0).sum()
    negative = (df['sentiment'] < 0).sum()
    neutral = (df['sentiment'] == 0).sum()
    plt.pie([positive, negative, neutral], labels=['Positive', 'Negative', 'Neutral'], autopct='%1.1f%%')
    plt.title('Proportion of Sentiments')
    plt.show()
