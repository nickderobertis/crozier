

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .principal_id import PrincipalId


class RunMaintenanceRequest_Gc(UniversalBaseModel):
    """
    One maintenance job for one namespace.
    """

    kind: typing.Literal["gc"] = "gc"
    grace_window_ms: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceRequest_Metadata(UniversalBaseModel):
    """
    One maintenance job for one namespace.
    """

    kind: typing.Literal["metadata"] = "metadata"
    max_wal_tail_objects: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceRequest_RecoverAdministrator(UniversalBaseModel):
    """
    One maintenance job for one namespace.
    """

    kind: typing.Literal["recover_administrator"] = "recover_administrator"
    principal_id: PrincipalId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceRequest_Retention(UniversalBaseModel):
    """
    One maintenance job for one namespace.
    """

    kind: typing.Literal["retention"] = "retention"
    cutoff_at_ms: typing.Optional[int] = None
    to_seq: typing.Optional[ChangeSeq] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunMaintenanceRequest_RetentionWindow(UniversalBaseModel):
    """
    One maintenance job for one namespace.
    """

    kind: typing.Literal["retention_window"] = "retention_window"
    retention_window_ms: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunMaintenanceRequest = typing_extensions.Annotated[
    typing.Union[
        RunMaintenanceRequest_Gc,
        RunMaintenanceRequest_Metadata,
        RunMaintenanceRequest_RecoverAdministrator,
        RunMaintenanceRequest_Retention,
        RunMaintenanceRequest_RetentionWindow,
    ],
    pydantic.Field(discriminator="kind"),
]
