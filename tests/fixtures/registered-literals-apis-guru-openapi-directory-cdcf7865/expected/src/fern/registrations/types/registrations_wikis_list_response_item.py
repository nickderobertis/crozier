

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_wikis_list_response_item_attributes import RegistrationsWikisListResponseItemAttributes
from .registrations_wikis_list_response_item_links import RegistrationsWikisListResponseItemLinks
from .registrations_wikis_list_response_item_relationships import RegistrationsWikisListResponseItemRelationships


class RegistrationsWikisListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[RegistrationsWikisListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the wiki.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the wiki.
    """

    links: typing.Optional[RegistrationsWikisListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the wiki.
    """

    relationships: RegistrationsWikisListResponseItemRelationships = pydantic.Field()
    """
    URLs to other entities or entity collections that have a relationship to the wiki.
    """

    type: str = pydantic.Field()
    """
    The type identifier of the wiki (`wikis`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
