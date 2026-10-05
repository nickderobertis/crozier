

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HealthStatus(UniversalBaseModel):
    """
    Health status for a component.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional status message
    """

    status: str = pydantic.Field()
    """
    Health status: healthy, unhealthy, degraded
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
