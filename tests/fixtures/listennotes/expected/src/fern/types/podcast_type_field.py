

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PodcastTypeField(enum.StrEnum):
    """
    The type of this podcast - episodic or serial.
    """

    EPISODIC = "episodic"
    SERIAL = "serial"

    def visit(self, episodic: typing.Callable[[], T_Result], serial: typing.Callable[[], T_Result]) -> T_Result:
        if self is PodcastTypeField.EPISODIC:
            return episodic()
        if self is PodcastTypeField.SERIAL:
            return serial()
