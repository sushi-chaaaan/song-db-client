from typing import Optional

from SongDBCore.http import SongDBHttpClient
from SongDBCore.model.artist import Artist
from SongDBCore.model.no_recent import No_Recent
from SongDBCore.model.song import RawSong
from SongDBCore.model.stream import Stream


class SongDBClient(SongDBHttpClient):
    def __init__(self, url: Optional[str] = None) -> None:
        super().__init__(url=url)

    async def search_artist(self, *, artist_name: str) -> Artist:
        return Artist(await self._search_by_artist(artist_name=artist_name))

    async def search_no_recent(self) -> No_Recent:
        return No_Recent(await self._search_no_recent_song())

    async def search_song(self, *, song_name: str) -> RawSong:
        return RawSong(await self._search_by_song(song_name=song_name))

    async def search_stream(self, *, stream_id: str) -> Stream:
        return Stream(await self._search_by_stream(stream_id=stream_id))

    async def multi_search(
        self,
        *,
        song_name: Optional[str] = None,
        artist_name: Optional[str] = None,
        stream_id: Optional[str] = None
    ) -> RawSong:
        return RawSong(
            await self._multi_search(
                song_name=song_name,
                artist_name=artist_name,
                stream_id=stream_id,
            )
        )
