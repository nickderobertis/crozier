

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_unlock_expression_definition import (
    DestinyDefinitionsDestinyUnlockExpressionDefinition,
)
from .destiny_definitions_director_destiny_linked_graph_entry_definition import (
    DestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition,
)


class DestinyDefinitionsDirectorDestinyLinkedGraphDefinition(UniversalBaseModel):
    """
    This describes links between the current graph and others, as well as when that link is relevant.
    """

    description: typing.Optional[str] = None
    linked_graph_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="linkedGraphId"), pydantic.Field(alias="linkedGraphId")
    ] = None
    linked_graphs: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition]],
        FieldMetadata(alias="linkedGraphs"),
        pydantic.Field(alias="linkedGraphs"),
    ] = None
    name: typing.Optional[str] = None
    overview: typing.Optional[str] = None
    unlock_expression: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyUnlockExpressionDefinition],
        FieldMetadata(alias="unlockExpression"),
        pydantic.Field(alias="unlockExpression"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
