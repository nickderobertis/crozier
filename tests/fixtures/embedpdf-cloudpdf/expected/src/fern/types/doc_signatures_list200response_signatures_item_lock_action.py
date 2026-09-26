

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesList200ResponseSignaturesItemLockAction(enum.StrEnum):
    ALL = "all"
    INCLUDE = "include"
    EXCLUDE = "exclude"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        exclude: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesList200ResponseSignaturesItemLockAction.ALL:
            return all_()
        if self is DocSignaturesList200ResponseSignaturesItemLockAction.INCLUDE:
            return include()
        if self is DocSignaturesList200ResponseSignaturesItemLockAction.EXCLUDE:
            return exclude()
