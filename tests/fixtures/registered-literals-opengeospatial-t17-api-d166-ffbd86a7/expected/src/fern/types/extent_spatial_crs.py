

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtentSpatialCrs(enum.StrEnum):
    """
    Coordinate reference system of the coordinates in the spatial extent
    (property `bbox`). The default reference system is WGS 84 longitude/latitude.
    In the Core this is the only supported coordinate reference system.
    Extensions may support additional coordinate reference systems and add
    additional enum values.
    """

    HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC13CRS84 = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"

    def visit(self, http_www_opengis_net_def_crs_ogc13crs84: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtentSpatialCrs.HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC13CRS84:
            return http_www_opengis_net_def_crs_ogc13crs84()
