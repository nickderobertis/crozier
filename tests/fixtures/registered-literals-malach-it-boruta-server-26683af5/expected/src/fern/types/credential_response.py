

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CredentialResponse(UniversalBaseModel):
    format: typing.Optional[str] = None
    credential: typing.Optional[typing.Any] = None
    acceptance_token: typing.Optional[str] = None
    c_nonce: typing.Optional[str] = None
    c_nonce_expires_in: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
