

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HealthCheckResponse(UniversalBaseModel):
    """
    Health check status for critical application dependencies
    """

    main_database: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Main database connection status - true if database is reachable and running
    """

    cache_database: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Cache database connection status - true if cache database is reachable and running
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
