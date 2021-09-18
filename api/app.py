import os
import openai

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

engine = "cushman-codex"
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

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}