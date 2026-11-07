

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidationErrorErrorDetailsViolationsItem(UniversalBaseModel):
    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field that failed validation
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
