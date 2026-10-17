

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .database_upgrade_status_response_output_database_upgrade_status_error import (
    DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError,
)
from .database_upgrade_status_response_output_database_upgrade_status_progress import (
    DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress,
)


class DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatus(UniversalBaseModel):
    initiated_at: str
    latest_status_at: str
    target_version: str
    error: typing.Optional[DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError] = None
    progress: typing.Optional[DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress] = None
    status: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
