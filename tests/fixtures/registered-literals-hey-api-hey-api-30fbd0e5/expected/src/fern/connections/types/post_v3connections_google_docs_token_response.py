

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV3ConnectionsGoogleDocsTokenResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    A valid Google access token
    """

    granted_scopes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The scopes granted by the user during OAuth (may be a subset of requested scopes)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
