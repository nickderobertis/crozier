

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_snapshot_response_snapshot_progress_snapshot import (
    CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot,
)


class CurrentUserProgressSnapshotResponseSnapshot(UniversalBaseModel):
    progress_snapshot: typing_extensions.Annotated[
        CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot,
        FieldMetadata(alias="progressSnapshot"),
        pydantic.Field(alias="progressSnapshot"),
    ]
    total_brain_power: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalBrainPower"), pydantic.Field(alias="totalBrainPower")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
