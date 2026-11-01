

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .basic_error_model import BasicErrorModel


class ExtendedErrorModel(BasicErrorModel):
    errors: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
