
import uvicorn #ASCI 
from fastapi import FastAPI

#2. Create the app object
app = FastAPI()

#3. Index route, opens automatcally on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "Hello, World"}

#4. Route with a sigle parameter, returns the parameter within a messaege
# Located at: http://127.0.0.1:8000/AnyNameHere
@app.get("/welcome")
def get_name(name: str):
    return {"welcome to ife LinkedIn": name}

#5 Run the API with uvicorn #Will run on http://127.0.0.1:8000
if __name__ == '__main__': 
    uvicorn.run(app, host='127.0.0.1', port=8000)
