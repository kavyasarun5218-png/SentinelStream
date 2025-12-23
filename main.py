from fastapi import FastAPI, HTTPException
from datetime import datetime

from models import TransactionRequest, TransactionResponse
from rules import check_rules
from ml_model import predict_risk
from database import get_connection

app = FastAPI(
    title="SentinelStream – Transaction Guard",
    version="1.0.0",
    description="High-speed fraud detection API"
)

@app.post(
    "/process-transaction",
    response_model=TransactionResponse,
    tags=["Transactions"]
)
def process_transaction(payload: TransactionRequest):

    amount = payload.amount

    rule_flag = check_rules(amount)
    risk_score = predict_risk(amount)

    decision = "REJECT" if rule_flag or risk_score > 0.7 else "APPROVE"
    created_at = datetime.utcnow()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO transactions (amount, risk_score, decision)
            VALUES (%s, %s, %s)
        """, (amount, risk_score, decision))

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return TransactionResponse(
        amount=amount,
        rule_flag=rule_flag,
        risk_score=risk_score,
        decision=decision,
        created_at=created_at
    )
