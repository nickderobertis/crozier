

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_collections_response_collections_item import ListCollectionsResponseCollectionsItem


class ListCollectionsResponse(UniversalBaseModel):
    collections: typing.Optional[typing.List[ListCollectionsResponseCollectionsItem]] = pydantic.Field(default=None)
    """
    An array of Collections
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
