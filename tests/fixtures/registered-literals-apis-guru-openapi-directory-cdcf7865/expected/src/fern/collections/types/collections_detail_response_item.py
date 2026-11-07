

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collections_detail_response_item_attributes import CollectionsDetailResponseItemAttributes
from .collections_detail_response_item_links import CollectionsDetailResponseItemLinks
from .collections_detail_response_item_relationships import CollectionsDetailResponseItemRelationships


class CollectionsDetailResponseItem(UniversalBaseModel):
    attributes: typing.Optional[CollectionsDetailResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the collection.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the collection.
    """

    links: typing.Optional[CollectionsDetailResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the entity.
    """

    relationships: typing.Optional[CollectionsDetailResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the node entity.
    """

    type: str = pydantic.Field()
    """
    The type identifier of the entity (`collections`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
