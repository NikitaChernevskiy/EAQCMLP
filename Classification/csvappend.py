import pandas as pd
import random

def generate_dataset(output_filename, total_rows):
    # Read the original dataset from a CSV file
    csv_filename = 'OriginalData.csv'
    df = pd.read_csv(csv_filename)

    # Create a new DataFrame
    new_df = pd.DataFrame(columns=df.columns)

    # Define the total number of rows needed
    total_rows_needed = total_rows

    # Calculate the remaining rows needed
    remaining_rows = total_rows_needed - len(df)

    # Define the number of duplicates for each farm
    duplicates_per_farm = 6

    # Calculate the number of new farms needed
    new_farms_to_create = (remaining_rows // duplicates_per_farm) + 1

    # Iterate over each farm in the original dataset
    for farm in df['Farm'].unique():
        type_value = df.loc[df['Farm'] == farm, 'Type'].iloc[0]  # Ensure consistent Type for each farm

        # Create duplicates for the current farm
        duplicates = [{'Farm': farm, 'Type': type_value, 'Year': year, 'Round': round_val,
                       'Bees': random.randint(1, 500), 'Floral': random.randint(5000, 100000)} for year in [2013, 2014] for round_val in [1, 2, 3]]

        # Add the duplicates to the new DataFrame
        new_df = pd.concat([new_df, pd.DataFrame(duplicates)], ignore_index=True)

    # Create new farms and implement the same logic
    for _ in range(new_farms_to_create):
        new_farm_number = max(new_df["Farm"].str.extract(r"(\d+)", expand=False).astype(int), default=0) + 1
        new_farm = f'Farm{new_farm_number}'

        type_value = random.choice(['ELS', 'HLS'])

        # Create duplicates for the new farm
        duplicates = [{'Farm': new_farm, 'Type': type_value, 'Year': year, 'Round': round_val,
                       'Bees': random.randint(1, 500), 'Floral': random.randint(5000, 100000)} for year in [2013, 2014] for round_val in [1, 2, 3]]

        # Add the duplicates to the new DataFrame
        new_df = pd.concat([new_df, pd.DataFrame(duplicates)], ignore_index=True)

    # Truncate the DataFrame to the desired total number of rows
    new_df = new_df.head(total_rows_needed)

    # Save the new DataFrame to a CSV file
    new_df.to_csv(output_filename, index=False)

# Generate datasets with the specified number of rows
generate_dataset('csvs/100.csv', 102)
generate_dataset('csvs/200.csv', 202)
generate_dataset('csvs/300.csv', 302)
generate_dataset('csvs/400.csv', 402)
generate_dataset('csvs/500.csv', 502)
generate_dataset('csvs/600.csv', 602)
generate_dataset('csvs/700.csv', 702)
generate_dataset('csvs/800.csv', 802)
generate_dataset('csvs/900.csv', 902)
generate_dataset('csvs/1000.csv', 1002)
