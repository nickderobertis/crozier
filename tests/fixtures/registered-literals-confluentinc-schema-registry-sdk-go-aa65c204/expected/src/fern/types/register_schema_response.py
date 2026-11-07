

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .rule_set import RuleSet
from .schema_reference import SchemaReference


class RegisterSchemaResponse(UniversalBaseModel):
    """
    Schema register response
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Globally unique identifier of the schema
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number
    """

    guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Globally unique identifier of the schema
    """

    schema_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schemaType"),
        pydantic.Field(alias="schemaType", description="Schema type"),
    ] = None
    """
    Schema type
    """

    references: typing.Optional[typing.List[SchemaReference]] = pydantic.Field(default=None)
    """
    References to other schemas
    """

    metadata: typing.Optional[Metadata] = None
    rule_set: typing_extensions.Annotated[
        typing.Optional[RuleSet], FieldMetadata(alias="ruleSet"), pydantic.Field(alias="ruleSet")
    ] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Schema definition string"),
    ] = None
    """
    Schema definition string
    """

    ts: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp when the schema was created
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the schema has been deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
