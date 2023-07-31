import pandas as pd

# Load the athlete_events and noc_regions CSV files into dataframes
athlete_events = pd.read_csv("athlete_events.csv",header=0)
noc_regions = pd.read_csv("noc_regions.csv",header=0)

print(noc_regions.columns.tolist())
print(athlete_events.columns.to_list())
# Create a dictionary mapping NOC codes to regions
nocs_to_regions = noc_regions.set_index('NOC')['region'].to_dict()

# Replace the NOC acronyms with regions in the athlete_events dataframe
athlete_events['NOC'] = athlete_events['NOC'].map(nocs_to_regions)

# Replace "NA" with blank values in the "Medal" column
athlete_events['Medal'] = athlete_events['Medal'].replace('NA', '')

#Splitting Games column into Year and Season
athlete_events['Year'] = athlete_events['Games'].str.extract('(\d{4})')
athlete_events['Season'] = athlete_events['Games'].str.extract('(Summer|Winter)')

#drop games and ID column
athlete_events.drop('Games', axis=1, inplace=True)
athlete_events.drop('ID', axis=1, inplace=True)

# Save the modified athlete_events dataframe to a new CSV file
athlete_events.to_csv('modified_file.csv', index=False)

