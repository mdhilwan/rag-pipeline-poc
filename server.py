from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from rag_chain import qa

app = FastAPI()
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

@app.post("/ask")
async def ask(request: Request):
    print("✅ POST /ask received")
    body = await request.json()
    query = body.get("query")
    answer = qa.run(query)
    return JSONResponse(content={"result": answer})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
