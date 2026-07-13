

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_presentation_destiny_presentation_node_requirements_block import (
    DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock,
)


class DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock(UniversalBaseModel):
    obscured_override_item_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="obscuredOverrideItemHash")
    ] = None
    requirements: typing.Optional[DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
