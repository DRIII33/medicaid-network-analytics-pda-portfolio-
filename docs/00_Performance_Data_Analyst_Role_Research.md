# **Comprehensive Strategic Analysis and Operational Process Framework for the Performance Data Analyst IV within the Texas Health and Human Services Commission**

## **Enterprise Overview and Organizational Realignment**

The Texas Health and Human Services Commission (HHSC) operates as one of the most vital and complex administrative entities within the state government of Texas. As of April 19, 2026, the agency is responsible for the health and well-being of approximately 7.5 million Texans, a figure that underscores its massive operational footprint and its significance to the state's social infrastructure. The agency manages a biennial budget for the 2026-2027 period that exceeds $94 billion, which accounts for nearly 28% of the entire state budget. This fiscal magnitude is primarily driven by the administration of Medicaid and the Children’s Health Insurance Program (CHIP), alongside essential nutrition programs such as the Supplemental Nutrition Assistance Program (SNAP) and the Women, Infants, and Children (WIC) initiative.  
A transformative organizational realignment was implemented on April 1, 2026, designed to improve programmatic coordination and enhance the effectiveness of service delivery. This structural shift was informed by extensive feedback from staff, stakeholders, and agency leadership, aiming to center the organization around the specific needs of the clients and families who frequently rely on multiple HHS programs. Central to this realignment was the consolidation of similar programs under two primary divisions: Behavioral Health, Disability and Aging Services, and Family Resources and Eligibility Services.  
The Performance Management and Analytics System (PMAS) is a critical component within the Office of Data, Analytics, and Performance (DAP), which itself is a cornerstone of the Strategic Integration area. DAP is directed by Calvin Green, who oversees the development of data analytics, performance metrics, and governance strategies. The PMAS unit acts as the primary technical engine for integrating and transforming raw HHSC program data into actionable intelligence. Its department designation, PMAS IAPDU FFY26 90/10 Imp, identifies it as a specialized implementation team focused on the FFY 2026 project cycle. The "90/10" nomenclature refers to the enhanced federal financial participation (FFP) rate provided by the Centers for Medicare & Medicaid Services (CMS). Under this funding mechanism, the federal government provides 90% of the funds required for the design, development, and implementation (DDI) of modernized Medicaid IT systems, while the state contributes the remaining 10%.

| Division/Department | Core Functional Responsibility | Key Leadership |
| :---- | :---- | :---- |
| **Health and Human Services Commission** | Enterprise administration of Medicaid, SNAP, and regulatory functions. | Stephanie Muth, Executive Commissioner |
| **Medicaid and CHIP Services (MCS)** | Managed care contract oversight, policy development, and clinical quality. | Emily Zalkovsky, Chief MCS Officer |
| **Office of Data, Analytics, and Performance (DAP)** | Strategy for data governance, predictive modeling, and performance monitoring. | Calvin Green, Director |
| **Performance Management and Analytics System (PMAS)** | Technical implementation of 90/10 federally funded data infrastructure projects. | Director of Performance Analysis |
| **Information Technology (IT)** | Management of the $1.1B IT capital budget and cloud migration efforts. | Sylvia Hernandez Kauffman, CIO |

The PMAS department specifically serves as the vital bridge between the high-level policy goals of the Medicaid and CHIP Services (MCS) division and the technical infrastructure managed by the agency's IT department. The unit's work is inherently cross-functional, requiring the integration of claims data from the Texas Medicaid & Healthcare Partnership (TMHP), provider enrollment data from the Provider Enrollment and Management System (PEMS), and eligibility data from the Texas Integrated Eligibility Redesign System (TIERS). By April 2026, the department is heavily focused on the migration of these disparate datasets into a unified cloud-based environment to support real-time monitoring and legislative reporting mandates.

## **Current Trends and Regional Challenges in Austin, TX**

The operational environment for the Texas HHSC and its PMAS department is currently characterized by a state-wide push for IT modernization, rigorous legislative oversight regarding program integrity, and the administrative complexities of the post-pandemic "Medicaid unwinding" process.

### **System Modernization and the Cloud Migration Trend**

Texas is currently executing a multi-year, $1 billion IT modernization strategy following the passage of the $337 billion biennial budget for 2026-2027. HHSC holds the largest IT capital budget of any Texas agency at $1.1 billion, with major allocations dedicated to the overhaul of the Medicaid Enterprise System and the TIERS eligibility platform. The prevailing trend is the decommissioning of legacy "siloed" databases in favor of the Snowflake AI Data Cloud and Databricks lakehouse architecture.  
This transition represents a fundamental shift toward "data liquidity," where healthcare data is not just stored but is made interoperable and AI-ready. For the PMAS department, this shift creates the challenge of maintaining reporting continuity while migrating petabytes of historical claims and provider records. Data stewards are currently managing the migration from the legacy Compass-21 system to the new PEMS+ format, a process that has identified significant data discrepancies that require manual validation and remediation.

### **Legislative Mandates and Program Integrity**

The 89th Texas Legislature has instituted several mandates that directly impact the workload of performance analysts in Austin. Under SB 1, Rider 7, HHSC must provide quarterly and annual reports to the Legislative Budget Board regarding activities and findings of the Data Analysis Unit. Critically, this rider mandates that any identified anomalies in service utilization, provider behavior, or payment methodologies must be reported immediately to the HHSC Office of Inspector General (OIG).  
In early 2026, Governor Greg Abbott issued a directive to HHSC and the OIG to aggressively increase efforts to combat Medicaid fraud, specifically targeting high-risk service lines. This has led to an imminent June 2026 deadline for a comprehensive report on the utilization of Autism services and Applied Behavior Analysis (ABA). Analysts must also account for HB 26, which requires the tracking and reporting of nutrition counseling services offered by Managed Care Organizations (MCOs) in lieu of clinical services—a new data category that requires the creation of entirely new performance metrics.

### **Austin-Specific Operational Pressures**

The Performance Data Analyst role is based in Austin, TX, at the North Austin Complex. The Austin headquarters is navigating the complexities of a hybrid work environment, where staff are required to be in-office multiple days a week to facilitate high-touch collaboration with program managers and IT vendors. Regional recruitment and retention remain a challenge, as the agency competes with Austin's private tech sector for high-level data talent.  
The Austin eligibility operations teams are also dealing with the "Medicaid unwinding" backlog. Following the end of pandemic-era continuous coverage, over 2 million Texans were disenrolled, many for administrative reasons. As individuals attempt to re-establish eligibility, the volume of applications processed annually has reached 6 million, placing a massive burden on the TIERS system and creating data spikes that analysts must normalize when performing longitudinal trend analysis.

## **Challenges Faced by the Performance Data Analyst**

The Performance Data Analyst IV operates in an environment where technical precision must be balanced against shifting political and policy landscapes.

### **The Problem of Legacy Data Silos**

One of the primary hurdles for the analyst is the lack of integration between legacy systems. For years, provider data was managed in the legacy Compass-21 system, while claims were processed in another, and client eligibility in a third. The analyst must perform complex joins across these disparate environments to create a single view of program performance. Discrepancies in data formats, naming standards, and geocoding accuracy between these systems often lead to "data friction," slowing down the production of time-sensitive reports.

### **Interpretation and Translation of Qualitative Policy**

Analysts face a significant challenge in translating qualitative legislative intent into quantitative technical logic. When a bill like HB 26 mandates reporting on "cost-effective" and "evidence-based" nutrition services, the analyst must work with clinicians to define exactly which CPT (Current Procedural Terminology) codes and provider taxonomies qualify under those definitions. Misalignment between the analyst's query logic and the policy team's intent can lead to inaccurate reporting, which, under the current high-stakes audit environment, could result in legislative scrutiny or federal fund recoupment.

### **User Acceptance Testing (UAT) and Stakeholder Management**

A core function of the Analyst IV is coordinating UAT for new system deployments, such as the PEMS+ launch or the migration of the Quality Performance Report (QPR) dashboards to the cloud. This involves not only technical validation but also "change management"—training non-technical program staff who may be unfamiliar with modern data tools. The analyst must resolve technical bugs identified during testing while simultaneously convincing stakeholders that the new, more rigorous data quality standards are beneficial rather than just another administrative burden.

## **Strategic Reason for Hiring the Candidate**

The hire of a journey-level Performance Data Analyst IV is a strategic move to ensure the successful delivery of the FFY26 PMAS modernization goals while protecting the state's fiscal and regulatory interests.

### **Securing the 90/10 Federal Match**

The successful implementation of the PMAS project is essential for maintaining the 90/10 federal funding match for Medicaid IT infrastructure. HHSC requires a journey-level professional who can ensure that all development work—from the design of analytical data marts to the automation of geoprocessing scripts—meets the rigorous federal standards for interoperability, security (HIPAA), and reporting accuracy. The cost of failure is immense, as a lapse in project delivery could jeopardize hundreds of millions in federal support.

### **Bridging the Capacity Gap for Executive Intelligence**

Leadership at HHSC currently suffers from a "data-rich but insight-poor" dynamic created by legacy infrastructure. The agency is hiring for this role to bridge the gap between complex technical databases (like Snowflake and Databricks) and the practical policy oversight needed by the Executive Commissioner and the 89th Legislature. The Analyst IV is expected to serve as a product owner who can take raw SQL output and transform it into executive-ready summaries and Tableau dashboards that drive high-level decisions.

### **Mandatory Fraud Detection and Risk Mitigation**

With the Governor’s January 2026 directive and SB 1 Rider 7, HHSC is under a strict mandate to identify and report utilization anomalies to the OIG. The agency needs a seasoned analyst with at least two years of SQL and Python experience to build the proactive detection models required to spot fraud, waste, and abuse in real-time. This position is critical for preventing overpayments, such as the $235,000 in excess payments recently identified by the OIG due to duplicate member IDs, and for protecting the overall integrity of the $82 billion Medicaid program.

## **Problem Resolution and Analyst Interventions**

The Performance Data Analyst IV will employ a variety of technical and consultative interventions to resolve the operational issues currently facing the HHSC PMAS unit.

### **Deployment of Automated Monitoring Systems**

To resolve the drain on staff resources caused by manual reporting, the analyst will leverage advanced SQL (using window functions and CTEs) and Python within the Snowflake/Databricks environment to automate data extractions. This replaces the manual processing of thousands of reports formerly submitted by MCOs for quality reviews of network adequacy and provider terminations. These automated pipelines will feed directly into Tableau dashboards, providing leadership with immediate visibility into MCO compliance with hotline call pick-up rates and claims adjudication timeliness.

### **Geospatial Solutions for Provider Network Adequacy (PNA)**

The analyst will directly address the challenge of healthcare access by using GIS (Geographic Information Systems) and geospatial mapping analysis. By integrating geocoding automation into the Provider+ data mart, the analyst will calculate geodistance and travel times between Medicaid clients and providers. These findings will be displayed in interactive dashboards, allowing the agency to identify specific counties or provider types where access standards (e.g., 30 miles for primary care in metro areas) are not being met, thereby providing the evidence needed for Liquidated Damages (LD) or Corrective Action Plans (CAP).

### **Proactive Anomaly and Outlier Detection**

The analyst will move the agency from a reactive audit posture to a proactive risk management model. By applying statistical modeling and forecasting in Databricks, the analyst will identify "highest priority anomalies" in service utilization—such as unusual patterns in psychotropic medication use for foster children or outliers in Autism service billing—long before they are flagged in formal audits. This proactive detection saves the state millions in potential overpayments and ensures that clinical services are reaching the intended populations in a cost-effective manner.

## **Operational Framework and Role Objectives**

The Performance Data Analyst IV operates within a dual-layered framework consisting of Agile Project Management and the rigorous HHSC Data Governance and Performance Management (DGPM) standards.

### **Core Role Objectives**

1. **Technical Architecture Support:** Facilitate the migration of program data into the Snowflake AI Data Cloud, ensuring that the new analytical layer is optimized for performance and security.  
2. **Compliance Oversight:** Monitor the contractual performance of Managed Care Organizations and other providers, ensuring they meet the quality and efficiency standards defined in the Uniform Managed Care Manual (UMCM).  
3. **Policy Translation:** Act as the expert interpreter who converts legislative mandates and federal rules into technical data specifications and KPIs.  
4. **Strategic Support and Training:** Provide ongoing consultation and training to program staff, enabling them to use modern data tools for evidence-based decision-making.

### **Operational Frameworks**

The unit utilizes the Scrum framework, an iterative Agile methodology that organizes work into time-bound "sprints". This allows the analyst to respond rapidly to evolving policy changes, such as the sudden mid-cycle requirement to report on maternal depression outcomes or new biomarker testing codes. Jira and Confluence are the primary tools for tracking progress, managing the technical backlog, and documenting metadata and business glossaries.  
Simultaneously, the role is governed by the HHSC Enterprise Information Management (EIM) Data Modeling Methodology Guidelines. These guidelines prescribe the standards for developing Conceptual, Logical, and Physical data models, ensuring that every data product is scalable, reusable, and interoperable across the $94 billion enterprise. All data handling must also comply with the Texas Risk and Authorization Management Program (TX-RAMP) and Section 508 accessibility standards.

## **Modern Health Tech Stack and Tool Integration**

The Performance Data Analyst’s tech stack represents a shift from "flexible/ad-hoc" tools to a "regulated enterprise" ecosystem designed for high data volumes and strict security.

| Stage of Workflow | Tooling Requirement | Functional Application |
| :---- | :---- | :---- |
| **Requirements & Agile** | **Jira / Confluence / Azure DevOps** | Backlog management, requirement tracking, and UAT test case documentation. |
| **Data Warehouse** | **Snowflake AI Data Cloud** | Centralized repository for structured and semi-structured health data; HIPAA-aligned semantic classification. |
| **Data Engineering** | **Databricks / Python (PySpark)** | Production-level ETL pipelines; predictive modeling and time-series forecasting for utilization trends. |
| **Statistical Analysis** | **SQL / Python / Excel** | Complex data manipulation using CTEs and window functions; ad-hoc statistical sampling. |
| **Visualization & BI** | **Tableau** | Executive-ready dashboards; geospatial mapping of provider networks and accessibility gaps. |
| **Geospatial Tools** | **ArcGIS / GeoPandas** | Geocoding automation; calculating travel distance and time standards per metro/micro/rural zones. |

The integration of these tools is demonstrated in the unit's routine projects. For example, data is extracted from legacy Oracle systems using Databricks notebooks, where it is cleansed and geocoded using Python. This cleaned data is then pushed into Snowflake, where multi-cluster compute power allows for rapid SQL-based aggregations. Finally, these metrics are surfaced in Tableau, which is embedded in the Medicaid Quality Performance website to provide public transparency into health plan report cards and medical pay-for-quality results.

## **Detailed Standard Operating Procedures and Process Manual**

The following SOP provides an exhaustive, step-by-step lifecycle for the work performed by the Performance Data Analyst IV, ensuring alignment with agency strategy and technical standards.

### **Phase 0: Strategic Intake and Governance Alignment**

The analyst begins every project by ensuring that the proposed work is legally mandated, ethically sound, and strategically aligned.  
**Step 1.1: Legislative and Policy Analysis.** Identify specific reporting requirements from new statutes, such as HB 26 (nutrition counseling) or SB 1 Rider 7 (anomaly reporting).

* *Action:* Review the bill text to identify "trigger" dates (e.g., September 1, 2025, effective date) and mandatory data points (e.g., "number of services delivered" and "respective costs").  
* *Constraint:* Ensure any new benefit additions follow the Texas Medicaid rate hearing process.

**Step 1.2: Strategic Consultation and Definition of Core KPIs.** Consult with the Director of Performance Analysis and MCS program staff to define the core performance metrics.

* *Action:* Formalize the definition of "performance" (e.g., numerator \= unique pregnant members receiving nutrition counseling; denominator \= all pregnant members in STAR program).

**Step 1.3: Data Governance and Security Review.** Verify that the project complies with the HHSC Data Governance and Performance Management (DGPM) standards.

* *Action:* Consult the Metadata Standard to identify authorized data elements and naming conventions.  
* *Security:* Confirm that all data processing and storage remains within the United States, as required by contract.

### **Phase 1: Requirements Engineering and Technical Specification**

The analyst converts the high-level policy needs into a detailed technical blueprint for development.  
**Step 2.1: Requirement Gathering and Documentation.** Interview subject matter experts from MCS Managed Care Utilization Review (MCUR) and Managed Care Contracts and Oversight (MCCO).

* *Action:* Document the functional requirements for data visualization, including required filters (e.g., Service Delivery Area, demographic groups, MCO name).

**Step 2.2: Data Mapping and Source Inventory.** Identify the location of all necessary data elements in legacy and modern systems.

* *Action:* Map claims data from TMHP, eligibility data from TIERS, and provider data from PEMS+ into a centralized "Data Mapping Matrix".

**Step 2.3: Agile Backlog Creation and Sizing.** Translate requirements into "User Stories" within Jira.

* *Action:* Define acceptance criteria and estimate story points for development phases (Ingestion, Modeling, QA, Visualization).

### **Phase 2: Data Ingestion and Multi-Source Integration (ETL/ELT)**

The analyst unifies disparate datasets into the agency's modern cloud infrastructure.  
**Step 3.1: Developing Extraction Workflows.** Use Databricks and SQL Server to extract data from legacy Oracle systems and MCO self-reported datasets (e.g., member complaints, hotlines).

* *Action:* Implement an ETL process that extracts self-reported data from the TexConnect database for network adequacy reviews.

**Step 3.2: Schema Normalization and Data Cleansing.** Apply Python scripts (pandas/PySpark) to normalize schemas and clean inconsistencies.

* *Action:* Resolve "dirty data" issues such as misspelled names or incorrect dates of birth that would otherwise skew geodistance calculations.

**Step 3.3: Loading into Snowflake AI Data Cloud.** Move validated and structured data into Snowflake, utilizing multi-cluster computing to ensure performance.

* *Action:* Apply Snowflake’s native semantic classifiers for medical and health data to automatically tag HIPAA-sensitive information such as ICD-10 codes and lab results.

### **Phase 3: Data Modeling and Complex Transformation**

The analyst builds the analytical foundations for performance monitoring.  
**Step 4.1: Building Fact and Dimension Tables.** Develop robust data models following the HHSC Data Modeling Methodology Guidelines (DMMG).

* *Action:* Create "Fact" tables for utilization (e.g., claims volume, amounts paid) and "Dimension" tables for geography, providers, and member demographics.  
* *Output:* Integrated Analytical Data Marts (e.g., Provider+ data mart).

**Step 4.2: Applying Advanced SQL Logic.** Develop optimized SQL views using Common Table Expressions (CTEs) and window functions.

* *Action:* Use window functions to calculate "Days since last service" or "Rolling average of call abandonment rates" for MCO hotlines.

**Step 4.3: Query Optimization for Visualization.** Refine query performance to support executive-level Tableau dashboards.

* *Action:* Utilize Snowflake’s separation of compute and storage to handle complex joins across massive claims datasets without degrading dashboard response times.

### **Phase 4: Data Quality and Validation Framework**

The analyst ensures that all performance data is "audit-ready" and compliant with legislative oversight.  
*Step 5.1: Exception Rule Implementation.* Define and implement data quality rules within the production pipeline.

* *Action:* Implement "null checks" for mandatory fields like NPI (National Provider Identifier) or Medicaid ID.

**Step 5.2: Reconciliation and Accuracy Verification.** Perform cross-system reconciliation to ensure data integrity.

* *Action:* Compare the total claims dollar amount in Snowflake against the legacy Oracle source to ensure 100% data fidelity during migration.

**Step 5.3: Anomaly and Outlier Detection.** Execute statistical models to identify unusual patterns that may indicate fraud or policy failure.

* *Action:* Present "highest priority anomaly findings" to the Service Utilization Workgroup, consisting of SMEs from policy, actuarial analysis, and clinical areas.

### **Phase 5: Pattern Recognition, Analytics, and Forecasting**

The analyst transforms data into predictive insights for agency leadership.  
**Step 6.1: Trend Analysis and Benchmarking.** Interpret historical and current data to identify long-term patterns.

* *Action:* Compare current service utilization rates against pre-pandemic baselines to normalize for the "Medicaid unwinding" effect.

**Step 6.2: Root Cause Analysis of Performance Gaps.** Identify the underlying causes for why an MCO or program area is failing to meet benchmarks.

* *Action:* Correlate performance failures (e.g., 50,000 provider enrollment delays) with specific system changes or policy rollouts like PEMS+.

**Step 6.3: Budgetary and Policy Impact Forecasting.** Develop projections for future program performance and the fiscal impact of proposed legislation.

* *Action:* Forecast the two-year net impact on General Revenue for bills like HB 26 through FFY 2027\.

### **Phase 6: Geospatial Analytics for Access to Care**

The analyst uses geographic data to ensure Texans can physically access the care they are entitled to.  
**Step 7.1: Geocoding Automation.** Standardize client and provider location data using the agency’s automated GIS pipeline.

* *Action:* Convert physical practice addresses into latitude and longitude coordinates for thousands of providers.

**Step 7.2: Time and Distance Measurement.** Use Spatial SQL or Python (GeoPandas) to calculate geodistance and travel times.

* *Action:* Map travel times against the standards defined in UMCM 5.28.1 (e.g., 30 minutes for Acute Care in metro areas; 75 minutes for Nursing Facilities in rural areas).

**Step 7.3: Network Adequacy Gap Identification.** Visualize accessibility by region to identify "care deserts".

* *Output:* Detailed "Access-to-Care" maps for inclusion in biennial legislative reports.

### **Phase 7: Visualization and Executive Support**

The analyst creates the public-facing and internal interfaces for performance data.  
**Step 8.1: Dashboard Design and Development.** Build interactive Tableau dashboards for MCO contract oversight and service utilization monitoring.

* *Action:* Design dashboards that allow leadership to filter by Program (STAR, CHIP), MCO, Service Delivery Area (SDA), and demographic factors.

**Step 8.2: Plain Language Narrative Translation.** Summarize technical findings into briefings for agency leaders and the legislature.

* *Action:* Convert complex window-function results into high-level KPI summaries that explain *why* utilization surged in a specific quarter.

**Step 8.3: Tableau Content Management.** Perform regular review, cleanup, and maintenance of Tableau server content to ensure data accuracy and user performance.

### **Phase 8: User Acceptance Testing (UAT) and System Readiness**

The analyst leads the final validation of new tools before they go live to program staff.  
**Step 9.1: Test Script Development.** Develop detailed test scripts and test documents for new system functionality in various environments.

* *Action:* Create step-by-step validation guides for non-technical testers to follow.

**Step 9.2: Coordination of Testing Cycles.** Lead teams of program staff through the UAT process, troubleshooting issues and submitting bug reports.

* *Action:* Manage the feedback loop using Azure DevOps or Jira to ensure all critical bugs are resolved before production release.

**Step 9.3: Production Readiness and Stakeholder Approval.** Obtain final sign-offs from MCS and DAP leadership.

### **Phase 9: Pipeline Automation and Orchestration**

The analyst moves the department from manual data pulls to a scheduled intelligence system.  
**Step 10.1: Scheduling Automated ETL Workflows.** Automate the execution of Databricks and Snowflake pipelines using enterprise orchestrators like Azure Data Factory.

* *Action:* Ensure data is refreshed on a daily or weekly cadence to support real-time oversight.

**Step 10.2: Configuring Automated Performance Alerts.** Implement automated alerts for performance anomalies or data quality failures.

* *Action:* Set up email or Slack notifications for MCCO staff if an MCO’s clean claim rate falls below 98%.

### **Phase 10: Stakeholder Support and Stakeholder Enablement**

The analyst ensures the data products are adopted and effectively used by the agency.  
**Step 11.1: Staff Training and Support.** Train program staff on new Tableau dashboards and data analysis tools.

* *Action:* Provide ongoing user support and troubleshooting for technical issues identified by frontline workers.

**Step 11.2: Technical Assistance for Policy Evolution.** Provide consultative services to programs seeking to establish *new* metrics or refine existing measures in response to legislation.  
**Step 11.3: Continuous Product Improvement.** Identify future data product needs or additional features to be included in future 90/10 implementation cycles.

## **Causal Insights and Second-Order Implications**

The integration of a journey-level Performance Data Analyst into the PMAS unit creates several profound ripple effects across the HHSC enterprise.

### **The Direct Link Between Analysis and Fiscal Sustainability**

There is a direct causal relationship between the analyst’s performance in the PMAS IAPDU project and the agency’s fiscal health. By successfully completing the UAT and deployment phases of the modern analytical layer, the analyst ensures the state remains eligible for the $119 million in enhanced federal funding. This federal investment offsets the state's General Revenue (GR) costs, allowing Texas to reallocate funds toward high-priority areas like the $436 million appropriation for personal care attendant wage increases or the expansion of women's preventative health units.

### **Data Transparency as a Market Incentive**

The creation of Tableau-based "Quality Performance Report" (QPR) dashboards introduces a competitive dynamic to the Medicaid managed care marketplace. When the analyst publishes accurate, granular data on MCO hotline abandonment rates and claims processing timeliness, it provides a public benchmark that MCOs must meet to avoid sanctions or Corrective Action Plans (CAPs). This data-driven transparency effectively acts as a low-cost mechanism for improving clinical quality and administrative efficiency without the need for additional regulatory staffing.

### **Proactive Detection and the "OIG Feedback Loop"**

The mandate under SB 1 Rider 7 to report anomalies to the OIG creates a critical new feedback loop. As the Performance Data Analyst identifies billing outliers in high-risk areas like Autism services, the OIG can initiate audits earlier in the cycle. This proactive intervention prevents the accumulation of massive overpayments—similar to the $922,000 in unallowable CHIP capitation payments previously identified—thereby preserving the integrity of the state’s safety net programs.

### **The Evolution of the "Data Analyst" Professional Standard**

The requirements for this role—advanced SQL, Python, Snowflake, and policy expertise—signal a fundamental shift in the professional standards for public sector employment in Texas. The "Data Analyst IV" is no longer a clerical role but a strategic technical leader who must understand the nuances of the 89th Legislature's intent as deeply as they understand a database schema. This indicates that data literacy and technical proficiency have become the core competencies required for modern public administration.

## **Conclusion: The Analyst as the Engine of Quality Management**

The role of the Performance Data Analyst IV within the HHSC PMAS department is foundational to the agency's success in navigating the 2026-2027 biennium. By April 19, 2026, the analyst serves as the primary technical catalyst for converting a $1.1 billion IT investment into a connected, efficient, and transparent healthcare system for 7.5 million Texans.  
The meticulous execution of the 10-phase master workflow ensures that HHSC moves from a reactive, legacy-burdened state to a proactive, "data-liquid" organization capable of identifying fraud, improving provider network adequacy, and making evidence-based policy shifts. In an environment where the state legislature and the public demand absolute transparency and fiscal accountability, the analyst provides the technical rigor and policy insight required to protect the state’s resources while ensuring that the most vulnerable residents of Texas receive the high-quality care they are entitled to. Through the bridge-building efforts in Austin, the agency is positioned to meet its mission of "Making a positive difference in the lives of the people we serve" with unprecedented precision and integrity.

#### **Works cited**

1\. Search About | Texas Health and Human Services, https://www.hhs.texas.gov/about?facets\_query=\&page=17\&search-about-hhs= 2\. Presentation to the Senate Committee on Health and Human Services \- Aril 2026, https://www.hhs.texas.gov/sites/default/files/documents/senate-hhs-presentation-2026.pdf 3\. LSG Analysis of the House-Introduced Budget \- Texas Legislative Study Group, https://texaslsg.org/2025/02/10/lsg-analysis-of-the-house-introduced-budget/ 4\. Senate Finance Committee Reviews HHSC Budget \- Texas Association of Counties, https://www.county.org/resources/news/county-issues/2025/february-7/budget 5\. SB 1 Is in Effect: See What Every Texan Is Tracking, https://everytexan.org/2026/02/11/sb-1-is-in-effect-see-what-every-texan-is-tracking/ 6\. Executive Teams and Organizational Charts \- Texas Health and Human Services, https://www.hhs.texas.gov/about/about-us/executive-teams-organizational-charts 7\. Data and Statistics | Texas Health and Human Services, https://www.hhs.texas.gov/about/records-statistics/data-statistics 8\. HHSC Outlines Organizational Realignment \- Texas Health and Human Services, https://www.hhs.texas.gov/news/2026/03/hhsc-outlines-organizational-realignment 9\. HHSC New Organizational Realignment Outline \- Twogether Consulting, https://twogetherconsulting.com/hhsc-new-organizational-realignment-outline/ 10\. Director, Office of Data, Analytics and Performance, Calvin Green, https://www.hhs.texas.gov/about/about-us/executive-teams-organizational-charts/director-office-data-analytics-performance-calvin-green 11\. Performance Data Analyst Job Details | TX-HHSC-DSHS-DFPS, https://careers.hhs.texas.gov/hhscjobs/job/AUSTIN-Performance-Data-Analyst-TX-73301/1367419200/ 12\. SMD \# 16-009 Mechanized Claims Processing and Information Retrieval Systems – APD Requirements \- Medicaid, https://www.medicaid.gov/federal-policy-guidance/downloads/smd16009.pdf 13\. A Step-by-Step Guide for Health Departments Seeking HIT/HIE Funding Via the 90/10 Medicaid Match, https://phii.org/download/a-step-by-step-guide-for-health-departments-seeking-hit-hie-funding-via-the-90-10-medicaid-match/?wpdmdl=15548\&masterkey=6179c51b6b471 14\. Advanced Planning Documents (APD) for System Development Associated with 1115 Demonstrations \- Medicaid, https://www.medicaid.gov/federal-policy-guidance/downloads/faq061319.pdf 15\. Module 1 Information Sheet on the CMS HITECH 90-10 Funding Program \- Public Health Informatics Institute, https://phii.org/wp-content/uploads/2021/10/1.-Information-Sheet-on-the-HITECH-90-10-Program.pdf 16\. Medicaid CHIP Data Analytics Unit-Quarterly Report of Activities \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-unit-quarterly-report-activities-sfy-2025-q2.pdf 17\. Medicaid CHIP Data Analytics Unit-Quarterly Report of Activities State Fiscal Year 2025 Quarter 3, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-unit-quarterly-report-activities-sfy-2025-q3.pdf 18\. Medicaid CHIP Data Analytics Unit Annual Report of Activities State Fiscal Year 2025, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-unit-annual-report-of-activities-sfy-2025.pdf 19\. Texas Health and Human Services Commission \- Industry Insider, https://insider.govtech.com/texas/tag/texas-health-and-human-services-commission 20\. Texas Governor Issues New Directive on Medicaid Fraud Enforcement- Five Things That Managed Care Organizations Should Do Now, https://natlawreview.com/article/texas-governor-issues-new-directive-medicaid-fraud-enforcement-five-things-managed 21\. Texas Budget and CIOs Signal Major IT Overhauls in 2026 \- Industry Insider, https://insider.govtech.com/texas/news/texas-budget-and-cios-signal-major-it-overhauls-in-2026 22\. Medicaid Managed Care: Top Issues for Advocates in 2026 \- Families USA, https://familiesusa.org/wp-content/uploads/2026/01/MCO-2026-Top-Priorities\_Final.pdf 23\. 3 Predictions Impacting the Public Sector in 2026 \- Snowflake, https://www.snowflake.com/en/blog/ai-predictions-public-sector-2026/ 24\. Healthcare AI Data Solutions: 2026 Interoperability Research Report \- Snowflake, https://www.snowflake.com/en/blog/ai-interoperability-healthcare/ 25\. The Modern Data Stack in 2026: Transformation in Healthcare, Finance & Government, https://www.alation.com/blog/modern-data-stack-regulated-industries-2026/ 26\. SOW 781-4-02321 Snowflake Data Submission \- THECB Report Center, https://reportcenter.highered.texas.gov/agency-publication/sow-781-4-02321-snowflake-data-submission/sow-no-781-4-02321-questions-and-answerspdf/ 27\. Texas HHSC Alert \- PEMS+ Project Go-Live Plan \- UHC provider portal, https://www.uhcprovider.com/content/dam/provider/docs/public/commplan/tx/hhs-messages/TX-HHSC-Alert-PEMS-Go-Live.pdf 28\. HB 4666 \- 89th Legislature \- Texas Policy Research, https://www.texaspolicyresearch.com/bills/89th-legislature-hb-4666/ 29\. Supplement: TX HB26 | 2025-2026 | 89th Legislature | Fiscal Note (Introduced) \- LegiScan, https://legiscan.com/TX/supplement/HB26/id/542447 30\. HB 26 \- 89th Legislature \- Texas Policy Research, https://www.texaspolicyresearch.com/bills/89th-legislature-hb-26/ 31\. 89(R) HB 26 \- Engrossed version \- Bill Text \- Texas Legislature Online, https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00026E.htm 32\. HHS Locations \- Texas Health and Human Services, https://www.hhs.texas.gov/contact/hhs-locations 33\. Quality Review Unit Data Analyst IV in Austin \- Talents by Vaia, https://talents.vaia.com/companies/texas-health-human-services-commission/austin/quality-review-unit-data-analyst-iv-73257265/ 34\. Crunching the Numbers: Analysis of 2026 Healthcare Predictions \- Trilliant Health, https://www.trillianthealth.com/market-research/studies/analysis-of-2026-healthcare-predictions 35\. Texas Medicaid Enrollment, Eligibility Systems Get Modernization Funding, https://www.texmed.org/Template.aspx?id=66566 36\. Congress Passed their Mega-Bill. What Does the Texas Legislature Do Now?, https://txchildren.org/congress-passed-their-mega-bill-what-does-the-texas-legislature-do-now/ 37\. Multiple Identification Numbers in Texas Medicaid and CHIP \- Office of Inspector General, https://oig.hhs.texas.gov/sites/default/files/documents/multiple\_texas\_medicaid\_and\_chip\_ids\_hhsc\_aes\_accessible.pdf 38\. Texas HHS Signals Stricter Procurement Standards \- Industry Insider, https://insider.govtech.com/texas/news/texas-hhs-signals-stricter-procurement-standards 39\. Data Analyst Job Details | TX-HHSC-DSHS-DFPS, https://careers.hhs.texas.gov/hhscjobs/job/AUSTIN-Data-Analyst-TX-73301/1364908200/ 40\. Vendor Resources | Texas Health and Human Services, https://www.hhs.texas.gov/business/contracting-hhs/vendor-resources 41\. Health and Human Services State Medicaid Managed Care Advisory Committee (SMMCAC) Clinical Oversight and Administrative Simplifi \- Texas Insight, https://www.txinsight.com/wp-content/uploads/2026/02/Clinical-Oversight-and-Administrative-Simplification-2-12-2026.pdf 42\. Texas Medicaid Behavioral Health 2026 Updates \- The Medicators, https://themedicators.com/texas-medicaid-behavioral-health-2026/ 43\. Managed Care Organization Sanctions \- Texas Health and Human Services, https://www.hhs.texas.gov/services/health/medicaid-chip/managed-care-contract-management/managed-care-organization-sanctions 44\. Quality Assurance Analyst Job Details | TX-HHSC-DSHS-DFPS, https://careers.hhs.texas.gov/hhscjobs/job/AUSTIN-Quality-Assurance-Analyst-TX-73301/1356156100/ 45\. IMPORTANT: Compliance with U.S.-Only Performance and Data Handling Requirements \- Foster Care Texas, https://www.fostercaretx.com/newsroom/important-compliance-with-us-only-performance-and-data-handling-requirements-07152025.html 46\. Texas Sunset Commission Health and Human Services Commission Review as of October 22, 2025 \- Texas Insight, https://www.txinsight.com/texas-sunset-commission-health-and-human-services-commission-review/ 47\. MACPAC Holds January 2026 Meeting \- Applied Policy, https://www.appliedpolicy.com/macpac-holds-january-2026-meeting/ 48\. Performance Data Analyst @ TX-HHSC-DSHS-DFPS \- Teal, https://www.tealhq.com/job/performance-data-analyst\_7ea1aba50c8f7d8fb437325c4736248154dc7 49\. SB 1 \- 89th Legislature \- Texas Policy Research, https://www.texaspolicyresearch.com/bills/89th-legislature-sb-1/ 50\. Medicaid CHIP Data Analytics Unit Annual Report of Activities State Fiscal Year 2024, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-unit-annual-report-of-activities-sfy-2024-q4.pdf 51\. Medicaid CHIP Data Analytics Quarterly Report \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-q4-report-oct-2022.pdf 52\. Medicaid CHIP Data Analytics Quarterly Report Revised March 2024 \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/medicaid-chip-data-analytics-unit-quarterly-report-activities-sfy-2024-q2.pdf 53\. Medicaid Managed Care Provider Network Adequacy Report \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/sb760-medicaid-managed-care-provider-network-adequacy-dec-2022.pdf 54\. UMCM 5.28.1 \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/laws-regulations/handbooks/umcm/5-28-1.xlsx 55\. Five Key Issues Shaping Medicaid in 2026 and Beyond \- Myers and Stauffer, https://myersandstauffer.com/insights/five-key-issues-shaping-medicaid-in-2026-and-beyond/ 56\. Texas Medicaid and CHIP \- Uniform Managed Care Manual, https://www.hhs.texas.gov/services/health/medicaid-chip/managed-care-contract-management/texas-medicaid-chip-uniform-managed-care-manual 57\. Pay-for-Quality (P4Q) Programs \- Texas Health and Human Services, https://www.hhs.texas.gov/about/process-improvement/improving-services-texans/medicaid-chip-quality-efficiency-improvement/pay-quality-p4q-programs 58\. Why Jira for agile project management? \- Atlassian, https://www.atlassian.com/jira/solutions/agile-project-management 59\. Day 16: Agile Scrum Framework With Jira Software Demo | Project Management \- YouTube, https://www.youtube.com/watch?v=bEnKXtlblqk 60\. Agile Guide for Major Information Resources Projects (MIRPs) \- Quality Assurance Team, https://qat.dir.texas.gov/mirp\_guide.pdf 61\. Health and Human Services Medicaid Advisory Committee February 12, 2026 \- Texas Insight, https://www.txinsight.com/wp-content/uploads/2026/02/MAC-February-12-2026.pdf 62\. Reports and Presentations | Texas Health and Human Services, https://www.hhs.texas.gov/regulations/reports-presentations?f%5B0%5D=report\_category%3A126\&f%5B1%5D=report\_category%3A386\&page=1\&reports-search= 63\. Enterprise Information Management Data Modeling Methodology Guidelines \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/hhsc-data-modeling-methodology-guidelines.pdf 64\. SHARP for NEDSS Users | Texas DSHS, https://www.dshs.texas.gov/sharp-nedss-users 65\. How to Build ETL Data Pipelines for the Healthcare Industry | Integrate.io, https://www.integrate.io/blog/data-pipelines-healthcare/ 66\. Scalability of Snowflake Data Warehousing in Multi-State Medicaid Data Processing \- International Journal of Emerging Research in Engineering and Technology, http://ijeret.org/index.php/ijeret/article/download/163/151 67\. Scalability of Snowflake Data Warehousing in Multi-State Medicaid Data Processing, https://jrtcse.com/index.php/home/article/view/JRTCSE.2024.1.8 68\. Medicaid CHIP Quality and Efficiency Improvement Data and Reports, https://www.hhs.texas.gov/about/process-improvement/improving-services-texans/medicaid-chip-quality-efficiency-improvement/medicaid-chip-quality-efficiency-improvement-data-reports 69\. Medicaid Quality Performance \- Texas.gov, https://mqp.hhs.texas.gov/ 70\. First Quarter 2026 HCPCS Updates for Texas Medicaid \- TMHP, https://www.tmhp.com/news/2026-04-01-first-quarter-2026-hcpcs-updates-texas-medicaid 71\. Coming April 2026: First Quarter HCPCS Updates to Texas Medicaid Procedure Codes, https://www.tmhp.com/news/2026-02-13-coming-april-2026-first-quarter-hcpcs-updates-texas-medicaid-procedure-codes 72\. 2026 Texas Care Provider Manual \- UnitedHealthcare Community Plan of Texas, https://www.uhcprovider.com/content/dam/provider/docs/public/admin-guides/comm-plan/TX-UHCCP-Care-Provider-Manual.pdf 73\. Operating Structure \- Vision 2026 \- Texas Health Resources, https://www2.texashealth.org/videosite/operating.html 74\. Employee background check and training issues found during OIG inspection \- Texas.gov, https://oig.hhs.texas.gov/about-us/news/employee-background-check-and-training-issues-found-during-oig-inspection 75\. Apr 3, 2026: Medical and health data classifiers in sensitive data classification (General availability) | Snowflake Documentation, https://docs.snowflake.com/en/release-notes/2026/other/2026-04-03-sensitive-data-classification-medical-health-ga 76\. Data Analyst \- Texas Health and Human Services Commission \- Austin, TX | Ladders, https://www.theladders.com/job/data-analyst-texas-health-and-human-services-commission-austin-tx\_85707168 77\. CAP Website February 2026 \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/managed-care-action-plan-feb-2026.pdf 78\. STATE OF TEXAS MEDICAID MANAGED CARE STAR HEALTH PROGRAM RATE SETTING STATE FISCAL YEAR 2026, https://pfd.hhs.texas.gov/sites/default/files/documents/managed-care/2026/2026-ffy-star-health-rates.pdf 79\. How Health Plans Can Meet 2026 Network Adequacy Requirements \- Verisys, https://verisys.com/blog/how-health-plans-can-meet-network-adequacy-standards/ 80\. Nursing Facility Minimum Performance Standards | Texas Health and Human Services, https://www.hhs.texas.gov/providers/long-term-care-providers/nursing-facilities-nf/quality-monitoring-program-qmp/nursing-facility-minimum-performance-standards 81\. Tableau Data Analyst at Texas Health And Human Services in Austin, Tx | Jobrapido.com, https://us.jobrapido.com/jobpreview/197302076647145472 82\. Uniform Managed Care Claims Manual \- Medical Pay-for-Quality (P4Q) Program \- Texas Health and Human Services, https://www.hhs.texas.gov/sites/default/files/documents/laws-regulations/handbooks/umcm/6-2-14.pdf 83\. Data Analyst \- Texas State Auditor's Office, https://hr.sao.texas.gov/Compensation/Archives/2025/JobDescriptions/R0652.pdf 84\. About Us \- Texas Health and Human Services, https://www.hhs.texas.gov/about/about-us