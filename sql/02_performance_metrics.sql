-- Members with at least one claim within county (proxy for access-to-care)
CREATE OR REPLACE VIEW `driiiportfolio.medicaid.vw_member_access` AS
SELECT
  m.member_id,
  m.county AS member_county,
  COUNT(DISTINCT c.provider_id) AS providers_seen,
  COUNTIF(c.provider_type = 'Primary Care') AS primary_care_visits
FROM `driiiportfolio.medicaid.members` m
LEFT JOIN `driiiportfolio.medicaid.claims` c ON c.member_id = m.member_id
GROUP BY 1,2;

-- Network adequacy: providers per county
CREATE OR REPLACE VIEW `driiiportfolio.medicaid.vw_provider_density` AS
SELECT
  county,
  provider_type,
  COUNT(DISTINCT provider_id) AS num_providers
FROM `driiiportfolio.medicaid.providers`
GROUP BY county, provider_type;
