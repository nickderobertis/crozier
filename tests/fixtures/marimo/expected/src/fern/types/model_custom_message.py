

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_custom_message_method import ModelCustomMessageMethod


class ModelCustomMessage(UniversalBaseModel):
    """
    Custom widget message.

        Attributes:
            content: Arbitrary content for the custom message.
    """

    content: typing.Any
    method: ModelCustomMessageMethod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
