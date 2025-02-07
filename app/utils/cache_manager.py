import hashlib
import json
import os
from typing import Dict, Any

class CacheManager:
    def __init__(self, cache_dir: str = "cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, prompt: str) -> str:
        return hashlib.md5(prompt.encode()).hexdigest()
    
    def get_cached_result(self, prompt: str) -> Dict[str, Any]:
        cache_key = self._get_cache_key(prompt)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                return json.load(f)
        return None
    
    def cache_result(self, prompt: str, result: Dict[str, Any]):
        cache_key = self._get_cache_key(prompt)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        with open(cache_file, 'w') as f:
            json.dump(result, f) 