

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .openapi_get_error500error import OpenapiGetError500Error
from .openapi_get_error500meta import OpenapiGetError500Meta


class OpenapiGetError500(UniversalBaseModel):
    success: bool
    error: OpenapiGetError500Error
    meta: typing.Optional[OpenapiGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
