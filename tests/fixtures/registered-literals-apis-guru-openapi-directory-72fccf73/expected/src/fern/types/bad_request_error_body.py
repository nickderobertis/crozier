

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_invalid_params_item import BadRequestErrorBodyInvalidParamsItem


class BadRequestErrorBody(UniversalBaseModel):
    detail: typing.Optional[str] = None
    instance: typing.Optional[str] = None
    invalid_params: typing.Optional[typing.List[BadRequestErrorBodyInvalidParamsItem]] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
