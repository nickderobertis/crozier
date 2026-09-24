

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_error import FieldError


class ErrorResponse(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    custom raybot error code
    """

    message: str = pydantic.Field()
    """
    custom raybot error message
    """

    details: typing.Optional[typing.List[FieldError]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
