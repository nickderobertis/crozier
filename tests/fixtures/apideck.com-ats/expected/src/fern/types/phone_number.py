

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .phone_number_type import PhoneNumberType


class PhoneNumber(UniversalBaseModel):
    area_code: typing.Optional[str] = None
    country_code: typing.Optional[str] = None
    extension: typing.Optional[str] = None
    id: typing.Optional[str] = None
    number: str
    type: typing.Optional[PhoneNumberType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
