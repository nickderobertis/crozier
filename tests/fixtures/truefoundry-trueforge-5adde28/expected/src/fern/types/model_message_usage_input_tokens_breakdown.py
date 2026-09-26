

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelMessageUsageInputTokensBreakdown(UniversalBaseModel):
    harness: int = pydantic.Field()
    """
    Tokens attributed to harness system framing.
    """

    instructions: int = pydantic.Field()
    """
    Tokens attributed to agent instructions.
    """

    messages: int = pydantic.Field()
    """
    Tokens attributed to conversation messages.
    """

    skills: int = pydantic.Field()
    """
    Tokens attributed to skill instructions.
    """

    tool_definitions: int = pydantic.Field()
    """
    Tokens attributed to tool schemas.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
