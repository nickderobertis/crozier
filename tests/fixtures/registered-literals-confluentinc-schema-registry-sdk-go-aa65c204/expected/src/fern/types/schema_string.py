

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .rule_set import RuleSet
from .schema_reference import SchemaReference
from .schema_tags import SchemaTags


class SchemaString(UniversalBaseModel):
    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the subject
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

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Schema string identified by the ID"),
    ] = None
    """
    Schema string identified by the ID
    """

    references: typing.Optional[typing.List[SchemaReference]] = pydantic.Field(default=None)
    """
    Schema references
    """

    metadata: typing.Optional[Metadata] = None
    rule_set: typing_extensions.Annotated[
        typing.Optional[RuleSet], FieldMetadata(alias="ruleSet"), pydantic.Field(alias="ruleSet")
    ] = None
    schema_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[SchemaTags]],
        FieldMetadata(alias="schemaTags"),
        pydantic.Field(alias="schemaTags", description="Schema tags"),
    ] = None
    """
    Schema tags
    """

    max_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxId"), pydantic.Field(alias="maxId", description="Maximum ID")
    ] = None
    """
    Maximum ID
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
