

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtentTemporalTrs(enum.StrEnum):
    """
    Coordinate reference system of the coordinates in the temporal extent
    (property `interval`). The default reference system is the Gregorian calendar.
    In the Core this is the only supported temporal coordinate reference system.
    Extensions may support additional temporal coordinate reference systems and add
    additional enum values.
    """

    HTTP_WWW_OPENGIS_NET_DEF_UOM_ISO86010GREGORIAN = "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"

    def visit(self, http_www_opengis_net_def_uom_iso86010gregorian: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtentTemporalTrs.HTTP_WWW_OPENGIS_NET_DEF_UOM_ISO86010GREGORIAN:
            return http_www_opengis_net_def_uom_iso86010gregorian()
