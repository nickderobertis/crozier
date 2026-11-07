

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_errors import BadRequestErrorBodyErrors
from .bad_request_error_body_meta import BadRequestErrorBodyMeta


class BadRequestErrorBody(UniversalBaseModel):
    meta: BadRequestErrorBodyMeta
    message: str
    errors: BadRequestErrorBodyErrors = pydantic.Field()
    """
    Map that sums up all received values that seemed incorrect
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
