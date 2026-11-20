

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeVerticalReferenceType(enum.StrEnum):
    """
    A code indicating a vertical reference system. Allowed values:
    AGL = Above ground level (or above water surface, as applicable)
    AMSL = Above Mean Sea Level
    WGS84 = Above the surface of the WGS-84 ellipsoid (Ellipsoidal height)
    """

    AGL = "AGL"
    AMSL = "AMSL"
    WGS84 = "WGS84"

    def visit(
        self,
        agl: typing.Callable[[], T_Result],
        amsl: typing.Callable[[], T_Result],
        wgs84: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SimpleDataModelsCodeVerticalReferenceType.AGL:
            return agl()
        if self is SimpleDataModelsCodeVerticalReferenceType.AMSL:
            return amsl()
        if self is SimpleDataModelsCodeVerticalReferenceType.WGS84:
            return wgs84()
