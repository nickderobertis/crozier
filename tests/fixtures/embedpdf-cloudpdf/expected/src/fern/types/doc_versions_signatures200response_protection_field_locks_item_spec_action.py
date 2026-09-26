

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatures200ResponseProtectionFieldLocksItemSpecAction(enum.StrEnum):
    ALL = "all"
    INCLUDE = "include"
    EXCLUDE = "exclude"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        exclude: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsSignatures200ResponseProtectionFieldLocksItemSpecAction.ALL:
            return all_()
        if self is DocVersionsSignatures200ResponseProtectionFieldLocksItemSpecAction.INCLUDE:
            return include()
        if self is DocVersionsSignatures200ResponseProtectionFieldLocksItemSpecAction.EXCLUDE:
            return exclude()
