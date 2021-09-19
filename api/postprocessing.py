from typing import Optional

def fetch_url(text: str) -> Optional[str]:
    chunks = text.split('\n')
    chunks = list(filter(None, chunks))
    
    if '://' in chunks[0]:
        return chunks[0]
    return None
