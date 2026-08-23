

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Granularity(enum.StrEnum):
    """
    Granularity derived from the GS1 Digital Link AIs (EN 18219 / EN 18223).
    """

    MODEL = "model"
    BATCH = "batch"
    ITEM = "item"

    def visit(
        self,
        model: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
        item: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Granularity.MODEL:
            return model()
        if self is Granularity.BATCH:
            return batch()
        if self is Granularity.ITEM:
            return item()
