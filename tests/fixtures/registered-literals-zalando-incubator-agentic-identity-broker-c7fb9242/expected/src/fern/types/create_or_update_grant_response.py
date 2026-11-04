

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_grant import UserGrant


class CreateOrUpdateGrantResponse(UniversalBaseModel):
    data: UserGrant
    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional redirect URL returned when a valid session_token query parameter was present. Contains the original authorization request URL so the frontend can resume the OAuth2 flow via window.location.href (not XHR).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
