from typing import Any

from SongDBCore.model.history import History


class Song:  # ひきすう:song.jsonのりすと
    """An object that represents a song."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def title(self) -> str:
        """A title of the song.

        Returns:
            str: the song's title
        """
        return self._response["title"]

    @property
    def artist(self) -> str:
        """An artist of the song.
        may contains the song's composer.

        Returns:
            str: the song's artist's name or composer's name
        """
        return self._response["artist"]

    @property
    def history(self) -> list[History]:
        """A history of the song.
        it contains when the song was sang and that links to youtube.

        Returns:
            list[History]: Contains the date and the link tou youtube.
        """
        return [History(history) for history in self._response["history"]]

    @property
    def latest(self) -> History:
        """A history object that the song was sung most recently.

        Returns:
            History
        """
        return History(self._response["history"][0])


class RawSong(Song):
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def songs(self) -> list[Song]:
        return [Song(song) for song in self._response["result"]]
