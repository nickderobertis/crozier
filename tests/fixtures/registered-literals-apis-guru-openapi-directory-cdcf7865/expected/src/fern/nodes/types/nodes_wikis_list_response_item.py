

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_wikis_list_response_item_attributes import NodesWikisListResponseItemAttributes
from .nodes_wikis_list_response_item_links import NodesWikisListResponseItemLinks
from .nodes_wikis_list_response_item_relationships import NodesWikisListResponseItemRelationships


class NodesWikisListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesWikisListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the wiki.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the wiki.
    """

    links: typing.Optional[NodesWikisListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the wiki.
    """

    relationships: NodesWikisListResponseItemRelationships = pydantic.Field()
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
