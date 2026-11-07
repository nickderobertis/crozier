

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_institutions_list_response_item_attributes import UsersInstitutionsListResponseItemAttributes
from .users_institutions_list_response_item_links import UsersInstitutionsListResponseItemLinks
from .users_institutions_list_response_item_relationships import UsersInstitutionsListResponseItemRelationships


class UsersInstitutionsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[UsersInstitutionsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the institution entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the institution entity.
    """

    links: typing.Optional[UsersInstitutionsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the institutions entity.
    """

    relationships: typing.Optional[UsersInstitutionsListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the institution entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the institution entity (`institutions`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
