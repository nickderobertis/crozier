

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v60response_info import V60ResponseInfo


class V60Metadata(UniversalBaseModel):
    response: V60ResponseInfo = pydantic.Field()
    """
    Response-code detail: numeric code, symbolic name, human-readable message, and a URL to the response schema definition.
    """

    version: str = pydantic.Field()
    """
    Schema version of the response payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
