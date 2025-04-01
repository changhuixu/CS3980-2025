# Settings Demo

```powershell
python -m venv venv
./venv/Scripts/activate

pip install beanie
pip install pydantic-settings
```

The `.env` file in a Python project should be placed in the root directory of the project. This is the standard location where libraries like `python-dotenv` expect to find it. The root directory is generally defined as the top-level directory containing your main application files, such as `main.py`.
