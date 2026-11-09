

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageVariationRequestResponseFormat(enum.StrEnum):
    """
    The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.
    """

    URL = "url"
    B64JSON = "b64_json"

    def visit(self, url: typing.Callable[[], T_Result], b64json: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageVariationRequestResponseFormat.URL:
            return url()
        if self is CreateImageVariationRequestResponseFormat.B64JSON:
            return b64json()
