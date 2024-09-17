# Quantum Computing in Machine Learning: Performance Analysis

## Project Complexity

This project presents a medium to high level of complexity due to the integration of quantum technologies and specific machine learning algorithms. It requires in-depth knowledge in the field of quantum computing and its practical applicability within artificial intelligence. Besides technical competence, successful implementation also depends on the ability to adapt and integrate new methodologies into existing machine learning systems and infrastructures.

## Architecture

The architecture of the project is designed to leverage the capabilities of quantum computing while ensuring scalability, efficiency, security, and user-friendliness.

### Components

- **Quantum Computing Resources**: Utilizes quantum computing capabilities provided by Azure Quantum Workspace.
- **Data Processing Scripts**: Includes `csvappend.py` and `csvtojson.py` for data augmentation and conversion.
- **Machine Learning Models**: Employs the HalfMoon model for data classification.
- **User Interface**: Provides an intuitive interface for researchers to input their datasets and algorithms.

### Advantages

- **Scalability**: Easily adapts to increasing data processing requirements and model complexities.
- **Efficiency**: Significant improvements in data processing speed and analysis due to the integration with quantum computational resources.
- **Security**: Built-in data protection measures ensure all operations with datasets and models are safeguarded.
- **Open Source and User-Friendly**: Developed with an emphasis on open-source principles, allowing the research community to contribute and optimize the system. The user interface is intuitive, facilitating the process of working with the tool.

## Implementation Details

The project uses leading products and programming languages to create a robust and functional system that maximizes the benefits of quantum computing.

- **Azure Quantum Workspace**: Provides direct access to quantum computing capabilities, offering a reliable platform for executing program codes.
- **Visual Studio Code**: Serves as a secure integrated development environment (IDE) supporting consistent development and improvement of the code.
- **Programming Languages**:
  - **Python**: Used for development and visualization of quantum computations.
  - **Q#**: A specialized language for quantum programming.
- **Machine Learning Model**:
  - **HalfMoon Model**: Adapted for data classification tasks, demonstrating high adaptability and functionality when working with binary classification problems.

## Project Description

This project involves two key experiments:

### 1. Experiment on a Classical Computer

- **Objective**: Establish baseline metrics for training time and accuracy of selected machine learning models.
- **Method**: Models were trained on standard computer hardware.
- **Results**: As the complexity and volume of data increased, the training time grew significantly.

### 2. Experiment on a Quantum Computer

- **Objective**: Evaluate the performance improvements when using quantum computing.
- **Method**: The same models were trained using a quantum computer.
- **Results**: A significant acceleration in training time was observed compared to the classical computer.

With the growing importance of large language models (LLMs) and artificial intelligence (AI) in general, the ability to assess the benefits of quantum computers becomes increasingly vital. By developing such programs, any AI developer can download the software from GitHub, add their own datasets and machine learning algorithms, and thus evaluate the efficiency of quantum computing for their specific project.

The full installation instructions and source code are freely available for download from the [GitHub repository](https://github.com/NikitaChernevskiy/EAQCMLP). The project is licensed under the GNU General Public License, ensuring that the distribution of modified versions of the software must also be free and distributed under the same license, while sharing improvements with the community and contributing to its development.

This approach allows for individual evaluation and adaptation to the specific needs of each project. Developers can experiment with different types of datasets and algorithms to observe how quantum computing affects training speed, accuracy, and data processing. This enables them to identify potential areas for improvement and determine whether quantum computers represent a worthwhile investment for their project.

Furthermore, this platform can help expand the understanding of quantum technologies in the context of AI. This includes exploring new applications and using quantum algorithms to solve complex problems that traditional computational methods cannot efficiently process.

## Installation

### Prerequisites

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

## Working with Personal Data

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
When working with your own data, keep in mind that although your dataset may contain more than two columns, the model is designed to train correctly only with two columns. Therefore, in the JSON files, you should not include arrays with three elements if you aim for stable results. Also, please remember that the first row of your dataset contains the column headers, so you'll need to generate the new tables with the required number of data rows plus one to account for the headers. The csvtojson.py script intentionally skips the first row.

## Conclusion

The project demonstrates that the use of quantum computers in machine learning can significantly improve the speed and efficiency of processing large volumes of data. However, it is necessary to conduct further research with different datasets, machine learning models, and quantum computers of various generations to draw precise conclusions.

---
