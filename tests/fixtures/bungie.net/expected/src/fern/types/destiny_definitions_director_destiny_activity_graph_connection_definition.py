

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition(UniversalBaseModel):
    """
    Nodes on a graph can be visually connected: this appears to be the information about which nodes to link. It appears to lack more detailed information, such as the path for that linking.
    """

    dest_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="destNodeHash"), pydantic.Field(alias="destNodeHash")
    ] = None
    source_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sourceNodeHash"), pydantic.Field(alias="sourceNodeHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
