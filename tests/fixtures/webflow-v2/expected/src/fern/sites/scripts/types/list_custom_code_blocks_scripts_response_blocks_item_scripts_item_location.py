

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListCustomCodeBlocksScriptsResponseBlocksItemScriptsItemLocation(enum.StrEnum):
    """
    Location of the script, either in the header or footer of the published site
    """

    HEADER = "header"
    FOOTER = "footer"

    def visit(self, header: typing.Callable[[], T_Result], footer: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCustomCodeBlocksScriptsResponseBlocksItemScriptsItemLocation.HEADER:
            return header()
        if self is ListCustomCodeBlocksScriptsResponseBlocksItemScriptsItemLocation.FOOTER:
            return footer()
