from SongDB.http import SongDBHttpClient
from SongDB.model.artist import Artist
from SongDB.model.no_recent import No_Recent
from SongDB.model.song import Song
from SongDB.model.stream import Stream


class SongDBClient(SongDBHttpClient):
    def __init__(self) -> None:
        super().__init__()

    async def search_artist(self, *, artist_name: str) -> Artist:
        return Artist(await self._search_by_artist(artist_name=artist_name))

    async def search_no_recent(self) -> No_Recent:
        return No_Recent(await self._search_no_recent_song())

    async def search_song(self, *, song_name: str) -> Song:
        return Song(await self._search_by_song(song_name=song_name))

    async def search_stream(self, *, stream_id: str) -> Stream:
        return Stream(await self._search_by_stream(stream_id=stream_id))