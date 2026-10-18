

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ThirdPartyAuthOutput(UniversalBaseModel):
    id: str
    type: str
    oidc_issuer_url: typing.Optional[str] = None
    jwks_url: typing.Optional[str] = None
    custom_jwks: typing.Optional[typing.Any] = None
    resolved_jwks: typing.Optional[typing.Any] = None
    inserted_at: str
    updated_at: str
    resolved_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
