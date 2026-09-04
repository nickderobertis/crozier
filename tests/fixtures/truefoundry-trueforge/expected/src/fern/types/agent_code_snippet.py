

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_code_snippet_sample_code import AgentCodeSnippetSampleCode


class AgentCodeSnippet(UniversalBaseModel):
    icon: str
    label_name: str
    language: str
    sample_code: AgentCodeSnippetSampleCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
