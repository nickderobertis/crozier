

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_contributors_read_response_item_attributes import NodesContributorsReadResponseItemAttributes
from .nodes_contributors_read_response_item_links import NodesContributorsReadResponseItemLinks
from .nodes_contributors_read_response_item_relationships import NodesContributorsReadResponseItemRelationships


class NodesContributorsReadResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesContributorsReadResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the contributor entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the contributor entity. Contributor identifiers have the form {node_id}-{user_id}.
    """

    links: typing.Optional[NodesContributorsReadResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the contributor entity.
    """

    relationships: NodesContributorsReadResponseItemRelationships = pydantic.Field()
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
