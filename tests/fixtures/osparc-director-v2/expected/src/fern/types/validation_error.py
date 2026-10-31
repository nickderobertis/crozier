

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validation_error_loc_item import ValidationErrorLocItem


class ValidationError(UniversalBaseModel):
    loc: typing.List[ValidationErrorLocItem]
    msg: str
    type: str
    input: typing.Optional[typing.Any] = None
    ctx: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
