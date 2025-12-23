## Analytics Star Schema

### Fact Table
fact_transactions
- transaction_id (PK)
- time_id (FK)
- decision_id (FK)
- amount
- risk_score

### Dimension Tables

dim_time
- time_id (PK)
- date
- hour
- day
- month
- year

dim_decision
- decision_id (PK)
- decision_label (APPROVE / DECLINE)

Purpose:
Optimized for fast analytical queries such as:
- Fraud trends per hour
- Decision distribution
