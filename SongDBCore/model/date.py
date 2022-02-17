from typing import Any
from SongDBCore.model.song import Song


class Date:
    """A object that has a list of songs that fit the date requirements."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def songs(self) -> list[Song]:
        """returns a list of songs that fit the date requirements.

        Returns:
            list[Song]: a list of songs
        """
        return [Song(song) for song in self._response["result"]]
