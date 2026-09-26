

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseSignatureFieldMdpAction(enum.StrEnum):
    ALL = "all"
    INCLUDE = "include"
    EXCLUDE = "exclude"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        exclude: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesComplete200ResponseSignatureFieldMdpAction.ALL:
            return all_()
        if self is DocSignaturesComplete200ResponseSignatureFieldMdpAction.INCLUDE:
            return include()
        if self is DocSignaturesComplete200ResponseSignatureFieldMdpAction.EXCLUDE:
            return exclude()
