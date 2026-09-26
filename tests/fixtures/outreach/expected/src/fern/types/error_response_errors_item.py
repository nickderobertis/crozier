

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_errors_item_source import ErrorResponseErrorsItemSource


class ErrorResponseErrorsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    detail: typing.Optional[str] = None
    status: typing.Optional[int] = None
    source: typing.Optional[ErrorResponseErrorsItemSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
