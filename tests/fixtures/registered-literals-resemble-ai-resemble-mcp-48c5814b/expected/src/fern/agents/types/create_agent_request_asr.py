

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_agent_request_asr_user_input_audio_format import CreateAgentRequestAsrUserInputAudioFormat


class CreateAgentRequestAsr(UniversalBaseModel):
    model: typing.Optional[str] = None
    provider: typing.Optional[str] = None
    user_input_audio_format: typing.Optional[CreateAgentRequestAsrUserInputAudioFormat] = None
    keywords: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
