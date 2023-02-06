import nmap
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"HOSS": "Home & Office Security Scanner"}

@app.get("/scan")
def scan(request: Request):
    client_host = request.client.host

    nm = nmap.PortScanner() 
    return nm.scan(hosts=f'{client_host}/24', arguments='-sS -O')

@app.get("/test")
def test(fName, lName):
    return f'Hello {fName} {lName}, this is a test endpoint'
    
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)