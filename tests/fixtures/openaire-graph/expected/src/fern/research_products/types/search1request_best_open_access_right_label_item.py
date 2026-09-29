

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Search1RequestBestOpenAccessRightLabelItem(enum.StrEnum):
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
        if self is Search1RequestBestOpenAccessRightLabelItem.OPEN_SOURCE:
            return open_source()
        if self is Search1RequestBestOpenAccessRightLabelItem.OPEN:
            return open()
        if self is Search1RequestBestOpenAccessRightLabelItem.EMBARGO:
            return embargo()
        if self is Search1RequestBestOpenAccessRightLabelItem.RESTRICTED:
            return restricted()
        if self is Search1RequestBestOpenAccessRightLabelItem.CLOSED:
            return closed()
        if self is Search1RequestBestOpenAccessRightLabelItem.UNKNOWN:
            return unknown()
