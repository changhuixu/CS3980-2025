# Todo app

1. Create a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\activate

# macOS
source venv\bin\activate

pip install fastapi uvicorn

# after creating the main.py file, and generate an instance of FastAPI()
uvicorn main:app --reload
```
