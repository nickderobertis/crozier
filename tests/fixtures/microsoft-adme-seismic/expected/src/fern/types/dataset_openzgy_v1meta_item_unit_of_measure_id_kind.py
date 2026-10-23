

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetOpenzgyV1MetaItemUnitOfMeasureIdKind(enum.StrEnum):
    """
    The kind of reference, 'Unit' for FrameOfReferenceUOM.
    """

    UNIT = "Unit"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT:
            return unit()
