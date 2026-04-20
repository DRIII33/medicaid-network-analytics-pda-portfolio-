CREATE OR REPLACE VIEW `driiiportfolio.medicaid.view_primary_care_access_rate` AS
WITH child_members AS (
  SELECT
    members.member_id,
    members.age,
    members.county
  FROM
    `driiiportfolio.medicaid.members` AS members
  WHERE
    members.age < 18
),
recent_pc_claims AS (
  SELECT DISTINCT
    claims.member_id
  FROM
    `driiiportfolio.medicaid.claims` AS claims
  WHERE
    claims.cpt_code IN ('99213', '99214')
    -- Filtering for services in the "last year" relative to current date 2026-04-19
    AND claims.claim_date >= DATE_SUB(DATE '2026-04-19', INTERVAL 1 YEAR)
)
SELECT
  cm.member_id,
  cm.age,
  cm.county,
  -- Calculated Field: 1 if visit exists, else 0
  CASE WHEN rpc.member_id IS NOT NULL THEN 1 ELSE 0 END AS has_primary_care_visit
FROM
  child_members AS cm
LEFT JOIN
  recent_pc_claims AS rpc
  ON cm.member_id = rpc.member_id;
