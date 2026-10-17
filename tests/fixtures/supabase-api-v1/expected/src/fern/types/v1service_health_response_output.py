

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1service_health_response_output_info import V1ServiceHealthResponseOutputInfo
from .v1service_health_response_output_name import V1ServiceHealthResponseOutputName
from .v1service_health_response_output_status import V1ServiceHealthResponseOutputStatus


class V1ServiceHealthResponseOutput(UniversalBaseModel):
    name: V1ServiceHealthResponseOutputName
    healthy: bool = pydantic.Field()
    """
    Deprecated. Use `status` instead.
    """

    status: V1ServiceHealthResponseOutputStatus
    info: typing.Optional[V1ServiceHealthResponseOutputInfo] = None
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
