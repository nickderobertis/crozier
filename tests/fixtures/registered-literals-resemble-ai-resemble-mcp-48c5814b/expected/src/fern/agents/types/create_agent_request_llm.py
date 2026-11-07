

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateAgentRequestLlm(UniversalBaseModel):
    prompt: typing.Optional[str] = None
    provider: typing.Optional[str] = None
    model: typing.Optional[str] = None
    reasoning_effort: typing.Optional[str] = None
    temperature: typing.Optional[float] = None
    timezone: typing.Optional[str] = None
    built_in_tools: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
