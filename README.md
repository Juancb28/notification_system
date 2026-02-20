# Notification System
This application allows us to be up to date with tech news

## Techs used
Next, it's going to show some tools that was used in this project, and how to install in your computer. 

* **uv** as a library manager.
To install:
> In MacOS & Linux, using this command:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
> In Windows (Powershell), we use this command:
```
irm https://astral.sh/uv/install.ps1 | iex
```

To verificate installation, use this command in shell:

```
uv --version
```

As last movement in this tool, we initialazing **uv**, inside the directory's proyect path. 

Use this command to initialize **uv**:

```
uv init
```

This command generate 1 file:
- pyproject.toml

To add dependecies, or any library, you can use this command:

```
uv add fastapi
```

And **uv** will update automatically pyproject.toml.

### To Run project

Use this command to run code:

```
uv run python main.py
---
uvicorn api.api:app --host 127.0.0.1 --port 5757 --reload
```

Where 'main' could be another python's file.

Be the case, if you have requirements.txt with the libraries, you can add using the follow command:

```
uv add -r requirements.txt
```

When you need the same dependecies that you used in this project in another project, you need to follow the next intructions. 

1. You need 2 files: pyproject.toml & uv.lock
2. Those files must be cloned in the new project directory.
3. In the terminal, change directory to the correct path and run this command:
```
uv sync
```
4. Verify if all dependecies were cloned in the new project.


* Python as a backend language.
