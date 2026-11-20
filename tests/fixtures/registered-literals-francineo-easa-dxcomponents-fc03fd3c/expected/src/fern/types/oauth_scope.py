

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    GEOSPATIAL_DATA_PROVIDER = "geospatial.data_provider"
    """
    Client may provide geospatial data to data consumers.
    """

    GEOSPATIAL_DATA_CONSUMER = "geospatial.data_consumer"
    """
    Client may consume geospatial data from data providers.
    """

    def visit(
        self,
        geospatial_data_provider: typing.Callable[[], T_Result],
        geospatial_data_consumer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.GEOSPATIAL_DATA_PROVIDER:
            return geospatial_data_provider()
        if self is OauthScope.GEOSPATIAL_DATA_CONSUMER:
            return geospatial_data_consumer()
