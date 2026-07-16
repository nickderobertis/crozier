

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .db_migration_read import DbMigrationRead


class DbMigrationExecutionRead(UniversalBaseModel):
    executed_migrations: typing_extensions.Annotated[
        typing.Optional[typing.List[DbMigrationRead]],
        FieldMetadata(alias="executedMigrations"),
        pydantic.Field(alias="executedMigrations"),
    ] = None
    initial_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initialVersion"), pydantic.Field(alias="initialVersion")
    ] = None
    target_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetVersion"), pydantic.Field(alias="targetVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
