# Настройте проекта за лична разработка
1. Създайте Azure Ресурс за Квантови Сервиси Azure Quantum Workspace Resource - https://learn.microsoft.com/en-us/azure/quantum/how-to-create-workspace
2. Свалете проекта в определена локация
3. Свалете и инсталирайте:

   I. Visual Studio Code

   II. Anaconda
   
   III. Dot NET Core
4. Свалете ресурси и инструменти за разработка с Квантови алгоритми - Quantum Development Kit - https://marketplace.visualstudio.com/items?itemName=quantum.qsharp-lang-vscode
5. Създайте и активирайте виртуална среда с Anaconda - https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk?tabs=tabid-vscode%2Ctabid-conda#use-q-and-python-with-jupyter-notebooks
6. Сега трябва да свалим няколко пакета. В терминала за локацията с проекта копирайте този списък с команди:
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
7. Трябва да промените тази част от кода във файла host.py - данните може да намерите на главната страница на Azure Ресурса за Квантови Сервиси 
   ![Files](https://github.com/NikitaChernevskiy/EAQCMLP/assets/117015781/e66224ed-03e5-403b-96a3-ae129c21f29d)
8. За да стартирате проекта, в терминала трябва да напишете командата python host.py

# Работа с лични данни
