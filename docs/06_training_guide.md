# Dashboard & Data Tool Training Guide: Medicaid Network Analytics

## Who should use this guide?
- HHSC PMAS analysts, program managers, and staff who need to view, explore, and present provider network and payment integrity data

---

## Getting Started

1. **Dashboard Access**
    - Log in to Google Looker Studio using your agency-issued credentials.
    - Open the “Medicaid Network Analytics” dashboard from shared links or the agency dashboard portal.

2. **Dashboard Structure**
    - **3 Main Pages:**  
        - **Network Adequacy Overview** (provider access, county/member KPIs)
        - **Payment Integrity & Outliers** (high-activity provider risk, identity issues)
        - **Utilization & Service Type Detail** (what services are being used, trend over time)

---

## Key Features & Filters

- **Date Range Filter**: Top right of each page allows selection of reporting period (default: last 12 months).
- **County/Provider Type Filters**: Adjust tables and charts to focus on specific locations or provider specialties.
- **Tooltips / Info Buttons**: Hover for metric definitions and calculation notes.

---

## Working with Visuals

- **KPIs/Scorecards**:  
    - Show current rates and counts. Click or filter to see breakdowns by geography or type.

- **Tables & Charts**:  
    - Click column headers to sort.
    - Export as CSV by clicking the three-dot menu above each visual.

- **Time Series**:  
    - Use claim_date axis to observe trends or spot anomalies in payment over months.

- **Bar Charts**:  
    - Hover for underlying numbers and exact rates.

---

## Interpreting Key Metrics

- **Provider Density**: Higher values mean more providers are available per 1,000 Medicaid members.
- **Network Adequacy Rate**: Percent of members with at least one claim from a provider in their home county—aim for numbers above 90%.
- **Primary Care Access Rate**: For child members (<18), shows if they receive regular check-ups.
- **High-Risk Provider Count**: Providers with abnormally high claim volumes—review these for quality or compliance.
- **Duplicate Member IDs**: Higher rates may mean system errors or potential fraud; escalate to management if this rises or spikes.

---

## Best Practices for Staff

- Regularly review dashboard KPIs to monitor trends and problems.
- Use export features for reports or detailed follow-ups.
- If you spot odd numbers or spikes, verify the underlying data and alert the PMAS analytics or compliance team.
- Participate in UAT and provide feedback using the bug log—this improves future dashboards and data quality.

---

## Support & Questions

- For access issues or requests, email the PMAS data team.
- See README and docs folder in GitHub for detailed technical logic, calculations, and troubleshooting.

---

*This guide is current as of April 20, 2026, and should be updated if major dashboard or process changes are implemented.*
