from typing import Any
from SongDBCore.model.song import Song


class Artist:  # 引数:artist.json
    """A Object that has a list of the song related to a specific artist."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def songs(self) -> list[Song]:
        """A list of the song related to a specific artist.

        Returns:
            list[Song]: A list contains each song's title and so on.
        """
        return [Song(song) for song in self._response["result"]]
