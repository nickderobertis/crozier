

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unit_type_term_value import UnitTypeTermValue


class UnitTypeTerm(UniversalBaseModel):
    exponent: typing.Optional[int] = None
    value: typing.Optional[UnitTypeTermValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
