

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DepositErrorsItem(UniversalBaseModel):
    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field or file the violation concerns
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Validation error message
    """

    value: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The invalid value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
