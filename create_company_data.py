import pandas as pd

# Sample data for the DataFrame
data = {
    "company_name": ["Kuat Drive Yards", "Incom Corporation", "Sienar Fleet Systems", 
                     "Corellian Engineering Corporation", "Mon Calamari Shipyards", 
                     "TaggeCo", "Czerka Corporation", "Trade Federation", 
                     "Techno Union", "Holowan Mechanicals"],
    "company_planet": ["Kuat", "Naboo", "Coruscant", "Corellia", "Mon Cala", 
                       "Tatooine", "Kashyyyk", "Geonosis", "Mustafar", "Kamino"],
    "company_CEO": ["Kuat of Kuat", "Padmé Amidala", "Palpatine", 
                    "Han Solo", "Admiral Ackbar", "Jabba the Hutt", 
                    "Chewbacca", "Poggle the Lesser", "Darth Vader", "Lama Su"],
    "revenue": [5000000, 7500000, 2000000, 1500000, 
                3000000, 1000000, 8500000, 1000000, 
                7500000, 5000000],
    "company_age": [300, 20, 100, 200, 10, 5, 250, 50, 10, 30]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Add an auto-incrementing primary key
df['company_id'] = range(1, len(df) + 1)

# Set the 'company_id' as the first column
df = df[['company_id', 'company_name', 'company_planet', 'company_CEO', 'revenue', 'company_age']]

# Display the DataFrame
print(df)
df.to_csv("./company_data.csv", index=False)