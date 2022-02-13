import re
from typing import Any

remove_pre = re.compile(r"^[\S]*youtu.be/")
remove_suf = re.compile(r"\?t=[\d]*")


class History:  # ひきすう:history.json
    """An object that represents a history of the song."""

    def __init__(self, response: Any) -> None:
        self._response = response
        pass

    @property
    def date(self) -> str:  # 2022/02/02
        """
        A date that the song is sang.
        Returns:
            str: yyyy/mm/dd
        """
        return self._response["date"]

    @property
    def note(self) -> str:
        """
        A note that the song has.

        Returns:
            str: A note
        """
        return self._response["note"]

    @property
    def url(self) -> str:
        """
        A link that the song had begun singing.

        Returns:
            str: youtube link like youtu.be/xxxx
        """
        return self._response["url"]

    @property
    def raw_id(self) -> str:
        """A raw video id of youtube videos in this history.

        Returns:
            str: VideoId
        """
        raw_id = remove_pre.sub("", self._response["url"])  # 3aMJcqIu-EI?t=2700
        id = remove_suf.sub("", raw_id)  # 3aMJcqIu-EI
        return id
