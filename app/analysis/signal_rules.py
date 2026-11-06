def _trend(row):
    if row["ema_20"] > row["ema_50"]:
        return "bullish"
    if row["ema_20"] < row["ema_50"]:
        return "bearish"
    return "neutral"

def baseline_m15_signal(m15, h1):
    """Unvalidated research hypothesis. Inputs must be completed candles."""
    if m15 is None or h1 is None:
        return {"decision": "NO_TRADE", "reason": "Missing timeframe confirmation."}
    required_m15 = ("ema_20", "ema_50", "rsi_14", "atr_14")
    required_h1 = ("ema_20", "ema_50")
    if any(m15.get(k) is None for k in required_m15) or any(h1.get(k) is None for k in required_h1):
        return {"decision": "NO_TRADE", "reason": "Required indicator values missing."}
    ht, mt = _trend(h1), _trend(m15)
    if ht == mt == "bullish" and 45 <= m15["rsi_14"] <= 65:
        return {"decision": "BUY", "reason": "Bullish H1/M15 alignment and RSI filter."}
    if ht == mt == "bearish" and 35 <= m15["rsi_14"] <= 55:
        return {"decision": "SELL", "reason": "Bearish H1/M15 alignment and RSI filter."}
    return {"decision": "NO_TRADE", "reason": "Trend or momentum confirmation failed."}
