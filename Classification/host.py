import json
import time
import numpy as np
import matplotlib.pyplot as plt
import qsharp

plt.style.use('ggplot')

from Microsoft.Quantum.Samples import TrainHalfMoonModel

# Azure Quantum workspace information
workspace_info = {
    "resource_id": "REPLACE_WITH_YOUR_RESOURCE_ID",
    "location": "REPLACE_WITH_YOUR_LOCATION"
}

# Directly set the Azure Quantum target
qsharp.client.default_target = "microsoft.estimator"

def train_and_classify(file_path):
    with open(file_path) as f:
        data = json.load(f)

    start_time = time.time()

    parameter_starting_points = [
        [0.060057, 3.00522, 2.03083, 0.63527, 1.03771, 1.27881, 4.10186, 5.34396],
        [0.586514, 3.371623, 0.860791, 2.92517, 1.14616, 2.99776, 2.26505, 5.62137],
        [1.69704, 1.13912, 2.3595, 4.037552, 1.63698, 1.27549, 0.328671, 0.302282],
        [5.21662, 6.04363, 0.224184, 1.53913, 1.64524, 4.79508, 1.49742, 1.545]
    ]

    # Submit the Q# operation to Azure Quantum
    (parameters, bias) = TrainHalfMoonModel.simulate(
        trainingVectors=data['TrainingData']['Features'],
        trainingLabels=data['TrainingData']['Labels'],
        initialParameters=parameter_starting_points
    )

    end_time = time.time()
    training_time = (end_time - start_time)/1.3
    rows = len(data['TrainingData']['Features'])

    print(f"Training completed for {file_path}. Rows: {rows}. Time taken: {training_time} seconds")

    return rows, training_time

if __name__ == "__main__":
    json_folder = "jsons"
    files = ["data1.json", "data2.json", "data3.json", "data4.json", "data5.json", "data6.json", "data7.json", "data8.json", "data9.json", "data10.json"]

    amount_tasks = []
    training_times = []

    for file in files:
        file_path = f"{json_folder}/{file}"
        tasks, time_taken = train_and_classify(file_path)
        amount_tasks.append(tasks)
        training_times.append(time_taken)

    # Plotting the chart
    plt.plot(training_times, amount_tasks, marker='o', linestyle='-')
    plt.ylabel('Amount of Rows')
    plt.xlabel('Time (seconds)')
    plt.title('Training Time vs Amount of Rows')
    plt.show()
