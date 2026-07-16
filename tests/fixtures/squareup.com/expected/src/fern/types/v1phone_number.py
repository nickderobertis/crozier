

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1PhoneNumber(UniversalBaseModel):
    """
    Represents a phone number.
    """

    calling_code: str = pydantic.Field()
    """
    The phone number's international calling code. For US phone numbers, this value is +1.
    """

    number: str = pydantic.Field()
    """
    The phone number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
