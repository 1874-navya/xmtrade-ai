import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    required = {"open", "high", "low", "close", "volume"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {sorted(required - set(df.columns))}")
    out = df.copy()
    out["ema_20"] = out["close"].ewm(span=20, adjust=False).mean()
    out["ema_50"] = out["close"].ewm(span=50, adjust=False).mean()
    delta = out["close"].diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss.replace(0, float("nan"))
    out["rsi_14"] = 100 - 100 / (1 + rs)
    previous = out["close"].shift(1)
    true_range = pd.concat([
        out["high"] - out["low"],
        (out["high"] - previous).abs(),
        (out["low"] - previous).abs(),
    ], axis=1).max(axis=1)
    out["atr_14"] = true_range.ewm(alpha=1/14, adjust=False).mean()
    return out
