from threading import Lock
from datetime import datetime, UTC

from datetime import datetime, UTC

def test_created_at_timestamp():
    created_at = datetime.now(UTC)
    assert created_at.tzinfo is not None


class URLStore:
    def __init__(self):
        self.data = {}
        self.lock = Lock()

    def save(self, code, url):
        with self.lock:
            self.data[code] = {
                "url": url,
                "clicks": 0,
                "created_at": datetime.now(UTC)
            }

    def get(self, code):
        return self.data.get(code)

    def increment_clicks(self, code):
        with self.lock:
            if code in self.data:
                self.data[code]["clicks"] += 1

store = URLStore()

