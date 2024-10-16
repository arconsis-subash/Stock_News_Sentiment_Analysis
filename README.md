# Stock News Sentiment Analysis

## Overview
The Stock News Sentiment Analysis project aims to extract and analyze sentiment from news articles related to specific stock tickers. By leveraging web scraping, natural language processing, and data visualization techniques, this project provides insights that help investors make informed decisions based on real-time market sentiment.



## Features
- **Real-time News Scraping**: Fetches the latest news articles for specified stock tickers from [finviz.com](https://finviz.com).
- **Sentiment Analysis**: Analyzes the sentiment of news articles using TextBlob to derive sentiment scores.
- **Data Visualization**: Displays sentiment trends through various visualizations (scatter plots, histograms, pie charts).
- **Customizable**: Allows users to input different stock tickers for analysis.

## Technologies Used
| Technology          | Description                                                                          |
|---------------------|--------------------------------------------------------------------------------------|
| Python              | Programming language used for data scraping, analysis, and visualization.           |
| Requests            | Library for making HTTP requests to fetch web pages and news data.                 |
| BeautifulSoup       | Library for parsing HTML and XML documents to extract relevant data.                |
| TextBlob            | Natural language processing library for performing sentiment analysis.               |
| Pandas              | Data manipulation library for organizing and analyzing sentiment data.              |
| Matplotlib          | Plotting library for creating various visualizations.                               |
| PyCharm             | IDE for Python development, providing tools for code editing and debugging.        |
| Git                 | Version control system for tracking changes in code and facilitating collaboration.  |

## Workflow
The workflow of the Stock News Sentiment Analysis project can be summarized in the following steps:

1. **Input Stock Ticker**: The user enters a stock ticker symbol for analysis.
2. **Fetch News Data**: The program scrapes the latest news articles from finviz.com related to the specified ticker.
3. **Parse News Articles**: Extracts the date, time, title, and other relevant details from the scraped news data.
4. **Sentiment Analysis**: Analyzes the sentiment of the news titles using TextBlob, producing a sentiment polarity score.
5. **Data Visualization**: Generates various plots to visualize sentiment trends, distribution, and proportions of positive, negative, and neutral sentiments.

```mermaid
flowchart LR
    A[Input Stock Ticker] --> B[Fetch News Data]
    B --> C[Parse News Articles]
    C --> D[Sentiment Analysis]
    D --> E[Data Visualization]
    E --> F[Display Results]


![image](https://github.com/user-attachments/assets/b4be90c4-5735-4c5d-9082-098672708f6f)





