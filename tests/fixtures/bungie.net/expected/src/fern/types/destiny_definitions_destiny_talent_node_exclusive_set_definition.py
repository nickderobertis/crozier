

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition(UniversalBaseModel):
    """
    The list of indexes into the Talent Grid's "nodes" property for nodes in this exclusive set. (See DestinyTalentNodeDefinition.nodeIndex)
    """

    node_indexes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="nodeIndexes")] = (
        pydantic.Field(default=None)
    )
    """
    The list of node indexes for the exclusive set. Historically, these were indexes. I would have liked to replace this with nodeHashes for consistency, but it's way too late for that. (9:09 PM, he's right!)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
