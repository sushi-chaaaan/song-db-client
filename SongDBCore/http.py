from typing import Any, Optional

import requests

from SongDBCore.error import DBAccessError


class SongDBHttpClient:
    def __init__(self, url: Optional[str]) -> None:
        self.base_url = url
        pass

    async def request(self, *, endpoint: str, **kwargs: Any) -> Any | dict:
        if not self.base_url:
            self.base_url = "https://script.google.com/macros/s/AKfycbybEQO66Ui5AbgaPvisluBbWMqxayLM2iyPCNeipXUOvn__Jp4SQsm7X8Z4w3HQvxja/exec"
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

    async def _search_by_date(
        self,
        *,
        _from: Optional[str],
        _to: Optional[str],
    ) -> Any:
        dates = (_from, _to)
        if dates[0] is not None and dates[1] is not None:
            return await self.request(endpoint=f"?date_from={_from}&date_to={_to}")
        elif dates[0] is not None and dates[1] is None:
            return await self.request(endpoint=f"date_from={_from}")
        elif dates[0] is None and dates[1] is not None:
            return await self.request(endpoint=f"?date_to={_to}")
        else:
            raise DBAccessError(reason="Date select error.")

    async def _multi_search(
        self,
        *,
        song_name: Optional[str] = None,
        artist_name: Optional[str] = None,
        stream_id: Optional[str] = None,
        _from: Optional[str] = None,
        _to: Optional[str] = None,
    ) -> Any:
        endpoints: list[str] = []  # query:?xxx=yyy&xxx=yyy&xxx=yyy
        if song_name:
            endpoints.append(f"title={song_name}")
        if artist_name:
            endpoints.append(f"artist={artist_name}")
        if stream_id:
            endpoints.append(f"url={stream_id}")
        if _from:
            endpoints.append(f"date_from={_from}")
        if _to:
            endpoints.append(f"date_to={_to}")
        if not endpoints:
            raise DBAccessError(reason="I need at least 1 query.")
        else:
            endpoint = "?" + "&".join(endpoints)
            return await self.request(endpoint=endpoint)
