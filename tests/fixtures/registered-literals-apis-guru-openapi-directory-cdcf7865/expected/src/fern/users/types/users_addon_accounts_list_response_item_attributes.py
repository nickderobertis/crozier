

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsersAddonAccountsListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the addon account entity.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's display name on the third-party service
    """

    profile_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The link to user's profile on third-party service
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short name of the third-party service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
