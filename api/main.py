import os
import openai
import timeit

from typing import Optional
from fastapi import FastAPI
from io import StringIO
from contextlib import redirect_stdout

app = FastAPI()

engine = "davinci-codex"
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/debug/completion")
def completion(text: str, max_tokens: Optional[int]=50, stop: Optional[str]=None):
    return openai.Completion.create(
        engine=engine,
        text=text,
        max_tokens=max_tokens,
        temperature=0,
        frequency_penalty=0.0, # TODO: Tune these
        presence_penalty=0.0,
        stop=stop
    )

@app.get("/runtime")
def runtime(code: str, max_tokens: Optional[int]=50, stop: Optional[str]=None):
    prompt = "Optimize the runtime of the above code\n"
    return completion(prompt + code, max_tokens, stop)

@app.get("/explain")
def explain(code: str, max_tokens: Optional[int]=50, stop: Optional[str]=None):
    pass

@app.get("/parallel")
def parallel(code: str, max_tokens: Optional[int]=50, stop: Optional[str]=None):
    pass

@app.get("/")
def read_root():
    return "If you're reading this, know that this idea was born from a 2am session screwing with Copilot"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}