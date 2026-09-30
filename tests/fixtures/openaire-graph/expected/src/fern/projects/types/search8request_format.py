

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Search8RequestFormat(enum.StrEnum):
    """
    Response format
    """

    XML = "xml"
    JSON = "json"

    def visit(self, xml: typing.Callable[[], T_Result], json: typing.Callable[[], T_Result]) -> T_Result:
        if self is Search8RequestFormat.XML:
            return xml()
        if self is Search8RequestFormat.JSON:
            return json()
