# Software Requirements Specification (SRS)
## Project: SentinelStream – Real-Time Fraud Detection System

---

## 1. Introduction
SentinelStream is a real-time transaction fraud detection backend designed for high-throughput
financial systems such as credit cards and neo-banking platforms.

### 1.1 Purpose
The system detects potentially fraudulent transactions using a rule-based engine
and machine-learning risk scoring.

### 1.2 Scope
- Accept transactions via REST API
- Apply fraud rules
- Generate risk scores
- Persist immutable transaction records
- Provide analytics-ready data models

---

## 2. System Architecture

User → API Gateway → FastAPI → Rule Engine → ML Model → PostgreSQL → Response

Technologies:
- FastAPI
- PostgreSQL
- Pydantic
- Swagger/OpenAPI

---

## 3. Functional Requirements

FR-1: Accept transaction requests  
FR-2: Apply rule-based validation  
FR-3: Generate ML risk score  
FR-4: Store transaction immutably  
FR-5: Return fraud decision  

---

## 4. Non-Functional Requirements

- High throughput (low latency)
- API contract stability
- Secure database storage
- Scalable architecture

---

## 5. Database Design

- OLTP schema for transactions
- Star schema for analytics
- Fully normalized (3NF)

---

## 6. API Specification

POST /process-transaction  
Input: amount  
Output: rule_flag, risk_score, decision

---

## 7. Assumptions & Constraints

- ML model is simulated
- Single-node deployment


## Database Normalization (3NF Verification)

1NF:
- All fields are atomic
- No repeating groups

2NF:
- No partial dependency on composite keys
- Each non-key attribute depends on the primary key

3NF:
- No transitive dependencies
- Decision and time attributes moved to separate tables

Conclusion:
The schema satisfies Third Normal Form (3NF).
