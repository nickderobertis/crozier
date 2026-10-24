

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisteredClient(UniversalBaseModel):
    client_id: typing.Optional[str] = None
    client_secret: typing.Optional[str] = None
    redirect_uris: typing.Optional[typing.List[str]] = None
    grant_types: typing.Optional[typing.List[str]] = None
    response_types: typing.Optional[typing.List[str]] = None
    registration_access_token: typing.Optional[str] = None
    registration_client_uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
