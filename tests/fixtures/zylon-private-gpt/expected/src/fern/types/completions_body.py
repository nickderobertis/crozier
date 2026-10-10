

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_filter import ContextFilter


class CompletionsBody(UniversalBaseModel):
    prompt: str
    system_prompt: typing.Optional[str] = None
    use_context: typing.Optional[bool] = None
    context_filter: typing.Optional[ContextFilter] = None
    include_sources: typing.Optional[bool] = None
    stream: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
