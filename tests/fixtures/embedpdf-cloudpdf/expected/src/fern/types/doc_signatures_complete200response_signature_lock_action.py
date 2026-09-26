

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseSignatureLockAction(enum.StrEnum):
    ALL = "all"
    INCLUDE = "include"
    EXCLUDE = "exclude"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        exclude: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesComplete200ResponseSignatureLockAction.ALL:
            return all_()
        if self is DocSignaturesComplete200ResponseSignatureLockAction.INCLUDE:
            return include()
        if self is DocSignaturesComplete200ResponseSignatureLockAction.EXCLUDE:
            return exclude()
