

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind(enum.StrEnum):
    """
    The kind of reference, 'Unit' for FrameOfReferenceUOM.
    """

    UNIT = "Unit"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind.UNIT:
            return unit()
