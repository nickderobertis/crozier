

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TemplatesGetTemplateSnapshotResponseBlocksItem(UniversalBaseModel):
    entity_id: typing_extensions.Annotated[str, FieldMetadata(alias="entityId"), pydantic.Field(alias="entityId")]
    label: str
    value: str
    limit: float
    description: str
    preserve_on_migration: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveOnMigration"), pydantic.Field(alias="preserveOnMigration")
    ] = None
    read_only: typing_extensions.Annotated[bool, FieldMetadata(alias="readOnly"), pydantic.Field(alias="readOnly")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
