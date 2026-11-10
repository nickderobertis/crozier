

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .phone_number_type import PhoneNumberType


class PhoneNumber(UniversalBaseModel):
    """
    A phone number
    """

    data: str = pydantic.Field()
    """
    The phone number.
    """

    primary: bool = pydantic.Field()
    """
    When `true`, identifies the phone number as the primary number on an account.
    """

    type: PhoneNumberType = pydantic.Field()
    """
    The type of phone number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
