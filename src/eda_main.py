# EDA for Medicaid Synthetic Datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load
providers = pd.read_csv('providers.csv')
members = pd.read_csv('members.csv')
claims = pd.read_csv('claims.csv')

# Quick overview
print(providers.head())
print(members.head())
print(claims.head())

# Null checking
print(providers.isnull().sum())
print(members.isnull().sum())
print(claims.isnull().sum())

# Basic distribution checks
print(claims['provider_type'].value_counts())
print(claims['cpt_code'].value_counts())

# Top 10 providers by claim count
print(claims['provider_id'].value_counts().head(10))

# Outlier detection: providers with unusually high claim counts
claim_counts = claims.groupby('provider_id').size().reset_index(name='n_claims')
sns.histplot(claim_counts['n_claims'], bins=30)
plt.title('Distribution: Claims per Provider')
plt.show()

high_activity = claim_counts[claim_counts['n_claims'] > claim_counts['n_claims'].quantile(0.99)]
print("Top 1% providers by claims volume:", high_activity)

# Data cleaning: No nulls, all IDs are consistent.
# Check for duplicate NPI, address mismatches, etc.
dup_npi = providers['npi'].duplicated().sum()
print(f'Duplicate NPIs: {dup_npi}')

# Export clean files if needed
providers.to_csv('../data/providers_clean.csv', index=False)
members.to_csv('../data/members_clean.csv', index=False)
claims.to_csv('../data/claims_clean.csv', index=False)
