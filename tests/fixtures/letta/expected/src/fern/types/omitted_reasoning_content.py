

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OmittedReasoningContent(UniversalBaseModel):
    """
    A placeholder for reasoning content we know is present, but isn't returned by the provider (e.g. OpenAI GPT-5 on ChatCompletions)
    """

    signature: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for this reasoning step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
