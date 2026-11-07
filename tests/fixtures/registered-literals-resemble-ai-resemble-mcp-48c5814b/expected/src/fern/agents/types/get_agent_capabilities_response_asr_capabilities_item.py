

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAgentCapabilitiesResponseAsrCapabilitiesItem(UniversalBaseModel):
    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    ASR provider name (e.g., "deepgram")
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model identifier (e.g., "nova-2")
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
