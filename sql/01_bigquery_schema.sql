-- Run in BigQuery with driiiportfolio as project
CREATE OR REPLACE TABLE `driiiportfolio.medicaid.providers` (
  provider_id STRING,
  provider_name STRING,
  provider_type STRING,
  county STRING,
  address STRING,
  npi STRING
);
CREATE OR REPLACE TABLE `driiiportfolio.medicaid.members` (
  member_id STRING,
  dob DATE,
  age INT64,
  gender STRING,
  county STRING,
  address STRING
);
CREATE OR REPLACE TABLE `driiiportfolio.medicaid.claims` (
  claim_id STRING,
  member_id STRING,
  provider_id STRING,
  provider_type STRING,
  claim_date DATE,
  amount_paid FLOAT64,
  cpt_code STRING,
  status STRING
);
