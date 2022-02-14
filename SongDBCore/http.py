from inspect import EndOfBlock
from typing import Any, Optional

import requests

from SongDBCore.error import DBAccessError


class SongDBHttpClient:
    def __init__(self, url: Optional[str]) -> None:
        self.base_url = url
        pass

    async def request(self, *, endpoint: str, **kwargs: Any) -> Any | dict:
        if not self.base_url:
            self.base_url = "https://script.google.com/macros/s/AKfycbz_4ITm8ybnl7yLT0bmcGQoPHg3hGDAU38u6Q809dBhqS8-GZqnxTrWSqDKwAlZPuFi/exec"
        req_url = self.base_url + endpoint
        print(req_url)
        result: requests.Response = requests.get(req_url)
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

    async def _multi_search(
        self,
        *,
        song_name: Optional[str] = None,
        artist_name: Optional[str] = None,
        stream_id: Optional[str] = None,
    ) -> Any:
        endpoints: list[str] = []  # query:?xxx=yyy&xxx=yyy&xxx=yyy
        if song_name:
            endpoints.append(f"title={song_name}")
        if artist_name:
            endpoints.append(f"artist={artist_name}")
        if stream_id:
            endpoints.append(f"url={stream_id}")
        if not endpoints:
            raise DBAccessError(reason="I need at least 1 query.")
        else:
            endpoint = "?" + "&".join(endpoints)
            return await self.request(endpoint=endpoint)
