

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionMessageReasoning(UniversalBaseModel):
    """
    Note: This is not part of the OpenAI API spec, but we added it for interoperability with multiple reasoning models.
    """

    id: typing.Optional[str] = None
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
