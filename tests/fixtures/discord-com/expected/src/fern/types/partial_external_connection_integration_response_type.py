

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartialExternalConnectionIntegrationResponseType(enum.StrEnum):
    TWITCH = "twitch"
    YOUTUBE = "youtube"

    def visit(self, twitch: typing.Callable[[], T_Result], youtube: typing.Callable[[], T_Result]) -> T_Result:
        if self is PartialExternalConnectionIntegrationResponseType.TWITCH:
            return twitch()
        if self is PartialExternalConnectionIntegrationResponseType.YOUTUBE:
            return youtube()
