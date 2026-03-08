import pandas as pd

# 1. Check version
print(f"Pandas Version: {pd.__version__}")

# 2. Create a small test table (DataFrame)
data = {
    'Topic': ['Installation', 'Importing', 'Testing'],
    'Status': ['Done', 'Done', 'In Progress']
}

df = pd.DataFrame(data)

print("\n--- Your Progress Table ---")
print(df)