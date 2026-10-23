

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetRegisterBodySegyV1MetaItemThreeKind(enum.StrEnum):
    """
    The kind of reference, constant 'AzimuthReference', for FrameOfReferenceAzimuthReference.
    """

    AZIMUTH_REFERENCE = "AzimuthReference"

    def visit(self, azimuth_reference: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetRegisterBodySegyV1MetaItemThreeKind.AZIMUTH_REFERENCE:
            return azimuth_reference()
