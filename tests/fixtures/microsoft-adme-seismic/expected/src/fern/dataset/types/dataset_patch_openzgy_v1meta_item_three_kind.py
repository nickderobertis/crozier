

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetPatchOpenzgyV1MetaItemThreeKind(enum.StrEnum):
    """
    The kind of reference, constant 'AzimuthReference', for FrameOfReferenceAzimuthReference.
    """

    AZIMUTH_REFERENCE = "AzimuthReference"

    def visit(self, azimuth_reference: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetPatchOpenzgyV1MetaItemThreeKind.AZIMUTH_REFERENCE:
            return azimuth_reference()
