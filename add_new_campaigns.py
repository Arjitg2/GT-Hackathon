"""
Script to add new campaign columns to demonstrate future-proof capability
"""
import pandas as pd

# Load data
df = pd.read_csv('marketing_campaign.csv', sep=';')

print("=" * 60)
print("ADDING NEW CAMPAIGN COLUMNS")
print("=" * 60)

# Show current campaign columns
current_campaigns = [col for col in df.columns if col.startswith('AcceptedCmp') or col == 'Response']
print(f"\nCurrent campaigns: {current_campaigns}")

# Add two new campaign columns
print("\nAdding new campaigns: AcceptedCmp6, AcceptedCmp7")

# Campaign 6: Random 100 customers accepted
import random
random.seed(123)
df['AcceptedCmp6'] = 0
campaign6_acceptors = random.sample(range(len(df)), 100)
df.loc[campaign6_acceptors, 'AcceptedCmp6'] = 1

# Campaign 7: Random 75 customers accepted
df['AcceptedCmp7'] = 0
campaign7_acceptors = random.sample(range(len(df)), 75)
df.loc[campaign7_acceptors, 'AcceptedCmp7'] = 1

# Show new campaign columns
new_campaigns = [col for col in df.columns if col.startswith('AcceptedCmp') or col == 'Response']
print(f"New campaigns: {new_campaigns}")

print(f"\nAcceptedCmp6: {df['AcceptedCmp6'].sum()} acceptances")
print(f"AcceptedCmp7: {df['AcceptedCmp7'].sum()} acceptances")

# Save modified data
df.to_csv('marketing_campaign.csv', sep=';', index=False)
print("\n[OK] Data saved with new campaigns!")
print("=" * 60)
