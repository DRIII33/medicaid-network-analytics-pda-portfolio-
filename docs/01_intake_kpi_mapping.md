# Project Intake, KPI Mapping, and Methodology

## Business Problem

The Texas Health and Human Services Commission (HHSC) must guarantee that Medicaid members have timely access to qualified providers according to state and federal requirements and must rapidly identify and mitigate risks around inaccurate claims or potential fraud. Network adequacy (i.e., making sure enough providers of applicable types serve each region) and payment integrity (detecting overbilling or unusual provider utilization) are critical for compliance, funding, and the quality of care provided to Texans.

## Project Objectives

1. **Measure Medicaid Provider Network Adequacy:**  
   Track whether each county in Texas meets HHSC and CMS standards for Medicaid members’ access to primary care, specialty, and behavioral health providers within the required geographic/time distance.

2. **Detect Anomalous Provider Patterns (Potential Risk/Fraud):**  
   Identify providers or groups with higher-than-expected claims volumes, duplicate identifiers, or unusual service coding.

3. **Generate and Present Metrics for Stakeholders:**  
   Deliver clear and actionable dashboards and code-based reports for agency/legislative review showing areas of concern, improvement, and strong network performance.

## Key Stakeholders

- Office of Data, Analytics, and Performance (DAP) Director
- Program managers (Medicaid/CHIP Services)
- Provider network management teams
- Office of Inspector General (OIG)
- Agency Technical Staff (PMAS)
- Texas legislators/leadership

## Selected KPIs

| KPI Name                  | Brief Description                                                                                  | Calculation Methodology                                                    |
|--------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Provider Density         | # Medicaid providers per 1,000 enrolled members by county & provider type                          | COUNT(providers) / COUNT(members) per geography/type                     |
| Network Adequacy Rate    | % of members with at least one paid claim at appropriate provider type in their home county        | COUNT(members w/ county match claim) / COUNT(total members in county)    |
| Primary Care Access Rate | % of Medicaid members under age 18 with a paid claim for a PCP within last 12 months               | COUNT(members < 18 w/ PCP claim) / COUNT(members < 18)                  |
| High-Risk Provider Rate  | % providers above 99th percentile for claims submitted in last 12 months                          | COUNT(providers > 99th pctile) / COUNT(providers)                       |
| Duplicate Member IDs     | # of member IDs submitted on two providers’ claims in the same service week                        | COUNT(duplicates identified)                                             |
| Nutrition Counseling Rate| % of eligible pregnant women receiving nutrition counseling per HB 26                              | COUNT(unique service, eligible) / COUNT(eligible members)                |

## Data Sources & Flow

- **providers.csv** (Loaded to BigQuery: `driiiportfolio.medicaid.providers`): lists all Medicaid-enrolled providers, type, identifiers, location
- **members.csv** (Loaded to BigQuery: `driiiportfolio.medicaid.members`): synthetic member census including DOB, home county, demographics
- **claims.csv** (Loaded to BigQuery: `driiiportfolio.medicaid.claims`): all program claims submitted (with date, provider, member, CPT, status)

ETL pipeline and dashboards will be version-controlled via GitHub and all methodologies transparently documented for audit and agency review.

## Methodology Summary

1. **Intake & KPI Alignment**:  
   - Review state/agency standards (UMCM, HB 26, SB 1 Rider 7)
   - Consult stakeholders on reporting requirements and definitions (document here and in project issues)

2. **Data Mapping & Quality**:  
   - Map each field to its logical and business purpose (see `docs/02_data_dictionary.csv`)
   - Cross-check source, validity, uniqueness, and security constraints

3. **Metric Definition & SQL Logic**:  
   - Write SQL logic and calculations in BigQuery for each KPI
   - Test and validate logic using synthetic dataset

4. **Reporting & Dashboarding**:  
   - Metrics surfaced in Looker Studio and summary reports
   - Results mapped to required formats for executive and public transparency use

5. **Feedback & Continuous Improvement**:  
   - UAT, program staff review, and Q&A documented in GitHub issues

All definitions, mapping, and logic are versioned in the GitHub repository for full transparency and repeatability.

---
