from pydantic import BaseModel
from datetime import datetime

class TransactionRequest(BaseModel):
    amount: int

class TransactionResponse(BaseModel):
    amount: int
    rule_flag: bool
    risk_score: float
    decision: str
    created_at: datetime
