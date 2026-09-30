

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchRequestBestOpenAccessRightLabelItem(enum.StrEnum):
    OPEN_SOURCE = "OPEN SOURCE"
    OPEN = "OPEN"
    EMBARGO = "EMBARGO"
    RESTRICTED = "RESTRICTED"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        open_source: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        embargo: typing.Callable[[], T_Result],
        restricted: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchRequestBestOpenAccessRightLabelItem.OPEN_SOURCE:
            return open_source()
        if self is SearchRequestBestOpenAccessRightLabelItem.OPEN:
            return open()
        if self is SearchRequestBestOpenAccessRightLabelItem.EMBARGO:
            return embargo()
        if self is SearchRequestBestOpenAccessRightLabelItem.RESTRICTED:
            return restricted()
        if self is SearchRequestBestOpenAccessRightLabelItem.CLOSED:
            return closed()
        if self is SearchRequestBestOpenAccessRightLabelItem.UNKNOWN:
            return unknown()
