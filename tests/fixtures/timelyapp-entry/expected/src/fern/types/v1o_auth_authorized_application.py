

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1OAuthAuthorizedApplication(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Application ID
    """

    name: str = pydantic.Field()
    """
    Application name
    """

    uid: str = pydantic.Field()
    """
    Application client ID
    """

    scopes: str = pydantic.Field()
    """
    Space-separated list of granted scopes
    """

    created_at: int = pydantic.Field()
    """
    Authorization created timestamp (Unix timestamp)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
