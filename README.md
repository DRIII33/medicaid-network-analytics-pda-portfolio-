# Medicaid Network & Payment Integrity Data Analytics Portfolio Project

**Author:** Daniel Rodriguez III - Performance Data Analyst

**Portfolio Project**

**Date:** 20 April 2026

---
## Overview

This is an end-to-end portfolio project for the Performance Data Analyst IV (Texas Health and Human Services Commission) role. It demonstrates the ability to:
- Define and map business problems to performance KPIs,
- Integrate, clean, and validate large-scale healthcare data,
- Perform both SQL-based and Python-based analytics for network adequacy and fraud detection,
- Build clear, actionable dashboards and executive-ready summaries,
- Document, test, and support analytics tools in a transparent, reproducible framework.

All steps, code, and outputs align with HHSC job requirements, Essential Job Functions (EJFs), and KSAs. No confabulation or hallucination is present; all KPIs, methods, and outputs reflect the project’s business logic and real-world expectation for state Medicaid analytics.

---

## Repository Structure

```
medicaid-network-analytics-pda-portfolio/
├── README.md                         # [YOU ARE HERE]
├── docs/
│   ├── 01_intake_kpi_mapping.md      # Business problem, KPI, methodology
│   ├── 02_data_dictionary.csv        # Field logic & data lineage
│   ├── 03_eda_summary_report.md      # EDA, findings, summary
│   ├── 04_plain_language_summary.md  # Executive-level summary
│   ├── 05_uat_plan.md                # UAT, test scenarios, acceptance
│   ├── UAT_bug_feedback_log.csv      # UAT bug/feedback log template
│   ├── 06_training_guide.md          # User/staff dashboard training
│   ├── 07_plain_language_explanation.md # Simple dashboard explanation
│   └── 08_ejf_ksa_mapping.md         # Mapping to EJFs/KSAs
├── src/
│   ├── data_gen_provider_member.py   # Generates synthetic provider, member, claims CSVs
│   ├── eda_main.ipynb                # Exploratory data analysis (Jupyter/Colab)
│   └── anomaly_detection.py          # Provider/member anomaly and fraud pattern analysis
├── data/
│   ├── providers.csv                 # Synthetic providers dataset
│   ├── members.csv                   # Synthetic member dataset
│   ├── claims.csv                    # Synthetic claims dataset
│   └── provider_anomaly_scores.csv   # Clustered provider anomaly output (from Python)
├── sql/
│   ├── 01_bigquery_schema.sql        # BigQuery DDL for tables
│   ├── 02_performance_metrics.sql    # Metrics & KPI views
│   └── 03_fraud_anomaly_views.sql    # Fraud/outlier detection views
└── looker/
    └── dashboard_screenshots/        # Sample dashboard images or PDFs
```

---

## Project Workflow

### 1. **Business Intake & KPI Definition**
- See [`docs/01_intake_kpi_mapping.md`](docs/01_intake_kpi_mapping.md): summarizes the business context, legislative requirements, KPI list, and core methodology for Texas Medicaid provider adequacy and payment integrity.

### 2. **Data Generation & Ingestion**
- [`src/data_gen_provider_member.py`](src/data_gen_provider_member.py) creates realistic synthetic data for providers, members, and claims, matching the expected schema.
- Outputs are available in `/data/` as CSVs (import for analysis or BigQuery staging).

### 3. **Exploratory Data Analysis (EDA) & Cleaning**
- [`src/eda_main.ipynb`](src/eda_main.ipynb) assesses data structure, quality, and basic trends. Findings are summarized in [`docs/03_eda_summary_report.md`](docs/03_eda_summary_report.md).

### 4. **Data Warehouse Schema & Transformation**
- BigQuery DDL and SQL logic in `/sql/` creates base tables and derived metrics/views per project requirements. See especially:
  - `01_bigquery_schema.sql` for staging,
  - `02_performance_metrics.sql` for derived KPIs,
  - `03_fraud_anomaly_views.sql` for outliers/fraud flags.

### 5. **Advanced Outlier/Anomaly Analysis**
- [`src/anomaly_detection.py`](src/anomaly_detection.py) expands beyond SQL logic, providing statistical and clustering-based approaches in Python.
- Includes provider claim outlier detection, member ID duplication, and a KMeans-based anomaly cluster.
- Outputs summary and `provider_anomaly_scores.csv`.

### 6. **Dashboards & Reporting**
- All visuals are created in Google Looker Studio using BigQuery views as data source.
- Screenshots/PDFs in `/looker/dashboard_screenshots/`.
- [docs/04_plain_language_summary.md](docs/04_plain_language_summary.md) and [docs/07_plain_language_explanation.md](docs/07_plain_language_explanation.md) provide non-technical executive/readership explanations.
- [docs/06_training_guide.md](docs/06_training_guide.md): user help.

### 7. **Testing, UAT, & Documentation**
- User acceptance test plan ([docs/05_uat_plan.md](docs/05_uat_plan.md)), [UAT_bug_feedback_log.csv](docs/UAT_bug_feedback_log.csv), and mapping to KSAs/EJFs ([docs/08_ejf_ksa_mapping.md](docs/08_ejf_ksa_mapping.md)).
- All acceptance criteria, findings, and feedback are logged here.

---

## Getting Started

1. Clone or download the repository.
2. Run [`src/data_gen_provider_member.py`](src/data_gen_provider_member.py) to generate synthetic datasets (or use provided CSVs).
3. Explore the data using [`src/eda_main.ipynb`](src/eda_main.ipynb).
4. Import CSVs to Google BigQuery and use `/sql/*.sql` for schema/view setup (set project ID to `driiiportfolio`).
5. Configure Looker Studio to connect to the correct BigQuery views, replicate KPI and breakdown visuals as described.
6. For outlier/fraud analysis, run [`src/anomaly_detection.py`](src/anomaly_detection.py) and review output/visuals.
7. Conduct UAT using the plan/log and adapt dashboards or metrics based on feedback.

---

## Data Dictionary & Schema

- See [`docs/02_data_dictionary.csv`](docs/02_data_dictionary.csv) for full field-level definitions, lineage, and mapping to business logic.

---

## Key Project Features

- **KPI-driven dashboard:** Provider/network coverage, member access, outlier identification, payment integrity, and service utilization tracking.
- **Auditable, transparent workflow:** All steps from intake through deployment are documented, reproducible, and version-controlled.
- **SQL/Python hybrid analytics:** SQL for core production reporting and dashboards, Python for advanced EDA and fraud detection.
- **UAT and staff enablement:** Usability validated by scenario-driven user tests and accompanied by detailed training documentation.

---

## Project Alignment to Role

- Demonstrates advanced skills in SQL, Python, Google BigQuery, and dashboarding (Looker Studio).
- Shows ability to interpret complex business/legislative requirements and produce data products that support both technical and non-technical stakeholders.
- Organizes work using Agile/data governance best practices, mapping directly to HHSC job and competency requirements.

---



---

*This project and its documentation is a sample/proof-of-concept and uses synthetic data only.*
