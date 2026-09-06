

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAccessTokenResponse(UniversalBaseModel):
    access_token: typing.Optional[str] = None
    token_type: typing.Optional[str] = None
    expires_in: typing.Optional[int] = None
    scope: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
