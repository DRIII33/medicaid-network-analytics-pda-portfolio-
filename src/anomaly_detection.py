import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
claims = pd.read_csv('claims_clean.csv')
providers = pd.read_csv('providers_clean.csv')
members = pd.read_csv('members_clean.csv')

# --- 1. Provider Claim Volume Outlier Detection (99th Percentile Rule) ---

claim_counts = claims.groupby('provider_id').size().reset_index(name='n_claims')
p99 = np.percentile(claim_counts['n_claims'], 99)
outlier_providers = claim_counts[claim_counts['n_claims'] > p99]

print("Providers above 99th percentile claim volume:")
print(outlier_providers)

# Visualize
plt.figure(figsize=(8,4))
sns.histplot(claim_counts['n_claims'], bins=30, kde=True)
plt.axvline(p99, color='red', linestyle='dashed', label=f'99th percentile: {int(p99)} claims')
plt.title('Distribution of Claims per Provider (99th Percentile Outlier)')
plt.xlabel('Claims per Provider')
plt.ylabel('Provider Count')
plt.legend()
plt.tight_layout()
plt.show()


# --- 2. Z-score Based Outlier Detection (for claim amount) ---

claims['amount_zscore'] = (claims['amount_paid'] - claims['amount_paid'].mean()) / claims['amount_paid'].std()
outlier_claims = claims[np.abs(claims['amount_zscore']) > 3]

print(f"\nClaims with amount >3 standard deviations from mean: {len(outlier_claims)}")
if not outlier_claims.empty:
    print(outlier_claims[['claim_id', 'provider_id', 'amount_paid', 'amount_zscore']].head())

# Visualize
plt.figure(figsize=(8,4))
sns.boxplot(x=claims['amount_paid'])
plt.title("Boxplot: Amount Paid per Claim (Detecting Outliers)")
plt.xlabel("Amount Paid ($)")
plt.tight_layout()
plt.show()


# --- 3. Duplicate Member ID Use Across Providers (Potential Red Flag) ---

claims['claim_week'] = pd.to_datetime(claims['claim_date']).dt.isocalendar().week

member_provider_week = claims.groupby(['member_id', 'claim_week'])['provider_id'].nunique().reset_index()
potential_duplicates = member_provider_week[member_provider_week['provider_id'] > 1]

print(f"\nMember-week pairs with claims from multiple providers: {potential_duplicates.shape[0]}")

# Show some
print(potential_duplicates.head())

# --- 4. Simple Clustering for Provider Claim Pattern Anomalies ---

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Features: total claims and mean amount_paid per provider
provider_features = claims.groupby('provider_id').agg(
    n_claims=('claim_id', 'count'),
    avg_paid=('amount_paid', 'mean')
).reset_index()

scaler = StandardScaler()
X = scaler.fit_transform(provider_features[['n_claims', 'avg_paid']])

kmeans = KMeans(n_clusters=3, random_state=0)
provider_features['cluster'] = kmeans.fit_predict(X)

# Visualize clustering
plt.figure(figsize=(6,4))
sns.scatterplot(x='n_claims', y='avg_paid', data=provider_features, hue='cluster', palette='Set2')
plt.title("KMeans Clustering of Providers by Claim Volume and Avg Paid")
plt.xlabel("Total Claims")
plt.ylabel("Average Paid per Claim")
plt.tight_layout()
plt.show()

# Save identified high-risk providers (outliers and odd clusters)
provider_features.to_csv('provider_anomaly_scores.csv', index=False)
print("\nSaved provider-level anomaly cluster assignments to provider_anomaly_scores.csv.")

# --- 5. Summary Table of Anomalies ---

anomaly_summary = {
    'total_providers': claim_counts.shape[0],
    'providers_above_99pct': outlier_providers.shape[0],
    'high_zscore_claims': outlier_claims.shape[0],
    'member_id_multi_provider_weeks': potential_duplicates.shape[0],
}

print("\nAnomaly Summary:")
for k, v in anomaly_summary.items():
    print(f"{k}: {v}")

# End of script
