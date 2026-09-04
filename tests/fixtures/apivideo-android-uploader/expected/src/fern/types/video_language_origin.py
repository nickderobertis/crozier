

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VideoLanguageOrigin(enum.StrEnum):
    """
    Returns the origin of the last update on the video's `language` attribute.

    - `api` means that the last update was requested from the API.
    - `auto` means that the last update was done automatically by the API.
    """

    API = "api"
    AUTO = "auto"

    def visit(self, api: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is VideoLanguageOrigin.API:
            return api()
        if self is VideoLanguageOrigin.AUTO:
            return auto()
