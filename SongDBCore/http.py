from typing import Any

import requests

from SongDBCore.error import DBAccessError


class SongDBHttpClient:
    def __init__(self) -> None:
        pass

    async def request(self, *, endpoint: str, **kwargs: Any) -> Any | dict:
        BASE_URL = "https://script.google.com/macros/s/AKfycby8mvvmnNO3tQRsqM47A-Rh61zlgYpzUt40mLDKXuiwU2agS-KkeQheX3dwxOq7aZA/exec"
        url = BASE_URL + endpoint
        print(url)
        result: requests.Response = requests.get(url)
        if result.json().get("status") == "ng":
            raise DBAccessError
        else:
            return result.json()

    async def _search_by_song(self, *, song_name: str) -> Any:
        return await self.request(endpoint=f"?title={song_name}")

    async def _search_by_artist(self, *, artist_name: str) -> Any:
        return await self.request(endpoint=f"?artist={artist_name}")

    async def _search_by_stream(self, *, stream_id: str) -> Any:
        return await self.request(endpoint=f"?url={stream_id}")

    async def _search_no_recent_song(self) -> Any:
        return await self.request(endpoint="?recent")
