

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vanity_url_error_response import VanityUrlErrorResponse


class VanityUrlResponse(UniversalBaseModel):
    code: typing.Optional[str] = None
    uses: int
    error: typing.Optional[VanityUrlErrorResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
