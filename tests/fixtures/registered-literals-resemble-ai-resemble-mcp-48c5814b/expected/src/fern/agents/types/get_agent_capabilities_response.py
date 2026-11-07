

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_agent_capabilities_response_asr_capabilities_item import GetAgentCapabilitiesResponseAsrCapabilitiesItem
from .get_agent_capabilities_response_llm_capabilities_item import GetAgentCapabilitiesResponseLlmCapabilitiesItem


class GetAgentCapabilitiesResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    asr_capabilities: typing.Optional[typing.List[GetAgentCapabilitiesResponseAsrCapabilitiesItem]] = None
    llm_capabilities: typing.Optional[typing.List[GetAgentCapabilitiesResponseLlmCapabilitiesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
