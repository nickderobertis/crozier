

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetSegyV1MetaItemUnitOfMeasureIdKind(enum.StrEnum):
    """
    The kind of reference, 'Unit' for FrameOfReferenceUOM.
    """

    UNIT = "Unit"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetSegyV1MetaItemUnitOfMeasureIdKind.UNIT:
            return unit()
