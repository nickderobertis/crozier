

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the Schema Response Action.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="A link to the schema the the Registration Schema Block is on."),
    ] = None
    """
    A link to the schema the the Registration Schema Block is on.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
