# GridTariff ⚡

### Real-Time Energy Tariff & Billing Engine

GridTariff is a distributed system that simulates a real-world **energy tariff calculation platform** used by utility companies.

The system ingests electricity usage data from smart meters, processes it through a streaming pipeline, calculates energy costs using tariff rules (including Time-of-Use pricing), and exposes analytics through an API and dashboard.

This project demonstrates **event-driven microservices architecture** using modern backend technologies.

---

# Project Goals

The main objective of GridTariff is to simulate how electricity providers:

* collect smart meter readings
* process energy usage streams
* apply tariff pricing logic
* calculate electricity cost
* generate billing summaries
* expose consumption analytics to users

The system is designed for **learning distributed systems and streaming architectures** in the energy domain.

---

# Tech Stack

## Backend

* **Python** – core backend services
* **FastAPI** – API layer
* **Kafka** – event streaming pipeline
* **Redis** – caching and real-time state storage
* **APScheduler** – scheduled jobs for simulation and aggregation

## Frontend

* **React** – dashboard interface
* **Chart.js / Recharts** – energy consumption visualization

## Infrastructure

* **Docker / Docker Compose** – service orchestration
* **Kafka** – event broker
* **Redis** – in-memory data store

---

# Core System Architecture

The platform follows an **event-driven microservices architecture**.

```
Smart Meter Simulator
        |
        v
     Kafka (meter_usage)
        |
        v
Usage Aggregator Service
        |
        v
Tariff Engine Service
        |
        v
Billing Service
        |
        v
Redis Cache
        |
        v
FastAPI Backend
        |
        v
React Dashboard
```

Each service operates independently and communicates using **Kafka events**.

---

# Microservices Overview

## 1. Meter Simulator Service

Simulates smart meters sending electricity usage data.

Responsibilities:

* generate energy usage events
* publish messages to Kafka
* run scheduled tasks

Example event:

```
{
  "meter_id": "MTR001",
  "usage_kwh": 1.7,
  "timestamp": "2026-03-11T19:10:00"
}
```

Technologies:

* Python
* Kafka Producer
* APScheduler

---

## 2. Usage Aggregator Service

Consumes meter events and aggregates consumption data.

Responsibilities:

* process meter usage streams
* compute hourly energy totals
* store latest readings in Redis

Example Redis keys:

```
meter:MTR001:latest_usage
meter:MTR001:hourly_total
```

Technologies:

* Python
* Kafka Consumer
* Redis

---

## 3. Tariff Engine Service

Applies electricity tariff rules and calculates cost.

Responsibilities:

* determine applicable tariff window
* apply Time-of-Use pricing
* generate cost events

Energy billing follows:

Energy Cost = Energy Consumption × Tariff Rate

Example:

```
usage: 2 kWh
tariff: ₹8/kWh
cost: ₹16
```

---

## 4. Billing Service

Aggregates cost data to produce billing summaries.

Responsibilities:

* calculate daily cost
* estimate monthly bill
* maintain billing records

Example output:

```
meter_id: MTR001
daily_cost: ₹142
monthly_estimate: ₹3850
```

---

## 5. Backend API Service

Provides REST APIs for external access.

Responsibilities:

* expose meter data
* provide billing analytics
* serve dashboard queries

Example endpoints:

```
GET /meters
GET /usage/{meter_id}
GET /billing/{meter_id}
GET /tariffs
```

Technologies:

* FastAPI
* Redis
* Python

---

# Frontend Dashboard

The React dashboard provides real-time visibility into energy usage and billing.

Features:

### Meter Monitoring

Displays current consumption per meter.

```
Meter ID    Usage(kWh)    Cost
MTR001      12.4          ₹86
MTR002      9.2           ₹62
```

### Tariff Configuration

Allows modifying tariff rules such as:

* peak pricing
* off-peak pricing
* weekend pricing

### Billing Analytics

Visualizes:

* hourly consumption
* daily cost
* monthly projections

---

# Kafka Topics

The system communicates using the following Kafka topics:

```
meter_usage
usage_aggregated
cost_events
billing_events
alerts
```

---

# Redis Usage

Redis acts as the real-time state store.

Used for:

* latest meter readings
* aggregated hourly usage
* cached billing summaries

Example keys:

```
meter:MTR001:latest_usage
meter:MTR001:daily_cost
```

---

# Scheduled Jobs (APScheduler)

Scheduled tasks simulate real-world background processes.

Examples:

* generate smart meter events
* compute hourly usage summaries
* run daily billing calculations

---

# Project Structure

```
gridtariff
│
├── services
│   ├── meter_simulator
│   ├── usage_aggregator
│   ├── tariff_engine
│   ├── billing_service
│   └── backend_api
│
├── frontend
│   └── dashboard
│
├── infrastructure
│   ├── kafka
│   ├── redis
│   └── docker
│
└── docker-compose.yml
```

---

# Running the Project

## Prerequisites

* Python 3.10+
* Node.js
* Docker
* Docker Compose

---

## Start Infrastructure

```
docker-compose up -d
```

This will start:

* Kafka
* Redis

---

## Run Backend Services

Example:

```
cd services/meter_simulator
python main.py
```

Repeat for other services.

---

## Run Frontend

```
cd frontend/dashboard
npm install
npm start
```

---

# Learning Outcomes

This project demonstrates:

* event-driven architecture
* microservices communication using Kafka
* real-time data processing
* caching strategies using Redis
* scheduled job orchestration
* scalable backend design

---

# Future Improvements

Possible enhancements include:

* authentication and user accounts
* WebSocket-based real-time updates
* advanced tariff rule engine
* anomaly detection for energy spikes
* monitoring using Prometheus and Grafana


gridtariff
│
├── services
│   ├── meter-service
│   ├── processing-service
│   └── backend-api
│
├── frontend
│   └── dashboard
│
├── infrastructure
│   └── docker-compose.yml
│
└── README.md

meter-service
│
├── app
│   ├── producer.py
│   ├── meter_generator.py
│   └── main.py
│
├── config
│   └── settings.py
│
├── requirements.txt
└── Dockerfile

processing-service
│
├── app
│   ├── consumers
│   │   └── meter_consumer.py
│   │
│   ├── services
│   │   ├── aggregation_service.py
│   │   ├── tariff_service.py
│   │   └── billing_service.py
│   │
│   ├── repositories
│   │   └── redis_repository.py
│   │
│   ├── models
│   │   └── meter_event.py
│   │
│   └── main.py
│
├── config
│   └── settings.py
│
├── requirements.txt
└── Dockerfile

backend-api
│
├── app
│   ├── controllers
│   │   ├── meter_controller.py
│   │   ├── usage_controller.py
│   │   └── billing_controller.py
│   │
│   ├── services
│   │   ├── meter_service.py
│   │   └── billing_service.py
│   │
│   ├── repositories
│   │   └── redis_repository.py
│   │
│   ├── schemas
│   │   └── meter_schema.py
│   │
│   └── main.py
│
├── config
│   └── settings.py
│
├── requirements.txt
└── Dockerfile


