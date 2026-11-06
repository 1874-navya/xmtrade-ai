from pathlib import Path
import pandas as pd
from app.market_data.provider import HistoricalDataProvider

class CsvHistoricalProvider(HistoricalDataProvider):
    def __init__(self, data_dir: str = "./data"):
        self.data_dir = Path(data_dir)

    def load_candles(self, symbol: str, timeframe: str) -> pd.DataFrame:
        path = self.data_dir / f"{symbol}_{timeframe}.csv"
        if not path.exists():
            raise FileNotFoundError(path)
        df = pd.read_csv(path, parse_dates=["timestamp"])
        required = {"timestamp", "open", "high", "low", "close", "volume"}
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {sorted(missing)}")
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="raise")
        df = df.sort_values("timestamp").drop_duplicates("timestamp")
        if df.empty or (df[["open", "high", "low", "close"]] <= 0).any().any():
            raise ValueError("Empty data or non-positive OHLC values.")
        if (df["high"] < df[["open", "close", "low"]].max(axis=1)).any():
            raise ValueError("Invalid candle high.")
        if (df["low"] > df[["open", "close", "high"]].min(axis=1)).any():
            raise ValueError("Invalid candle low.")
        return df.set_index("timestamp")
