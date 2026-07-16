

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_not_found_errors_item import ErrorNotFoundErrorsItem


class ErrorNotFound(UniversalBaseModel):
    errors: typing.Optional[typing.List[ErrorNotFoundErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
