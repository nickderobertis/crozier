

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocHead200ResponseAccessReasonsItem(enum.StrEnum):
    PASSWORD = "password"
    CDN = "cdn"
    PERMISSIONS_UNKNOWN = "permissions-unknown"

    def visit(
        self,
        password: typing.Callable[[], T_Result],
        cdn: typing.Callable[[], T_Result],
        permissions_unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocHead200ResponseAccessReasonsItem.PASSWORD:
            return password()
        if self is DocHead200ResponseAccessReasonsItem.CDN:
            return cdn()
        if self is DocHead200ResponseAccessReasonsItem.PERMISSIONS_UNKNOWN:
            return permissions_unknown()
