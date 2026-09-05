

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MyProfileRestGetRole(enum.StrEnum):
    ANONYMOUS = "ANONYMOUS"
    GUEST = "GUEST"
    USER = "USER"
    TESTER = "TESTER"
    PRODUCT_OWNER = "PRODUCT_OWNER"
    ADMIN = "ADMIN"

    def visit(
        self,
        anonymous: typing.Callable[[], T_Result],
        guest: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        tester: typing.Callable[[], T_Result],
        product_owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MyProfileRestGetRole.ANONYMOUS:
            return anonymous()
        if self is MyProfileRestGetRole.GUEST:
            return guest()
        if self is MyProfileRestGetRole.USER:
            return user()
        if self is MyProfileRestGetRole.TESTER:
            return tester()
        if self is MyProfileRestGetRole.PRODUCT_OWNER:
            return product_owner()
        if self is MyProfileRestGetRole.ADMIN:
            return admin()
