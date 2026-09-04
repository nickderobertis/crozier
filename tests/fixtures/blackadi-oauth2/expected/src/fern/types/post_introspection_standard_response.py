

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostIntrospectionStandardResponse(UniversalBaseModel):
    active: typing.Optional[bool] = None
    sub: typing.Optional[str] = None
    scope: typing.Optional[str] = None
    client_id: typing.Optional[str] = None
    token_type: typing.Optional[str] = None
    exp: typing.Optional[int] = None
    iat: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
