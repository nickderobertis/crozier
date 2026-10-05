

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_status import HealthStatus


class HealthResponse(UniversalBaseModel):
    """
    Overall health check response.
    """

    components: typing.Optional[typing.Dict[str, HealthStatus]] = pydantic.Field(default=None)
    """
    Component health statuses
    """

    service: str = pydantic.Field()
    """
    Service name
    """

    status: str = pydantic.Field()
    """
    Overall status: healthy, unhealthy, degraded
    """

    version: str = pydantic.Field()
    """
    Service version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
