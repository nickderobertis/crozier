

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestResponseFormat(enum.StrEnum):
    """
    The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.
    """

    URL = "url"
    B64JSON = "b64_json"

    def visit(self, url: typing.Callable[[], T_Result], b64json: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageRequestResponseFormat.URL:
            return url()
        if self is CreateImageRequestResponseFormat.B64JSON:
            return b64json()
