from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="XMTrade AI", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "execution_mode": "PAPER_ONLY", "live_execution": "not_implemented"}

@app.get("/config")
def get_config():
    return {
        "symbol": settings.gold_symbol_override or "AUTO_DISCOVER_GOLD",
        "primary_timeframe": settings.primary_timeframe,
        "confirmation_timeframe": settings.confirmation_timeframe,
        "max_risk_per_trade_pct": settings.max_risk_per_trade_pct,
        "paper_starting_balance_usd": settings.paper_starting_balance_usd,
        "news_analysis_enabled": settings.news_analysis_enabled,
        "execution_mode": "PAPER_ONLY",
    }

@app.get("/recommendations/latest")
def latest_recommendation():
    return {
        "symbol": settings.gold_symbol_override or "GOLD_SYMBOL_PENDING_DISCOVERY",
        "timeframe": settings.primary_timeframe,
        "decision": "NO_TRADE",
        "reason": "No validated market data has been loaded.",
        "paper_eligible": False,
    }
