from typing import Any
from SongDBCore.model.song import Song


class Stream:
    """An object that has a list of the songs related to a specific stream."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def songs(self) -> list[Song]:
        """A list of the songs related to a specific stream.

        Returns:
            list[Song]: A list of object that representing a song.
        """
        return [Song(song) for song in self._response["result"]]
