

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth0config import Auth0Config
from .clever_settings import CleverSettings
from .elastic_config import ElasticConfig
from .ip_filtering import IpFiltering
from .mailer_settings import MailerSettings
from .webhook import Webhook


class GlobalConfig(UniversalBaseModel):
    """
    The global config object of Otoroshi, used to customize settings of the current Otoroshi instance
    """

    alerts_emails: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="alertsEmails")] = pydantic.Field()
    """
    Email addresses that will receive all Otoroshi alert events
    """

    alerts_webhooks: typing_extensions.Annotated[typing.List[Webhook], FieldMetadata(alias="alertsWebhooks")] = (
        pydantic.Field()
    )
    """
    Webhook that will receive all Otoroshi alert events
    """

    analytics_webhooks: typing_extensions.Annotated[typing.List[Webhook], FieldMetadata(alias="analyticsWebhooks")] = (
        pydantic.Field()
    )
    """
    Webhook that will receive all internal Otoroshi events
    """

    api_read_only: typing_extensions.Annotated[bool, FieldMetadata(alias="apiReadOnly")] = pydantic.Field()
    """
    If enabled, Admin API won't be able to write/update/delete entities
    """

    auto_link_to_default_group: typing_extensions.Annotated[bool, FieldMetadata(alias="autoLinkToDefaultGroup")] = (
        pydantic.Field()
    )
    """
    If not defined, every new service descriptor will be added to the default group
    """

    backoffice_auth0config: typing_extensions.Annotated[
        typing.Optional[Auth0Config], FieldMetadata(alias="backofficeAuth0Config")
    ] = pydantic.Field(default=None)
    """
    Optional configuration for the backoffice Auth0 domain
    """

    clever_settings: typing_extensions.Annotated[
        typing.Optional[CleverSettings], FieldMetadata(alias="cleverSettings")
    ] = pydantic.Field(default=None)
    """
    Optional CleverCloud configuration
    """

    elastic_reads_config: typing_extensions.Annotated[
        typing.Optional[ElasticConfig], FieldMetadata(alias="elasticReadsConfig")
    ] = pydantic.Field(default=None)
    """
    Config. for elastic reads
    """

    elastic_writes_configs: typing_extensions.Annotated[
        typing.Optional[typing.List[ElasticConfig]], FieldMetadata(alias="elasticWritesConfigs")
    ] = pydantic.Field(default=None)
    """
    Configs. for Elastic writes
    """

    endless_ip_addresses: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="endlessIpAddresses")] = (
        pydantic.Field()
    )
    """
    IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros
    """

    ip_filtering: typing_extensions.Annotated[IpFiltering, FieldMetadata(alias="ipFiltering")]
    limit_concurrent_requests: typing_extensions.Annotated[bool, FieldMetadata(alias="limitConcurrentRequests")] = (
        pydantic.Field()
    )
    """
    If enabled, Otoroshi will reject new request if too much at the same time
    """

    lines: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Possibles lines for Otoroshi
    """

    mailer_settings: typing_extensions.Annotated[
        typing.Optional[MailerSettings], FieldMetadata(alias="mailerSettings")
    ] = pydantic.Field(default=None)
    """
    Optional mailer configuration
    """

    max_concurrent_requests: typing_extensions.Annotated[int, FieldMetadata(alias="maxConcurrentRequests")] = (
        pydantic.Field()
    )
    """
    The number of authorized request processed at the same time
    """

    max_http10response_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxHttp10ResponseSize")
    ] = pydantic.Field(default=None)
    """
    The max size in bytes of an HTTP 1.0 response
    """

    max_logs_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxLogsSize")] = (
        pydantic.Field(default=None)
    )
    """
    Number of events kept locally
    """

    middle_fingers: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="middleFingers")] = (
        pydantic.Field(default=None)
    )
    """
    Use middle finger emoji as a response character for endless HTTP responses
    """

    per_ip_throttling_quota: typing_extensions.Annotated[int, FieldMetadata(alias="perIpThrottlingQuota")] = (
        pydantic.Field()
    )
    """
    Authorized number of calls per second globally per IP address, measured on 10 seconds
    """

    private_apps_auth0config: typing_extensions.Annotated[
        typing.Optional[Auth0Config], FieldMetadata(alias="privateAppsAuth0Config")
    ] = pydantic.Field(default=None)
    """
    Optional configuration for the private apps Auth0 domain
    """

    stream_entity_only: typing_extensions.Annotated[bool, FieldMetadata(alias="streamEntityOnly")] = pydantic.Field()
    """
    HTTP will be streamed only. Doesn't work with old browsers
    """

    throttling_quota: typing_extensions.Annotated[int, FieldMetadata(alias="throttlingQuota")] = pydantic.Field()
    """
    Authorized number of calls per second globally, measured on 10 seconds
    """

    u2f_login_only: typing_extensions.Annotated[bool, FieldMetadata(alias="u2fLoginOnly")] = pydantic.Field()
    """
    If enabled, login to backoffice through Auth0 will be disabled
    """

    use_circuit_breakers: typing_extensions.Annotated[bool, FieldMetadata(alias="useCircuitBreakers")] = (
        pydantic.Field()
    )
    """
    If enabled, services will be authorized to use circuit breakers
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
