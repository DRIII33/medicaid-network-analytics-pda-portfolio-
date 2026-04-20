# Generates realistic provider, member, and claims datasets for Medicaid analytics

import pandas as pd
import numpy as np
from faker import Faker

faker = Faker()
np.random.seed(42)

# --- Providers Data ---
n_providers = 500
provider_types = ['Primary Care', 'Specialist', 'Pediatrics', 'Mental Health', 'Nutritionist']
counties = ['Travis', 'Williamson', 'Hays', 'Bexar', 'Dallas', 'Harris', 'El Paso', 'Tarrant']

providers = []
for i in range(1, n_providers + 1):
    ptype = np.random.choice(provider_types, p=[0.4, 0.25, 0.15, 0.1, 0.1])
    providers.append({
        'provider_id': f'PRV{i:04}',
        'provider_name': faker.company(),
        'provider_type': ptype,
        'county': np.random.choice(counties),
        'address': faker.address().replace('\n', ', '),
        'npi': faker.unique.random_number(digits=10)
    })
providers_df = pd.DataFrame(providers)

# --- Members Data ---
n_members = 5000
members = []
for i in range(1, n_members + 1):
    age = np.random.randint(0, 90)
    gender = np.random.choice(['F', 'M'])
    members.append({
        'member_id': f'MEM{i:05}',
        'dob': faker.date_of_birth(minimum_age=age, maximum_age=age),
        'age': age,  # redundant but useful
        'gender': gender,
        'county': np.random.choice(counties),
        'address': faker.address().replace('\n', ', '),
    })
members_df = pd.DataFrame(members)

# --- Claims Data ---
n_claims = 20000
claim_status = ['Paid', 'Denied', 'Pending']
all_cpt = ['99213', '99214', '97802', '97803', '90791', '90834']  # Office, Nutrition, Mental Health

claims = []
for i in range(1, n_claims + 1):
    member = members_df.sample(1).iloc[0]
    provider = providers_df.sample(1).iloc[0]
    claims.append({
        'claim_id': f'CLM{i:06}',
        'member_id': member['member_id'],
        'provider_id': provider['provider_id'],
        'provider_type': provider['provider_type'],
        'claim_date': faker.date_between(start_date='-1y', end_date='today'),
        'amount_paid': np.round(np.random.uniform(50, 400), 2),
        'cpt_code': np.random.choice(all_cpt, p=[0.4, 0.3, 0.08, 0.08, 0.07, 0.07]),
        'status': np.random.choice(claim_status, p=[0.80, 0.1, 0.1])
    })
claims_df = pd.DataFrame(claims)

# Export as CSV
providers_df.to_csv('providers.csv', index=False)
members_df.to_csv('members.csv', index=False)
claims_df.to_csv('claims.csv', index=False)

print("Synthetic datasets generated and saved as CSV.")
