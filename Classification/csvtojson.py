import csv
import json
import os

# Input and output directories
csv_directory = 'csvs'
json_directory = 'jsons'

# Ensure the output directory exists
os.makedirs(json_directory, exist_ok=True)

# Process each CSV file
for i in range(1, 11):  # Assuming 10 CSV files with sequential numbering
    csv_filename = os.path.join(csv_directory, f"{i}00.csv")
    json_filename = os.path.join(json_directory, f"data{i}.json")

    training_data = {"Features": [], "Labels": []}
    validation_data = {"Features": [], "Labels": []}

    with open(csv_filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)  # Convert the reader to a list of dictionaries for easier indexing
        for row in rows:
            try:
                # Extract relevant columns
                round_value = float(row['Round'])
                amount_bees = float(row['Bees'])
                floral = float(row['Floral'])
                type_value = row['Type']

                # Create a feature from Floral and Amount_Bees
                feature = [floral, amount_bees]

                # Assign label based on the condition
                label = 1 if type_value == "HLS" else 0 if type_value == "ELS" else None

                # Decide which set to add the data to
                if label is not None:
                    if len(validation_data["Features"]) < 2:
                        validation_data["Features"].append(feature)
                        validation_data["Labels"].append(label)
                    else:
                        training_data["Features"].append(feature)
                        training_data["Labels"].append(label)
            except Exception as e:
                print(f"Error processing row in file {csv_filename}: {e}")

    # Create the final JSON structure
    json_data = {
        "TrainingData": training_data,
        "ValidationData": validation_data
    }

    # Write the JSON data to a file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)