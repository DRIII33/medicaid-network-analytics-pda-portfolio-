CREATE OR REPLACE VIEW `driiiportfolio.medicaid.view_provider_density_scorecard` AS
SELECT
  density.county,
  density.provider_type,
  density.num_providers,
  member_counts.total_members,
  -- Calculation: num_providers / (total_members / 1000)
  SAFE_DIVIDE(density.num_providers, (member_counts.total_members / 1000)) AS providers_per_1000_members
FROM
  `driiiportfolio.medicaid.vw_provider_density` AS density
INNER JOIN (
  SELECT
    members.county,
    COUNT(DISTINCT members.member_id) AS total_members
  FROM
    `driiiportfolio.medicaid.members` AS members
  GROUP BY
    members.county
) AS member_counts
  ON density.county = member_counts.county;
