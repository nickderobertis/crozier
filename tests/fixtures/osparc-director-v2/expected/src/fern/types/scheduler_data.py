

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callbacks_mapping import CallbacksMapping
from .compose_spec_label_dict import ComposeSpecLabelDict
from .dynamic_sidecar import DynamicSidecar
from .hardware_info import HardwareInfo
from .nat_rule import NatRule
from .path_mappings_label import PathMappingsLabel
from .pricing_info import PricingInfo
from .restart_policy import RestartPolicy
from .user_id_int import UserIdInt
from .user_preferences_version_source import UserPreferencesVersionSource
from .wallet_info_output import WalletInfoOutput


class SchedulerData(UniversalBaseModel):
    paths_mapping: PathMappingsLabel
    is_collaborative: typing.Optional[bool] = None
    simcore_service_compose_spec: typing_extensions.Annotated[
        typing.Optional[ComposeSpecLabelDict],
        FieldMetadata(alias="simcore.service.compose-spec"),
        pydantic.Field(
            alias="simcore.service.compose-spec",
            description="json encoded docker-compose specifications. see https://docs.docker.com/compose/compose-file/, only used by dynamic-sidecar.",
        ),
    ] = None
    """
    json encoded docker-compose specifications. see https://docs.docker.com/compose/compose-file/, only used by dynamic-sidecar.
    """

    simcore_service_container_http_entrypoint: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="simcore.service.container-http-entrypoint"),
        pydantic.Field(
            alias="simcore.service.container-http-entrypoint",
            description="When a docker-compose specifications is provided, the container where the traffic must flow has to be specified. Required by dynamic-sidecar when compose_spec is set.",
        ),
    ] = None
    """
    When a docker-compose specifications is provided, the container where the traffic must flow has to be specified. Required by dynamic-sidecar when compose_spec is set.
    """

    user_preferences_path: typing.Optional[str] = None
    user_preferences_version_source: typing.Optional[UserPreferencesVersionSource] = None
    simcore_service_restart_policy: typing_extensions.Annotated[
        typing.Optional[RestartPolicy],
        FieldMetadata(alias="simcore.service.restart-policy"),
        pydantic.Field(
            alias="simcore.service.restart-policy",
            description="the dynamic-sidecar can restart all running containers on certain events. Supported events:\n- `no-restart` default\n- `on-inputs-downloaded` after inputs are downloaded",
        ),
    ] = None
    """
    the dynamic-sidecar can restart all running containers on certain events. Supported events:
    - `no-restart` default
    - `on-inputs-downloaded` after inputs are downloaded
    """

    simcore_service_containers_allowed_outgoing_permit_list: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.List[NatRule]]]],
        FieldMetadata(alias="simcore.service.containers-allowed-outgoing-permit-list"),
        pydantic.Field(
            alias="simcore.service.containers-allowed-outgoing-permit-list",
            description="allow internet access to certain domain names and ports per container",
        ),
    ] = None
    """
    allow internet access to certain domain names and ports per container
    """

    simcore_service_containers_allowed_outgoing_internet: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="simcore.service.containers-allowed-outgoing-internet"),
        pydantic.Field(
            alias="simcore.service.containers-allowed-outgoing-internet",
            description="allow complete internet access to containers in here",
        ),
    ] = None
    """
    allow complete internet access to containers in here
    """

    callbacks_mapping: typing.Optional[CallbacksMapping] = None
    tracing: typing.Optional[bool] = None
    service_key: str = pydantic.Field()
    """
    distinctive name for the node based on the docker registry path
    """

    service_version: str = pydantic.Field()
    """
    semantic version number of the node
    """

    user_id: UserIdInt
    project_id: str
    service_uuid: str
    service_name: str = pydantic.Field()
    """
    Name of the current dynamic-sidecar being observed
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Uniquely identify the dynamic sidecar session (a.k.a. 2 subsequent exact same services will have a different run_id)
    """

    hostname: str = pydantic.Field()
    """
    dy-sidecar's service hostname (provided by docker-swarm)
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    dynamic-sidecar port
    """

    dynamic_sidecar: DynamicSidecar = pydantic.Field()
    """
    stores information fetched from the dynamic-sidecar
    """

    requires_data_mounting: typing.Optional[bool] = None
    dynamic_sidecar_network_name: str = pydantic.Field()
    """
    overlay network biding the proxy to the container spaned by the dynamic-sidecar
    """

    simcore_traefik_zone: str = pydantic.Field()
    """
    required for Traefik to correctly route requests to the spawned container
    """

    service_port: typing.Optional[int] = pydantic.Field(default=None)
    """
    port where the service is exposed defined by the service; NOTE: temporary default because it will be changed once the service is started, this value is fetched from the service start spec
    """

    service_resources: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    service resources used to enforce limits
    """

    request_dns: str = pydantic.Field()
    """
    used when configuring the CORS options on the proxy
    """

    request_scheme: str = pydantic.Field()
    """
    used when configuring the CORS options on the proxy
    """

    request_simcore_user_agent: str = pydantic.Field()
    """
    used as label to filter out the metrics from the cAdvisor prometheus metrics
    """

    proxy_service_name: str = pydantic.Field()
    """
    service name given to the proxy
    """

    proxy_admin_api_port: typing.Optional[int] = pydantic.Field(default=None)
    """
    used as the admin endpoint API port
    """

    wallet_info: typing.Optional[WalletInfoOutput] = pydantic.Field(default=None)
    """
    contains information about the wallet used to bill the running service
    """

    pricing_info: typing.Optional[PricingInfo] = pydantic.Field(default=None)
    """
    contains pricing information so we know what is the cost of running of the service
    """

    hardware_info: typing.Optional[HardwareInfo] = pydantic.Field(default=None)
    """
    contains hardware information so we know on which hardware to run the service
    """

    product_name: str = pydantic.Field()
    """
    Current product upon which this service is scheduled
    """

    version_display: typing.Optional[str] = pydantic.Field(default=None)
    """
    catalog's human readable name for this service version
    """

    product_api_base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base URL for the current product's API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
