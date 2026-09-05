

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPageMetadataRequestStatus(enum.StrEnum):
    PUBLISHED = "published"
    DRAFT = "draft"

    def visit(self, published: typing.Callable[[], T_Result], draft: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPageMetadataRequestStatus.PUBLISHED:
            return published()
        if self is GetPageMetadataRequestStatus.DRAFT:
            return draft()
