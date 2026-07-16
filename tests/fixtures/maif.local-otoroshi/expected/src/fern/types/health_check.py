

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HealthCheck(UniversalBaseModel):
    """
    The configuration for checking health of a service. Otoroshi will perform GET call on the URL to check if the service is still alive
    """

    enabled: bool = pydantic.Field()
    """
    Whether or not healthcheck is enabled on the current service descriptor
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to check
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
