

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .billable_owner_type import BillableOwnerType
from .client_usage_session import ClientUsageSession
from .connection_info_body import ConnectionInfoBody
from .consumer_type import ConsumerType
from .container_info_body import ContainerInfoBody
from .failover_details import FailoverDetails
from .git_status import GitStatus
from .runtime_constraints_body import RuntimeConstraintsBody
from .seed_info_body import SeedInfoBody
from .subscription_data import SubscriptionData


class CloudEnvironmentResult(UniversalBaseModel):
    access_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ] = None
    active: typing.Optional[dt.datetime] = None
    auto_shutdown_delay_minutes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="autoShutdownDelayMinutes"),
        pydantic.Field(alias="autoShutdownDelayMinutes"),
    ] = None
    billable_owner_type: typing_extensions.Annotated[
        typing.Optional[BillableOwnerType],
        FieldMetadata(alias="billableOwnerType"),
        pydantic.Field(alias="billableOwnerType"),
    ] = None
    client_usage: typing_extensions.Annotated[
        typing.Optional[ClientUsageSession], FieldMetadata(alias="clientUsage"), pydantic.Field(alias="clientUsage")
    ] = None
    connection: typing.Optional[ConnectionInfoBody] = None
    container: typing.Optional[ContainerInfoBody] = None
    container_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="containerImage"), pydantic.Field(alias="containerImage")
    ] = None
    create_from_prebuild: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="createFromPrebuild"), pydantic.Field(alias="createFromPrebuild")
    ] = None
    created: typing.Optional[dt.datetime] = None
    display_storage_utilization_in_kb: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="displayStorageUtilizationInKb"),
        pydantic.Field(alias="displayStorageUtilizationInKb"),
    ] = None
    exported_blob_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="exportedBlobUrl"), pydantic.Field(alias="exportedBlobUrl")
    ] = None
    failover_details: typing_extensions.Annotated[
        typing.Optional[FailoverDetails],
        FieldMetadata(alias="failoverDetails"),
        pydantic.Field(alias="failoverDetails"),
    ] = None
    features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    friendly_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="friendlyName"), pydantic.Field(alias="friendlyName")
    ] = None
    git_status: typing_extensions.Annotated[
        typing.Optional[GitStatus], FieldMetadata(alias="gitStatus"), pydantic.Field(alias="gitStatus")
    ] = None
    id: typing.Optional[str] = None
    last_state_update_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastStateUpdateReason"),
        pydantic.Field(alias="lastStateUpdateReason"),
    ] = None
    last_used: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUsed"), pydantic.Field(alias="lastUsed")
    ] = None
    location: typing.Optional[str] = None
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ] = None
    owner_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")
    ] = None
    plan_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="planId"), pydantic.Field(alias="planId")
    ] = None
    platform: typing.Optional[str] = None
    port_forwarding_connection: typing_extensions.Annotated[
        typing.Optional[ConnectionInfoBody],
        FieldMetadata(alias="portForwardingConnection"),
        pydantic.Field(alias="portForwardingConnection"),
    ] = None
    prebuild_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prebuildType"), pydantic.Field(alias="prebuildType")
    ] = None
    recent_folders: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="recentFolders"), pydantic.Field(alias="recentFolders")
    ] = None
    resource_tier: typing_extensions.Annotated[
        typing.Optional[ConsumerType], FieldMetadata(alias="resourceTier"), pydantic.Field(alias="resourceTier")
    ] = None
    runtime_constraints: typing_extensions.Annotated[
        typing.Optional[RuntimeConstraintsBody],
        FieldMetadata(alias="runtimeConstraints"),
        pydantic.Field(alias="runtimeConstraints"),
    ] = None
    seed: typing.Optional[SeedInfoBody] = None
    sku_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="skuDisplayName"), pydantic.Field(alias="skuDisplayName")
    ] = None
    sku_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="skuName"), pydantic.Field(alias="skuName")
    ] = None
    state: typing.Optional[str] = None
    storage_utilization_in_kb: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="storageUtilizationInKb"),
        pydantic.Field(alias="storageUtilizationInKb"),
    ] = None
    subscription_data: typing_extensions.Annotated[
        typing.Optional[SubscriptionData],
        FieldMetadata(alias="subscriptionData"),
        pydantic.Field(alias="subscriptionData"),
    ] = None
    template_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="templateStatus"), pydantic.Field(alias="templateStatus")
    ] = None
    type: typing.Optional[str] = None
    updated: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
