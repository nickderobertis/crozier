

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_item import CollectionItem
from .container_mapping import ContainerMapping


class FlowCollectionItem(CollectionItem):
    container_mapping: typing.Optional[ContainerMapping] = pydantic.Field(default=None)
    """
    Describes the mapping of the Flow essence from this Flow collection's container
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
