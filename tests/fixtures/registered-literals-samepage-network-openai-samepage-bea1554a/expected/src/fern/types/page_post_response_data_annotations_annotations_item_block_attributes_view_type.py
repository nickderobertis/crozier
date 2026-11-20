

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType(enum.StrEnum):
    BULLET = "bullet"
    NUMBERED = "numbered"
    DOCUMENT = "document"

    def visit(
        self,
        bullet: typing.Callable[[], T_Result],
        numbered: typing.Callable[[], T_Result],
        document: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType.BULLET:
            return bullet()
        if self is PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType.NUMBERED:
            return numbered()
        if self is PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType.DOCUMENT:
            return document()
