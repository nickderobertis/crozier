

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_param import InputParam
from .model_ids_responses import ModelIdsResponses


class RefHolder(UniversalBaseModel):
    ids: typing.Optional[ModelIdsResponses] = None
    param: typing.Optional[InputParam] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
