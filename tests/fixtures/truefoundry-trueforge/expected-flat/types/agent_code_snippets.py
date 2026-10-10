

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_code_snippet import AgentCodeSnippet


class AgentCodeSnippets(UniversalBaseModel):
    base_url: str = pydantic.Field()
    """
    Origin to pass as the TrueForge SDK `baseUrl`.
    """

    snippets: typing.List[AgentCodeSnippet]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
