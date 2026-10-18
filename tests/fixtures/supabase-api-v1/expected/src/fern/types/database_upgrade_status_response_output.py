

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .database_upgrade_status_response_output_database_upgrade_status import (
    DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatus,
)


class DatabaseUpgradeStatusResponseOutput(UniversalBaseModel):
    database_upgrade_status: typing_extensions.Annotated[
        typing.Optional[DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatus],
        FieldMetadata(alias="databaseUpgradeStatus"),
        pydantic.Field(alias="databaseUpgradeStatus"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
