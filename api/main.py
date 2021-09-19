import os
import openai
import timeit
import json

from typing import Optional
from fastapi import FastAPI
from io import StringIO
from contextlib import redirect_stdout
from pydantic import BaseModel

app = FastAPI()

engine = "davinci-codex"
openai.api_key = open('env.txt').readlines()[0]

class Item(BaseModel):
    code: str
    

@app.get("/debug/completion")
def completion(text: str, max_tokens: Optional[int]=None, stop: Optional[str]="\n#"):
    return openai.Completion.create(
        engine=engine,
        prompt=text,
        max_tokens=max_tokens,
        temperature=0.1,
        frequency_penalty=0.0, # TODO: Tune these
        presence_penalty=0.0,
        stop=stop
    )

@app.get("/runtime")
def runtime(code: Item, lang: str, max_tokens: Optional[int]=None, stop: Optional[str]="\n#"):
    if lang.lower() == "python":
        prefix = "#"
    elif lang.lower() == "c" or lang.lower() == "c++" or lang.lower() == "javascript":
        prefix = "//"
    prompts = [" Optimize the runtime of the above code", " Optimize the runtime complexity of the above code", 
                " Optimize the time complexity of the above code", " Improve the runtime complexity of the above code",
                " Improve the runtime of the above code", " Improve the time complexity of the above code",
                " Reduce the time complexity of the above code", " Reduce the runtime complexity of the above code",
                " Optimize the above code"]

    results = [completion(f"{code}\n{prefix}{prompt}\n", max_tokens, stop) for prompt in prompts]
    programs = [result["choices"][0]["text"] for result in results]

    char_freq_map = lambda x: {c: x.count(c) for c in x}
    char_freq_maps = [json.dumps(char_freq_map(program)) for i, program in enumerate(programs)]

    seen = set()
    output = []
    for i, char_freq_map in enumerate(char_freq_maps):
        if char_freq_map not in seen and programs[i] != "":
            output.append(programs[i])
            seen.add(char_freq_map)
    return output

with open("test.txt") as f:
    code = f.read()

print(runtime(code, "python", max_tokens=1024, stop="\n#"))

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