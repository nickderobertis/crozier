

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTicDataRequestFormat(enum.StrEnum):
    """
    Serialization format of the response body: 'json' (default) or 'xml'.
    """

    JSON = "json"
    XML = "xml"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTicDataRequestFormat.JSON:
            return json()
        if self is GetTicDataRequestFormat.XML:
            return xml()
