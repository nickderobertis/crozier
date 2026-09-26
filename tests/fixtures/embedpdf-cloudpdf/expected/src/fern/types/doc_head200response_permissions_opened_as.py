

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocHead200ResponsePermissionsOpenedAs(enum.StrEnum):
    NONE = "none"
    USER = "user"
    OWNER = "owner"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocHead200ResponsePermissionsOpenedAs.NONE:
            return none()
        if self is DocHead200ResponsePermissionsOpenedAs.USER:
            return user()
        if self is DocHead200ResponsePermissionsOpenedAs.OWNER:
            return owner()
