

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2error_error import V2ErrorError


class V2Error(UniversalBaseModel):
    """
    Canonical error envelope returned by the public v2 API.
    """

    error: V2ErrorError = pydantic.Field()
    """
    Canonical error details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
