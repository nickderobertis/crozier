

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_contributors_list_response_item_attributes import NodesContributorsListResponseItemAttributes
from .nodes_contributors_list_response_item_links import NodesContributorsListResponseItemLinks
from .nodes_contributors_list_response_item_relationships import NodesContributorsListResponseItemRelationships


class NodesContributorsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesContributorsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the contributor entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the contributor entity. Contributor identifiers have the form {node_id}-{user_id}.
    """

    links: typing.Optional[NodesContributorsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the contributor entity.
    """

    relationships: NodesContributorsListResponseItemRelationships = pydantic.Field()
    """
    URLs to other entities or entity collections that have a relationship to the contributor entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the contributor entity (`contributors`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
