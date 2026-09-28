

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_elastic_analytics_config import OtoroshiModelsElasticAnalyticsConfig
from .otoroshi_models_global_config_back_office_auth_ref import OtoroshiModelsGlobalConfigBackOfficeAuthRef
from .otoroshi_models_global_config_clever_settings import OtoroshiModelsGlobalConfigCleverSettings
from .otoroshi_models_global_config_elastic_reads_config import OtoroshiModelsGlobalConfigElasticReadsConfig
from .otoroshi_models_global_config_kafka_config import OtoroshiModelsGlobalConfigKafkaConfig
from .otoroshi_models_global_config_mailer_settings import OtoroshiModelsGlobalConfigMailerSettings
from .otoroshi_models_global_config_statsd_config import OtoroshiModelsGlobalConfigStatsdConfig
from .otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from .otoroshi_models_webhook import OtoroshiModelsWebhook


class OtoroshiModelsGlobalConfig(UniversalBaseModel):
    """
    The global config (dynamic) for otoroshi
    """

    geolocation_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="geolocationSettings"),
        pydantic.Field(alias="geolocationSettings"),
    ] = None
    alerts_emails: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="alertsEmails"),
        pydantic.Field(alias="alertsEmails", description="Email addresses that will receive all Otoroshi alert events"),
    ] = None
    """
    Email addresses that will receive all Otoroshi alert events
    """

    throttling_quota: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="throttlingQuota"),
        pydantic.Field(alias="throttlingQuota", description="Authorized number of calls per window globally"),
    ] = None
    """
    Authorized number of calls per window globally
    """

    anonymous_reporting: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="anonymousReporting"),
        pydantic.Field(alias="anonymousReporting", description="???"),
    ] = None
    """
    ???
    """

    max_webhook_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxWebhookSize"),
        pydantic.Field(alias="maxWebhookSize", description="Max number of items in webhooks"),
    ] = None
    """
    Max number of items in webhooks
    """

    env: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    ???
    """

    max_concurrent_requests: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxConcurrentRequests"),
        pydantic.Field(
            alias="maxConcurrentRequests", description="The number of authorized request processed at the same time"
        ),
    ] = None
    """
    The number of authorized request processed at the same time
    """

    clever_settings: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigCleverSettings],
        FieldMetadata(alias="cleverSettings"),
        pydantic.Field(alias="cleverSettings", description="Optional CleverCloud configuration"),
    ] = None
    """
    Optional CleverCloud configuration
    """

    templates: typing.Optional[typing.Any] = None
    endless_ip_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="endlessIpAddresses"),
        pydantic.Field(
            alias="endlessIpAddresses",
            description="IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros",
        ),
    ] = None
    """
    IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros
    """

    plugins: typing.Optional[typing.Any] = None
    kafka_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigKafkaConfig],
        FieldMetadata(alias="kafkaConfig"),
        pydantic.Field(alias="kafkaConfig", description="Kafka settings"),
    ] = None
    """
    Kafka settings
    """

    max_logs_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxLogsSize"),
        pydantic.Field(alias="maxLogsSize", description="Number of events kept locally"),
    ] = None
    """
    Number of events kept locally
    """

    proxies: typing.Optional[typing.Any] = None
    enable_embedded_metrics: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="enableEmbeddedMetrics"),
        pydantic.Field(alias="enableEmbeddedMetrics", description="Enable embedded metrics"),
    ] = None
    """
    Enable embedded metrics
    """

    elastic_reads_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigElasticReadsConfig],
        FieldMetadata(alias="elasticReadsConfig"),
        pydantic.Field(alias="elasticReadsConfig", description="Config. for elastic reads"),
    ] = None
    """
    Config. for elastic reads
    """

    trust_x_forwarded: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="trustXForwarded"),
        pydantic.Field(alias="trustXForwarded", description="Use X-Forwarded-* headers for routing"),
    ] = None
    """
    Use X-Forwarded-* headers for routing
    """

    quotas_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="quotasSettings"), pydantic.Field(alias="quotasSettings")
    ] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    limit_concurrent_requests: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="limitConcurrentRequests"),
        pydantic.Field(
            alias="limitConcurrentRequests",
            description="If enabled, Otoroshi will reject new request if too much at the same time",
        ),
    ] = None
    """
    If enabled, Otoroshi will reject new request if too much at the same time
    """

    use_akka_http_client: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useAkkaHttpClient"),
        pydantic.Field(alias="useAkkaHttpClient", description="Globally use akka http client for everything"),
    ] = None
    """
    Globally use akka http client for everything
    """

    elastic_writes_configs: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiModelsElasticAnalyticsConfig]],
        FieldMetadata(alias="elasticWritesConfigs"),
        pydantic.Field(alias="elasticWritesConfigs", description="Configs. for Elastic writes"),
    ] = None
    """
    Configs. for Elastic writes
    """

    log_analytics_on_server: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="logAnalyticsOnServer"),
        pydantic.Field(alias="logAnalyticsOnServer", description="Log analytics event on the server"),
    ] = None
    """
    Log analytics event on the server
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    api_read_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="apiReadOnly"),
        pydantic.Field(
            alias="apiReadOnly", description="If enabled, Admin API won't be able to write/update/delete entities"
        ),
    ] = None
    """
    If enabled, Admin API won't be able to write/update/delete entities
    """

    back_office_auth_ref: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigBackOfficeAuthRef],
        FieldMetadata(alias="backOfficeAuthRef"),
        pydantic.Field(alias="backOfficeAuthRef", description="Id of the auth module used for otoroshi-ui login"),
    ] = None
    """
    Id of the auth module used for otoroshi-ui login
    """

    stream_entity_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="streamEntityOnly"),
        pydantic.Field(
            alias="streamEntityOnly", description="HTTP will be streamed only. Doesn't work with old browsers"
        ),
    ] = None
    """
    HTTP will be streamed only. Doesn't work with old browsers
    """

    otoroshi_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="otoroshiId"),
        pydantic.Field(alias="otoroshiId", description="Unique id for this otoroshi instance"),
    ] = None
    """
    Unique id for this otoroshi instance
    """

    mailer_settings: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigMailerSettings],
        FieldMetadata(alias="mailerSettings"),
        pydantic.Field(alias="mailerSettings", description="Optional mailer configuration"),
    ] = None
    """
    Optional mailer configuration
    """

    lines: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Possibles lines for Otoroshi
    """

    extensions: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    ???
    """

    middle_fingers: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="middleFingers"),
        pydantic.Field(
            alias="middleFingers",
            description="Use middle finger emoji as a response character for endless HTTP responses",
        ),
    ] = None
    """
    Use middle finger emoji as a response character for endless HTTP responses
    """

    analytics_webhooks: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiModelsWebhook]],
        FieldMetadata(alias="analyticsWebhooks"),
        pydantic.Field(alias="analyticsWebhooks", description="Webhook that will receive all internal Otoroshi events"),
    ] = None
    """
    Webhook that will receive all internal Otoroshi events
    """

    auto_cert: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="autoCert"), pydantic.Field(alias="autoCert")
    ] = None
    maintenance_mode: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="maintenanceMode"),
        pydantic.Field(alias="maintenanceMode", description="Global maintenant mode"),
    ] = None
    """
    Global maintenant mode
    """

    init_with_new_engine: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="initWithNewEngine"),
        pydantic.Field(alias="initWithNewEngine", description="Was this instance init with new engine as default"),
    ] = None
    """
    Was this instance init with new engine as default
    """

    lets_encrypt_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="letsEncryptSettings"),
        pydantic.Field(alias="letsEncryptSettings"),
    ] = None
    snow_monkey_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsSnowMonkeyConfig],
        FieldMetadata(alias="snowMonkeyConfig"),
        pydantic.Field(alias="snowMonkeyConfig", description="Snowmonky settings"),
    ] = None
    """
    Snowmonky settings
    """

    scripts: typing.Optional[typing.Any] = None
    per_ip_throttling_quota: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="perIpThrottlingQuota"),
        pydantic.Field(
            alias="perIpThrottlingQuota", description="Authorized number of calls per window globally per IP address"
        ),
    ] = None
    """
    Authorized number of calls per window globally per IP address
    """

    use_circuit_breakers: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useCircuitBreakers"),
        pydantic.Field(
            alias="useCircuitBreakers", description="If enabled, services will be authorized to use circuit breakers"
        ),
    ] = None
    """
    If enabled, services will be authorized to use circuit breakers
    """

    max_http10response_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxHttp10ResponseSize"),
        pydantic.Field(alias="maxHttp10ResponseSize", description="The max size in bytes of an HTTP 1.0 response"),
    ] = None
    """
    The max size in bytes of an HTTP 1.0 response
    """

    tls_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="tlsSettings"), pydantic.Field(alias="tlsSettings")
    ] = None
    statsd_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsGlobalConfigStatsdConfig],
        FieldMetadata(alias="statsdConfig"),
        pydantic.Field(alias="statsdConfig", description="Statsd settings (agent connection)"),
    ] = None
    """
    Statsd settings (agent connection)
    """

    auto_link_to_default_group: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoLinkToDefaultGroup"),
        pydantic.Field(
            alias="autoLinkToDefaultGroup",
            description="If not defined, every new service descriptor will be added to the default group",
        ),
    ] = None
    """
    If not defined, every new service descriptor will be added to the default group
    """

    alerts_webhooks: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiModelsWebhook]],
        FieldMetadata(alias="alertsWebhooks"),
        pydantic.Field(alias="alertsWebhooks", description="Webhook that will receive all Otoroshi alert events"),
    ] = None
    """
    Webhook that will receive all Otoroshi alert events
    """

    ip_filtering: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="ipFiltering"), pydantic.Field(alias="ipFiltering")
    ] = None
    u2f_login_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="u2fLoginOnly"),
        pydantic.Field(
            alias="u2fLoginOnly", description="If enabled, login to backoffice through Auth0 will be disabled"
        ),
    ] = None
    """
    If enabled, login to backoffice through Auth0 will be disabled
    """

    user_agent_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="userAgentSettings"), pydantic.Field(alias="userAgentSettings")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
