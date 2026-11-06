from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "development"
    paper_trading_only: bool = True
    paper_starting_balance_usd: float = 1000.0
    max_risk_per_trade_pct: float = 0.5
    primary_timeframe: str = "M15"
    confirmation_timeframe: str = "H1"
    gold_symbol_override: str | None = None
    csv_data_dir: str = "./data"
    news_analysis_enabled: bool = True
    database_url: str = "sqlite:///./xmtrade_ai.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def enforce_safety(self):
        if not self.paper_trading_only:
            raise RuntimeError("Live trading is not supported by XMTrade AI.")
        if not 0 < self.max_risk_per_trade_pct <= 0.5:
            raise ValueError("V1 risk ceiling must be in (0, 0.5] percent.")
        if self.paper_starting_balance_usd <= 0:
            raise ValueError("Paper starting balance must be positive.")

settings = Settings()
settings.enforce_safety()
