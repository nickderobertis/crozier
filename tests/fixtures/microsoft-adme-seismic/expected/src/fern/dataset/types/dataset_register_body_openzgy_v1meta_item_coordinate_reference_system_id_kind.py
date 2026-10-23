

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemIdKind(enum.StrEnum):
    """
    The kind of reference, constant 'CRS' for FrameOfReferenceCRS.
    """

    CRS = "CRS"

    def visit(self, crs: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemIdKind.CRS:
            return crs()
