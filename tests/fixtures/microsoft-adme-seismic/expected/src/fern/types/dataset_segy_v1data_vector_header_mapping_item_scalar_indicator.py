

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator(enum.StrEnum):
    """
    Enumerated string indicating whether to use the normal scalar field for scaling this field (STANDARD), no scaling (NOSCALE), or override scalar (OVERRIDE).  Default is current STANDARD (such as SEG-Y rev2).
    """

    STANDARD = "STANDARD"
    NOSCALE = "NOSCALE"
    OVERRIDE = "OVERRIDE"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        noscale: typing.Callable[[], T_Result],
        override: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator.STANDARD:
            return standard()
        if self is DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator.NOSCALE:
            return noscale()
        if self is DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator.OVERRIDE:
            return override()
