

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAgentCapabilitiesResponseLlmCapabilitiesItem(UniversalBaseModel):
    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    LLM provider name (e.g., "openai", "anthropic")
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model identifier (e.g., "gpt-4o", "claude-3-5-sonnet-20241022")
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the capability
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
