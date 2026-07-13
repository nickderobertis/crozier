

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsPresentationDestinyPresentationChildBlock(UniversalBaseModel):
    display_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="displayStyle")] = None
    parent_presentation_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentPresentationNodeHashes")
    ] = None
    presentation_node_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="presentationNodeType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
