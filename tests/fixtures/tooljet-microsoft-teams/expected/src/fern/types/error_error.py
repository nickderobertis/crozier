

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_error_details_item import ErrorErrorDetailsItem
from .error_error_innererror import ErrorErrorInnererror


class ErrorError(UniversalBaseModel):
    code: typing.Optional[str] = None
    message: typing.Optional[str] = None
    target: typing.Optional[str] = None
    details: typing.Optional[typing.List[ErrorErrorDetailsItem]] = None
    innererror: typing.Optional[ErrorErrorInnererror] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
