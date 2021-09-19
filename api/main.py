import os
import openai
import timeit
import json

from typing import Optional
from contextlib import redirect_stdout
from postprocessing import fetch_url

engine = 'davinci-codex'
openai.api_key = open('env.txt').readlines()[0]

def completion(text: str, max_tokens: Optional[int]=None, stop: Optional[str]='\n\n#'):
    return openai.Completion.create(
        engine=engine,
        prompt=text,
        max_tokens=max_tokens,
        temperature=0.1,
        frequency_penalty=0.1,
        presence_penalty=0.0,
        stop=stop
    )

def runtime(code: str, lang: str, stop: str='\n\n\n'):
    max_tokens = 1024
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

def explain(code: str, lang: str, stop: str='\n\n\n'):
    max_tokens = 1024
    if lang.lower() == 'python':
        prefix = '\n#'
        suffix = "'''"
    elif lang.lower() == 'c' or lang.lower() == 'c++' or lang.lower() == 'javascript':
        prefix = '\n/**'
        suffix = '*/'
    prompt = ' Explain.\n'
    return completion(code + prefix + prompt + suffix, max_tokens, '\n\n')['choices'][0]['text']

def copied(code: str, lang: str, stop: str='\n\n\n'):
    max_tokens = 1024
    if lang.lower() == 'c' or lang.lower() == 'c++' or lang.lower() == 'javascript':
        prefix = '\n//'
    elif lang.lower() == 'python':
        prefix = '\n#'

    prompt = (' What URL was the following code copied from?\n')
    url = fetch_url(completion(code + prefix + prompt, max_tokens, stop)['choices'][0]['text'])

    # GPT-3 may troll you with Rick Astley's YouTube video if code was not copied :)
    if (url in 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' or '://' not in url):
        return 'No code copying inferred.'
    else:
        return 'Code copied from ' + url + '. A human should verify webpage content to confirm code copying.'