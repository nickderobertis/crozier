

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_list_response_item_attributes import UsersListResponseItemAttributes
from .users_list_response_item_links import UsersListResponseItemLinks
from .users_list_response_item_relationships import UsersListResponseItemRelationships


class UsersListResponseItem(UniversalBaseModel):
    attributes: UsersListResponseItemAttributes = pydantic.Field()
    """
    The properties of the user entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the user entity.
    """

    links: typing.Optional[UsersListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the user entity.
    """

    relationships: typing.Optional[UsersListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the user entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the user entity (`users`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
