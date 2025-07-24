from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from finviz_scrapper import get_finviz_news
from parser import parse_news
from sentiment import analyze_sentiment

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TickerRequest(BaseModel):
    ticker: str

@app.post("/analyze")
def analyze_news(request: TickerRequest):
    try:
        news_table = get_finviz_news(request.ticker)
        parsed_news = parse_news(news_table)
        analyzed_news = analyze_sentiment(parsed_news)

        return {"ticker": request.ticker, "news": analyzed_news}
    except Exception as e:
        return {"error": str(e)}
