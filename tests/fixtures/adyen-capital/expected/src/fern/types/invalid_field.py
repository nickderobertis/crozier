

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvalidField(UniversalBaseModel):
    message: str = pydantic.Field()
    """
    Description of the validation error.
    """

    name: str = pydantic.Field()
    """
    The field that has an invalid value.
    """

    value: str = pydantic.Field()
    """
    The invalid value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
