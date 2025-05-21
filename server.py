from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from rag_chain import qa
import uvicorn

app = FastAPI()
# app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

@app.get("/app")
async def root():
    return FileResponse('ui/index.html')

@app.post("/ask")
async def ask(request: Request):
    print("✅ POST /ask received")
    body = await request.json()
    query = body.get("query")
    answer = qa.run(query)
    return JSONResponse(content={"result": answer})

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
