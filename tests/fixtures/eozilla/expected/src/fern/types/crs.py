

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Crs(enum.StrEnum):
    HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC13CRS84 = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC0CRS84H = "http://www.opengis.net/def/crs/OGC/0/CRS84h"

    def visit(
        self,
        http_www_opengis_net_def_crs_ogc13crs84: typing.Callable[[], T_Result],
        http_www_opengis_net_def_crs_ogc0crs84h: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Crs.HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC13CRS84:
            return http_www_opengis_net_def_crs_ogc13crs84()
        if self is Crs.HTTP_WWW_OPENGIS_NET_DEF_CRS_OGC0CRS84H:
            return http_www_opengis_net_def_crs_ogc0crs84h()
