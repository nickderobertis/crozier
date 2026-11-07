

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentCodeSnippetSampleCode(UniversalBaseModel):
    non_stream: str = pydantic.Field()
    """
    SDK sample that creates a turn without streaming.
    """

    stream: str = pydantic.Field()
    """
    SDK sample that streams turn events.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
