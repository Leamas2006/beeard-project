# IDE Configuration Guide

This repository contains materials for Test BeeARD project  

## Required Software
1. **VS Code**: Download and install from [code.visualstudio.com](https://code.visualstudio.com/)
  
3. **Python Distribution**: **Anaconda** -- Full data science package download and install from [anaconda.com/download](https://www.anaconda.com/download)
    
4. **Ollama**: Download and install from [https://ollama.com/download/windows](https://ollama.com/download/windows)

5. **Git**: Download and install from [https://git-scm.com/downloads](https://git-scm.com/downloads)



### Recommended VS Code Extensions
Install from VS Code marketplace (Ctrl+Shift+X):

- autopep8
- Better Jinja
- Even Better TOML
- Git Graph
- GitHub Copilot
- GitHub Copilot Chat
- GitHub Pull Request
- GitLens
- isort
- Jinja
- Jupyter
- Material Icon Theme
- Path Intellisense
- Pylance
- Pylint
- Python
- Python Debugger
- Python Extension Pack
- Python Indent
- Rainbow CSV

## 🛠️ Environment Setup 
An `Anaconda Distribution` is required. Once downloaded, start with creating a virtual environment using `Anaconda Prompt`:

```Bash
conda env create --name beeard -f environment.yml
```
This command creates a new conda environment named beeard with all the dependencies specified in the environment.yml file.

Before working on the code, make sure to activate the environment using:

```Bash
conda activate beeard
```

Download Ollama LLMs on your PC (Comment:Update for this part is coming)
```Bash
ollama pull llama3.1:8b
ollama pull hermes3:8b
```

## 📥 Cloning the Repository (THIS PART IS JUST FOR TRAINING -- REPO`s BRANCHES IS NOT CORRECTLY ORGANISED)

Follow these steps to clone the repository to your local machine:

1. Create a new directory for the project:
```bash
mkdir -p /path/to/your/folder
```
This command creates a new directory path. The -p flag creates parent directories as needed and doesn't raise an error if the directory already exists.

2. Navigate to that directory:
```bash
cd /path/to/your/folder
```
The cd command changes your current working directory to the newly created folder.

3. Clone the repository into the current folder:
```bash
git init
git clone https://github.com/Leamas2006/beeard-project.git .
git remote -v
git status
```
This downloads all repository files into your current directory.
> **Note:** The trailing dot (`.`) after the repository URL tells Git to clone directly into the current directory instead of creating a new subdirectory.
> **Note:** check if source for (fetch) and (push) i correct -- `https://github.com/Leamas2006/beeard-project`
> **Note:** in the status bar shoud say thats all is synchronised or smth like that 
> **Note:** To be able to train work with repo you need to create your own github accounts and pin your usernames in discord chat. Thats all for now///

## 📂 Project Organization

```
beeard/
├── data/               # Исходные и обработанные данные
│   ├── raw/            # Скачанные статьи
│   ├── interim/        # Промежуточные данные
│   └── processed/      # Очищенные данные для моделей
├── models/             # Локальные модели ИИ
├── src/                # Исходный код
│   ├── agents/         # Код для агентов сбора информации
│   ├── kg/             # Код для создания графа знаний
│   └── hypothesis/     # Код для генерации гипотез
├── notebooks/          # Jupyter-ноутбуки для экспериментов
└── tests/              # Тесты
```
--------

