

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_addon_accounts_list_response_item_attributes import UsersAddonAccountsListResponseItemAttributes
from .users_addon_accounts_list_response_item_links import UsersAddonAccountsListResponseItemLinks


class UsersAddonAccountsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[UsersAddonAccountsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the addon account entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the addon account entity.
    """

    links: typing.Optional[UsersAddonAccountsListResponseItemLinks] = pydantic.Field(default=None)
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
