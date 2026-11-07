

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_addon_accounts_read_response_attributes import UsersAddonAccountsReadResponseAttributes
from .users_addon_accounts_read_response_links import UsersAddonAccountsReadResponseLinks


class UsersAddonAccountsReadResponse(UniversalBaseModel):
    attributes: typing.Optional[UsersAddonAccountsReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the addon account entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the addon account entity.
    """

    links: typing.Optional[UsersAddonAccountsReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the addon account entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the addon account entity (`external_accounts`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
