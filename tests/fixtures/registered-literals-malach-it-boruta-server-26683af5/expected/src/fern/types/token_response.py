

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenResponse(UniversalBaseModel):
    token_type: str
    access_token: typing.Optional[str] = None
    agent_token: typing.Optional[str] = None
    id_token: typing.Optional[str] = None
    refresh_token: typing.Optional[str] = None
    expires_in: int
    c_nonce: typing.Optional[str] = None
    c_nonce_expires_in: typing.Optional[int] = None
    authorization_details: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
