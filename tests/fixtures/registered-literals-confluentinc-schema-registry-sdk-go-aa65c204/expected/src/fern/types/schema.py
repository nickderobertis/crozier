

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .rule_set import RuleSet
from .schema_reference import SchemaReference
from .schema_tags import SchemaTags


class Schema(UniversalBaseModel):
    subject: typing.Optional[str] = None
    version: typing.Optional[int] = None
    id: typing.Optional[int] = None
    guid: typing.Optional[str] = None
    schema_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schemaType"), pydantic.Field(alias="schemaType")
    ] = None
    references: typing.Optional[typing.List[SchemaReference]] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    metadata: typing.Optional[Metadata] = None
    rule_set: typing_extensions.Annotated[
        typing.Optional[RuleSet], FieldMetadata(alias="ruleSet"), pydantic.Field(alias="ruleSet")
    ] = None
    schema_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[SchemaTags]], FieldMetadata(alias="schemaTags"), pydantic.Field(alias="schemaTags")
    ] = None
    ts: typing.Optional[int] = None
    deleted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
