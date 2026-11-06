from abc import ABC, abstractmethod
import pandas as pd

class HistoricalDataProvider(ABC):
    @abstractmethod
    def load_candles(self, symbol: str, timeframe: str) -> pd.DataFrame:
        """Return UTC-indexed OHLCV data and preserve source provenance."""
        raise NotImplementedError
