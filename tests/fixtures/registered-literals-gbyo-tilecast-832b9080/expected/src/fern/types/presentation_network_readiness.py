

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presentation_network_readiness_helper_state import PresentationNetworkReadinessHelperState
from .presentation_network_readiness_reported_state import PresentationNetworkReadinessReportedState
from .presentation_network_readiness_status import PresentationNetworkReadinessStatus


class PresentationNetworkReadiness(UniversalBaseModel):
    screen_id: typing_extensions.Annotated[str, FieldMetadata(alias="screenId"), pydantic.Field(alias="screenId")]
    platform: str
    presentation_network_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="presentationNetworkId"),
        pydantic.Field(alias="presentationNetworkId"),
    ] = None
    presentation_network_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="presentationNetworkName"),
        pydantic.Field(alias="presentationNetworkName"),
    ] = None
    assigned_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="assignedAt"), pydantic.Field(alias="assignedAt")
    ] = None
    applicable: bool
    status: PresentationNetworkReadinessStatus
    detail: str
    helper_state: typing_extensions.Annotated[
        typing.Optional[PresentationNetworkReadinessHelperState],
        FieldMetadata(alias="helperState"),
        pydantic.Field(alias="helperState"),
    ] = None
    network_manager_available: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="networkManagerAvailable"),
        pydantic.Field(alias="networkManagerAvailable"),
    ] = None
    wifi_adapter_present: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="wifiAdapterPresent"), pydantic.Field(alias="wifiAdapterPresent")
    ] = None
    radio_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="radioEnabled"), pydantic.Field(alias="radioEnabled")
    ] = None
    reported_state: typing_extensions.Annotated[
        typing.Optional[PresentationNetworkReadinessReportedState],
        FieldMetadata(alias="reportedState"),
        pydantic.Field(alias="reportedState"),
    ] = None
    installed_network_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="installedNetworkId"), pydantic.Field(alias="installedNetworkId")
    ] = None
    installed_revision: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="installedRevision"), pydantic.Field(alias="installedRevision")
    ] = None
    active_network_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="activeNetworkId"), pydantic.Field(alias="activeNetworkId")
    ] = None
    last_connected_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastConnectedAt"), pydantic.Field(alias="lastConnectedAt")
    ] = None
    last_failure_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastFailureAt"), pydantic.Field(alias="lastFailureAt")
    ] = None
    last_failure_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastFailureCode"), pydantic.Field(alias="lastFailureCode")
    ] = None
    limitation: typing.Optional[str] = None
    wired_interface_available: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="wiredInterfaceAvailable"),
        pydantic.Field(alias="wiredInterfaceAvailable"),
    ] = None
    wired_ipv4: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="wiredIpv4"), pydantic.Field(alias="wiredIpv4")
    ] = None
    credentials_available: typing_extensions.Annotated[
        bool, FieldMetadata(alias="credentialsAvailable"), pydantic.Field(alias="credentialsAvailable")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
