

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .db_migration_state import DbMigrationState


class DbMigrationRead(UniversalBaseModel):
    migrated_at: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="migratedAt")] = None
    migrated_by: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="migratedBy")] = None
    migration_description: typing_extensions.Annotated[str, FieldMetadata(alias="migrationDescription")]
    migration_script: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="migrationScript")] = None
    migration_state: typing_extensions.Annotated[
        typing.Optional[DbMigrationState], FieldMetadata(alias="migrationState")
    ] = None
    migration_type: typing_extensions.Annotated[str, FieldMetadata(alias="migrationType")]
    migration_version: typing_extensions.Annotated[str, FieldMetadata(alias="migrationVersion")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
