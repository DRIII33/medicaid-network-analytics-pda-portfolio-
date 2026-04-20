# User Acceptance Testing (UAT) Plan: Medicaid Network Analytics Dashboard

## Purpose

To ensure the dashboard, data pipeline, and reporting tools meet business requirements, are free of critical errors, and are usable by end-users (analysts, managers, leadership).

---

## Test Participants

- Program analysts (Medicaid/CHIP Services)
- Data team (PMAS)
- Program managers
- Super-users from policy and provider relations

---

## Test Scenarios

| Scenario | User Steps | Expected Result | Pass/Fail |
|----------|-----------|----------------|-----------|
| 1. Network Adequacy KPI | Open dashboard, check Network Adequacy Rate | Value matches latest “vw_member_access” calculation | [Result] |
| 2. Provider Density by County | Select a county, review density value | Matches SQL output; county list scrolls and filters | [Result] |
| 3. Access Rate Bar Chart | Hover over county bar, note % | % matches underlying data export | [Result] |
| 4. Filter by Provider Type | Change provider type filter (e.g., Specialist) | All tables and visuals update accordingly | [Result] |
| 5. Payment Integrity Outlier | Review High-Risk Provider Count | Matches count from view “vw_provider_outliers” | [Result] |
| 6. Duplicate Member ID Scorecard | View scorecard; verify with claims extract | Matches manual check | [Result] |
| 7. Download/Export Data | Download provider table view as CSV | File downloads, opens with matching columns | [Result] |
| 8. Responsive Layout | Resize window/browser; verify visuals remain clear and accessible | Visuals adjust for smaller/larger screens | [Result] |
| 9. Dashboard Help | Click on help/info tooltip | Documentation or hint appears as intended | [Result] |

---

## Data/Test Artifacts

- Use latest test export of providers, members, claims, and all BigQuery summary views
- Manual checks performed for at least two counties and three provider types

---

## Bug Reporting

- All defects, discrepancies, and feedback are logged in the UAT bug/feedback log (see CSV template below)
- Each bug entry includes: description, steps to reproduce, severity, status, assigned owner, resolution/notes

---

## Exit Criteria

- All critical bugs resolved or mitigated
- Key user stories and scenarios pass
- Stakeholder signoff (documented in GitHub PR or as a PDF)

---

**This UAT plan ensures that the solution is accurate, meets program needs, and is user-friendly.**
