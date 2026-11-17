

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_info import ModelInfo


class ModelInfoList(UniversalBaseModel):
    """
    The list of available models.
    """

    models: typing.Optional[typing.List[ModelInfo]] = pydantic.Field(default=None)
    """
    List of available models.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
