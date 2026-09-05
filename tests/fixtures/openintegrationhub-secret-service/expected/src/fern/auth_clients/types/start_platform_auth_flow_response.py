

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .start_platform_auth_flow_response_data import StartPlatformAuthFlowResponseData


class StartPlatformAuthFlowResponse(UniversalBaseModel):
    data: typing.Optional[StartPlatformAuthFlowResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
