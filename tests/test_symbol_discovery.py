from app.market_data.symbols import discover_gold_symbol

def test_exact_gold_symbol():
    assert discover_gold_symbol(["EURUSD", "XAUUSD"]) == "XAUUSD"

def test_unique_suffix_symbol():
    assert discover_gold_symbol(["EURUSD", "XAUUSDm"]) == "XAUUSDm"

def test_ambiguous_suffixes_require_manual_selection():
    assert discover_gold_symbol(["XAUUSDm", "XAUUSD.pro"]) is None
