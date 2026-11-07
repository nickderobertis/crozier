

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LifeCycleStatus(enum.StrEnum):
    """
    The life cycle status of a model.
    Note: A model can be promoted from "preview" to "generally-available", but never from "generally-available" to "preview".
    """

    PREVIEW = "preview"
    GENERALLY_AVAILABLE = "generally-available"

    def visit(
        self, preview: typing.Callable[[], T_Result], generally_available: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is LifeCycleStatus.PREVIEW:
            return preview()
        if self is LifeCycleStatus.GENERALLY_AVAILABLE:
            return generally_available()
