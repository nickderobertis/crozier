

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProvisionalTokenResponse(UniversalBaseModel):
    token_type: str
    access_token: str
    expires_in: int
    scope: str
    id_token: str
    refresh_token: typing.Optional[str] = None
    scopes: typing.Optional[typing.List[str]] = None
    expires_at_s: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
