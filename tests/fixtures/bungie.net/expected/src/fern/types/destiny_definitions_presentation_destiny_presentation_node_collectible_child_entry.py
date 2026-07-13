

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry(UniversalBaseModel):
    collectible_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="collectibleHash")] = None
    node_display_priority: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nodeDisplayPriority")
    ] = pydantic.Field(default=None)
    """
    Use this value to sort the presentation node children in ascending order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
