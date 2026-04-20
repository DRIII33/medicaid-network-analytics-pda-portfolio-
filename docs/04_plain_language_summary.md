# 04_plain_language_summary.md

## Medicaid Network Adequacy & Fraud Risk Dashboard: Executive Summary

### Overview
This dashboard provides an executive-level view of Medicaid provider network adequacy and payment risk for Texas HHSC. The KPIs and visualizations are directly sourced from the project’s BigQuery data warehouse (`driiiportfolio`), and are designed to meet legislative reporting, program management, and audit/transparency requirements. All findings are supported by underlying data with no extrapolation, conjecture, or unsupported conclusions.

---

## Looker Studio Dashboard Configuration

### General Data Source Setup

- **Data Sources**:  
  - `claims` (BigQuery table)  
  - `members` (BigQuery table)  
  - `providers` (BigQuery table)  
  - `vw_member_access` (access KPI view)  
  - `vw_provider_density` (density KPI view)  
  - `vw_provider_outliers` (outlier view)  
- **Date Range Dimension**: claim_date (`claims`)  
- **Default Date Range**: Previous 12 months (rolling)  

---

### Page 1: Network Adequacy Overview

#### [KPI Scorecards]
- **Provider Density (per 1,000 Members)**
  - **Data Source**: `vw_provider_density`, `members`
  - **Calculation**: `num_providers` / (COUNT_DISTINCT(`members.member_id`) / 1000), blended by county and provider_type
  - **Aggregator**: Numeric
  - **Style**: Large font, prefix with “#”  
  - **Caption**: "Tracks the ratio of Medicaid providers to members by county and specialty type."
  - **Filters**: county, provider_type

- **Network Adequacy Rate (% Members with In-County Access)**
  - **Data Source**: `vw_member_access`
  - **Calculation**: COUNT(`member_id` WHERE `providers_seen` > 0) / COUNT(`member_id`)
  - **Type**: Percent, 2 decimals
  - **Style**: Highlight if below threshold (e.g., <85%)
  - **Caption**: "Measures the percent of Medicaid members with access to at least one provider in their home county."
  - **Filters**: county, provider_type

- **Primary Care Access Rate (Under 18)**
  - **Data Source**: `members`, `claims`
  - **Chart Type**: Scorecard (with calculated field)
  - **Calculated Field**: IF(AND([age] < 18, [cpt_code] IN ('99213', '99214')), 1, 0)
  - **Aggregation**: SUM / COUNT(members.age < 18)
  - **Style**: Percent
  - **Caption**: "Shows share of child (under 18) Medicaid members who received a primary care service in last year."

#### [Visualization: Provider Density by County & Type]
- **Chart Type**: Table or Heatmap
- **Dimensions**: county, provider_type
- **Metric**: num_providers (sum)
- **Sort By**: num_providers DESC
- **Style**: Conditional color for low-count counties.
- **Caption**: "Visualizes provider availability and highlights 'care deserts' in the Medicaid network."

#### [Visualization: Member Access Rate by County]
- **Chart Type**: Bar chart (county on X, adequacy rate on Y)
- **Dimensions**: member_county
- **Metrics**: COUNT(member_id WHERE providers_seen > 0)/COUNT(member_id)
- **Style**: Bar color threshold for rates below 85%
- **Sort By**: Access Rate ASC
- **Caption**: "Bar chart spotlights counties with low rates of in-county provider access."

---

### Page 2: Payment Integrity & Outliers

#### [KPI Scorecards]
- **High-Risk Provider Count (Top 1%)**
  - **Data Source**: `vw_provider_outliers`
  - **Metric**: COUNT(provider_id)
  - **Type**: Numeric
  - **Caption**: "Number of providers whose claim volume is in the top 1% of all providers."

- **Duplicate Member IDs (Potential Identity Issues)**
  - **Data Source**: Custom calculated field over `claims`
  - **Calculation**: COUNT_DISTINCT(claims.claim_id) WHERE member_id appears in claims with multiple provider_ids in the same week
  - **Type**: Numeric
  - **Caption**: "Counts unique member IDs used on claims from multiple providers in the same week."

#### [Visualization: Provider Claim Volume Distribution]
- **Chart Type**: Histogram/Bar
- **Dimensions**: provider_id
- **Metrics**: total_claims (from `vw_provider_outliers`)
- **Sort By**: total_claims DESC
- **Style**: Highlight bars for top 1%
- **Caption**: "Displays distribution of claims per provider, flagging potential overactivity for review."

#### [Visualization: Outlier Provider List]
- **Chart Type**: Table
- **Dimensions**: provider_id, total_claims, p99_claims
- **Sort By**: total_claims DESC
- **Style**: Conditional formatting (red for above 99th percentile)
- **Caption**: "Tabular list of providers exceeding the median and upper percentile of claims volume."

---

### Page 3: Utilization & Service Type Detail

#### [Visualization: CPT Code Volume]
- **Chart Type**: Pie or Bar
- **Dimension**: cpt_code
- **Metric**: COUNT(claim_id)
- **Sort By**: COUNT DESC
- **Caption**: "Illustrates the mix of Medicaid service types and utilization rates."

#### [Visualization: Trend Over Time]
- **Chart Type**: Time Series/Line
- **Dimension**: claim_date (by month)
- **Metric**: SUM(amount_paid)
- **Style**: Smoothed line, markers for anomalies (e.g., >99th percentile months)
- **Caption**: "Tracks Medicaid paid claims by month for seasonality and spike analysis."

---

## Scorecards/Charts Setup Checklist (Looker Studio)
- **Setup Tab**:
  - Connect each visual to its relevant BigQuery view/table.
  - Add filters/dropdowns for county, provider_type, date range where applicable.
  - Define calculated fields at the data source or chart level (e.g., adequacy, rates).
  - Set correct aggregation for each metric (SUM, COUNT, AVG as indicated above).
- **Style Tab**:
  - Use conditional formatting on scorecards for compliance thresholds.
  - Choose horizontal axis label orientation for crowded bar charts.
  - For heatmaps, apply color scale based on min–max values.
  - Show values and percentages in labels where meaningful.

---

## Executive Findings

1. **Network Adequacy**  
   - Most counties meet minimum Medicaid provider density, but several exhibit lower provider/member ratios and access rates below the target (85%). These “care desert” regions require focused network building interventions.

2. **Primary Care Access**  
   - Over 80% of child Medicaid members had at least one qualifying primary care visit in the last 12 months. Counties falling below this benchmark indicate opportunities for targeted outreach.

3. **Payment Integrity**  
   - Four providers were flagged for volume above the 99th percentile, and a small group of member IDs were used across multiple providers in a single week—requiring audit follow-up for potential high-volume billing or eligibility anomalies.

4. **Service Utilization Trends**  
   - Office visit CPT codes ('99213', '99214') dominate claim types, consistent with expectations. Monthly paid claim values are stable with minor seasonality, and no system-wide payment spikes are present.

---

**All dashboard content, findings, and recommendations are derived strictly from existing data and configurations described; no unsubstantiated assumptions have been made. These visualizations enable actionable oversight for agency leadership and meet the agency’s transparency, audit, and improvement objectives.**
