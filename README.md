# Setting Up the Project for Personal Development
1. Create an Azure Quantum Workspace Resource - https://learn.microsoft.com/en-us/azure/quantum/how-to-create-workspace
2. Download the project https://github.com/NikitaChernevskiy/EAQCMLP to a specific location (e.g., `C:/`)
3. Download and install:

   I. Visual Studio Code - https://code.visualstudio.com/download

   II. Anaconda - https://www.anaconda.com/download/

   III. .NET Core - https://dotnet.microsoft.com/en-us/download
4. Download resources and tools for developing quantum algorithms - Quantum Development Kit - https://marketplace.visualstudio.com/items?itemName=quantum.qsharp-lang-vscode
5. Create and activate a virtual environment with Anaconda - https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk?tabs=tabid-vscode%2Ctabid-conda#use-q-and-python-with-jupyter-notebooks
6. Now we need to install several packages. In the terminal at the project's location, copy this list of commands:
```
pip install qsharp
dotnet tool install -g Microsoft.Quantum.IQSharp
dotnet iqsharp install
pip install --upgrade azure-quantum
dotnet add package Microsoft.Quantum.MachineLearning
pip install azure-ai-ml
pip install -U pip
pip install -U matplotlib
pip install numpy 
```
![Terminal](./Assets/OpenTerminal.png)

7. You need to modify this part of the code in the `host.py` file—the data can be found on the main page of your Azure Quantum Workspace Resource.

   ![Files](./Assets/ChangeDataInFile.png)
   ![Data](./Assets/AzureData.png)

9. To start the project, in the terminal you need to type the command `python host.py`

# Working with Personal Data

The project works with JSON in a specific format. To achieve this, we need to use the files `csvappend.py` and `csvtojson.py`, and for data—`OriginalData.csv`.

`OriginalData.csv` is the original data table on which the next two Python files operate. It has 6 columns: `Farm`, `Type`, `Year`, `Round`, `Bees`, and `Floral`. For training the model, the columns `Bees` and `Floral` are used. The `Type` column determines whether the farm is beneficial (`HLS` - 1) or harmful (`ELS` - 0) for the bees.

`csvappend.py` augments your original data with similar data by adding different noise. So if you initially have 1 CSV file with 100 rows, after executing the program you will have 10 files with 100, 200, 300, 400, 500, 600, 700, 800, 900, and 1000 rows. The data is generated based on the existing data—for example, a farm has 2 years of data collection, and each year has 3 rounds of analysis (Spring, Summer, Autumn)—so it turns out that one farm has a total of 6 rows of data collection. Also, if each farm has a certain type (`HLS` or `ELS`), then this type must be the same for each row of the given farm.

`csvtojson.py` converts the obtained 10 CSV datasets into 10 JSON files. These files serve as data for training the model. Two columns are used—`Bees` and `Floral`. The structure in which the existing datasets should be converted looks like this:

```json
{
  "TrainingData": {
    "Features": [
      [numeric value 1, numeric value 2],
      [numeric value 1, numeric value 2]
    ],
    "Labels": [
      1,
      0
    ]
  },
  "ValidationData": {
    "Features": [
      [numeric value 1, numeric value 2]
    ],
    "Labels": [
      0
    ]
  }
}
```
When working with your own data, keep in mind that although your dataset may contain more than two columns, the model is designed to train correctly only with two columns. Therefore, in the JSON files, you should not include arrays with three elements if you aim for stable results. Additionally, remember that the first row of your dataset contains the column headers, so you need to generate the new tables with the required number of data rows plus one to account for the headers. The csvtojson.py script intentionally skips the first row.
