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

engine = 'davinci-codex'
openai.api_key = open('env.txt').readlines()[0]

class Item(BaseModel):
    code: str
    

@app.get('/debug/completion')
def completion(text: str, max_tokens: Optional[int]=None, stop: Optional[str]='\n\n#'):
    return openai.Completion.create(
        engine=engine,
        prompt=text,
        max_tokens=max_tokens,
        temperature=0.1,
        frequency_penalty=0.0, # TODO: Tune these
        presence_penalty=0.0,
        stop=stop
    )

@app.get('/runtime')
def runtime(code: Item, lang: str, max_tokens: Optional[int]=1024, stop: Optional[str]='\n\n#'):
    if lang.lower() == 'python':
        prefix = '\n#'
    elif lang.lower() == 'c' or lang.lower() == 'c++' or lang.lower() == 'javascript':
        prefix = '\n//'
    prompts = [' Optimize the runtime of the above code', ' Optimize the runtime complexity of the above code', 
                ' Optimize the time complexity of the above code', ' Improve the runtime complexity of the above code',
                ' Improve the runtime of the above code', ' Improve the time complexity of the above code',
                ' Reduce the time complexity of the above code', ' Reduce the runtime complexity of the above code']

    results = [completion(f'{code}\n{prefix}{prompt}\n', max_tokens, stop) for prompt in prompts]
    programs = [result['choices'][0]['text'] for result in results]

    char_freq_map = lambda x: { c: x.count(c) for c in x }
    char_freq_maps = [json.dumps(char_freq_map(program)) for i, program in enumerate(programs)]

    seen = set()
    output = []

    for i, char_freq_map in enumerate(char_freq_maps):
        if char_freq_map not in seen and programs[i] != '':
            output.append(programs[i])
            seen.add(char_freq_map)
    return output

@app.get('/explain')
def explain(code: str, lang: str, max_tokens: Optional[int]=1024, stop: Optional[str]=None):
    if lang.lower() == 'python':
        prefix = '\n#'
        suffix = "'''"
    elif lang.lower() == 'c' or lang.lower() == 'c++' or lang.lower() == 'javascript':
        prefix = '\n/**'
        suffix = '*/'
    prompt = ' Explain.\n'
    return completion(code + prefix + prompt + suffix, max_tokens, '\n\n')['choices'][0]['text']

@app.get('/copied')
def copied(code: str, lang: str, max_tokens: Optional[int]=1024, stop: Optional[str]='\n\n#'):
    if lang.lower() == 'c' or lang.lower() == 'c++' or lang.lower() == 'javascript':
        prefix = '\n//'
    elif lang.lower() == 'python':
        prefix = '\n#'
    prompt = (' What URL was the following code copied from?\n')
    return completion(code + prefix + prompt, max_tokens, stop)['choices'][0]['text']

@app.get('/')
def read_root():
    return 'Welcome to CodexCelerate'
