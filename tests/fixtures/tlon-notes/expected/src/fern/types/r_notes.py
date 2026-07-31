

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .r_snapshot_visibility import RSnapshotVisibility
from .u_notebook import UNotebook


class RNotes_Snapshot(UniversalBaseModel):
    type: typing.Literal["snapshot"] = "snapshot"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    visibility: RSnapshotVisibility

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RNotes_Update(UniversalBaseModel):
    type: typing.Literal["update"] = "update"
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    time: int
    update: UNotebook

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RNotes = typing_extensions.Annotated[typing.Union[RNotes_Snapshot, RNotes_Update], pydantic.Field(discriminator="type")]
