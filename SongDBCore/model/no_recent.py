from typing import Any, Union
from SongDBCore.model.song import Song


class No_Recent:
    """An object that has a list of the songs that has not been sung recently."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def songs(self) -> Union[Song, list[Song]]:
        """A list of the songs that has not been sung recently.

        Returns:
            Union[Song, list[Song]]: An object that represents a song.
        """
        return self._response
