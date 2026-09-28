

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadCaptureSource(enum.StrEnum):
    """
    where to extract from: a JSONPath over the response body, a response header value, or a regex over the response body string
    """

    BODY_JSONPATH = "BODY_JSONPATH"
    HEADER = "HEADER"
    BODY_REGEX = "BODY_REGEX"

    def visit(
        self,
        body_jsonpath: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        body_regex: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadCaptureSource.BODY_JSONPATH:
            return body_jsonpath()
        if self is LoadCaptureSource.HEADER:
            return header()
        if self is LoadCaptureSource.BODY_REGEX:
            return body_regex()
