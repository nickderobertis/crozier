

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base64string import Base64String
from .model_custom_method import ModelCustomMethod


class ModelCustom(UniversalBaseModel):
    """
    Custom application message.
    """

    buffers: typing.List[Base64String]
    content: typing.Any
    method: ModelCustomMethod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
