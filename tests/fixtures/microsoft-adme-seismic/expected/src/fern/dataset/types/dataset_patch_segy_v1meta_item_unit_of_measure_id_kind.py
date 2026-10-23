

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind(enum.StrEnum):
    """
    The kind of reference, 'Unit' for FrameOfReferenceUOM.
    """

    UNIT = "Unit"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind.UNIT:
            return unit()
