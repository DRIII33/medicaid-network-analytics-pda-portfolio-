-- Fraud risk: high claim volume (>99th percentile) per provider
CREATE OR REPLACE VIEW `driiiportfolio.medicaid.vw_provider_outliers` AS
WITH provider_counts AS (
  SELECT
    provider_id,
    COUNT(*) AS total_claims
  FROM `driiiportfolio.medicaid.claims`
  GROUP BY provider_id
),
threshold AS (
  SELECT
    APPROX_QUANTILES(total_claims, 100)[OFFSET(99)] AS p99_claims
  FROM provider_counts
)
SELECT
  p.provider_id,
  p.total_claims,
  t.p99_claims
FROM provider_counts p, threshold t
WHERE p.total_claims > t.p99_claims;
