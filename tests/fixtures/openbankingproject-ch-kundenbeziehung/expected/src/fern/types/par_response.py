

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParResponse(UniversalBaseModel):
    request_uri: str = pydantic.Field()
    """
    Request URI to use in authorization request
    """

    expires_in: int = pydantic.Field()
    """
    Request URI lifetime in seconds (max 60 for FAPI 2.0)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
