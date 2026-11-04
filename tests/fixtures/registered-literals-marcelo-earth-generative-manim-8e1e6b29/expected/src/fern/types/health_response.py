

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_response_providers_value import HealthResponseProvidersValue
from .health_response_status import HealthResponseStatus


class HealthResponse(UniversalBaseModel):
    status: HealthResponseStatus = pydantic.Field()
    """
    healthy if at least one provider key is configured, degraded otherwise.
    """

    providers: typing.Dict[str, HealthResponseProvidersValue]
    configured_providers: int
    total_providers: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
