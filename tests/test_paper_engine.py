import pytest
from app.paper_trading.engine import PaperTradingEngine

def test_paper_trade_lifecycle():
    engine = PaperTradingEngine()
    trade = engine.open_trade("XAUUSD", "BUY", 3000, 1, 2990, 3020, True)
    engine.close_trade(trade, 3010)
    assert trade.status == "CLOSED"
    assert trade.pnl_usd == 10

def test_risk_rejection_blocks_open():
    engine = PaperTradingEngine()
    with pytest.raises(PermissionError):
        engine.open_trade("XAUUSD", "BUY", 3000, 1, 2990, 3020, False)
