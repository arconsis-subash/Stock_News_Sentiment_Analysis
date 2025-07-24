import axios from 'axios';
import './App.css';
import {ChangeEvent, useState} from "react"

interface NewsItem {
  0: string;    // date
  1: string;    // time
  2: string;    // title
  3: number;    // sentiment
}


interface SentimentResponse {
  ticker: string;
  news: NewsItem[];
}

function App() {
  const [ticker, setTicker] = useState<string>("");
  const [result, setResult] = useState<NewsItem[]>([]);


  const handleChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setTicker(e.target.value);
  };


  const fetchSentiment = async (): Promise<void> => {
    try {
      const response = await axios.post<SentimentResponse>("http://localhost:8000/analyze", {
        ticker: ticker.toUpperCase(),
      });
      setResult(response.data.news || []);
    } catch (err) {
      alert("Error fetching sentiment");
    }
  };

  return (
    <div className="App">
        <div style={{ padding: 20 }}>
      <h1>Stock News Sentiment</h1>
      <input
        type="text"
        value={ticker}
        onChange={handleChange}
        placeholder="Enter stock ticker (e.g., TSLA)"
      />
      <button onClick={fetchSentiment}>Analyze</button>

      {result.length > 0 && (
        <div>
          <h2>Results</h2>
          <ul>
            {result.map((news, idx) => (
              <li key={idx}>
                <strong>{news[0]} {news[1]}</strong>: {news[2]} <br />
                Sentiment: {news[3].toFixed(2)}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
    </div>
  );
}

export default App;
