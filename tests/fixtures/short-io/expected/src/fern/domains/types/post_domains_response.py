

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_domains_response_https_level import PostDomainsResponseHttpsLevel
from .post_domains_response_link_type import PostDomainsResponseLinkType
from .post_domains_response_robots import PostDomainsResponseRobots
from .post_domains_response_state import PostDomainsResponseState


class PostDomainsResponse(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Domain ID
    """

    hostname: str
    unicode_hostname: typing_extensions.Annotated[
        str, FieldMetadata(alias="unicodeHostname"), pydantic.Field(alias="unicodeHostname")
    ]
    state: PostDomainsResponseState
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    team_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="TeamId"), pydantic.Field(alias="TeamId")
    ] = None
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="OrganizationId"), pydantic.Field(alias="OrganizationId")
    ] = None
    has_favicon: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasFavicon"), pydantic.Field(alias="hasFavicon")
    ]
    segment_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="segmentKey"), pydantic.Field(alias="segmentKey")
    ] = None
    hide_referer: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hideReferer"), pydantic.Field(alias="hideReferer")
    ]
    link_type: typing_extensions.Annotated[
        PostDomainsResponseLinkType, FieldMetadata(alias="linkType"), pydantic.Field(alias="linkType")
    ]
    cloaking: bool = pydantic.Field()
    """
    Enable cloaking for all links on the domain
    """

    hide_visitor_ip: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hideVisitorIp"),
        pydantic.Field(alias="hideVisitorIp", description="Don't store visitor IPs in our database"),
    ]
    """
    Don't store visitor IPs in our database
    """

    enable_ai: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="enableAI"),
        pydantic.Field(alias="enableAI", description="Enable AI for all links on the domain"),
    ]
    """
    Enable AI for all links on the domain
    """

    https_level: typing_extensions.Annotated[
        PostDomainsResponseHttpsLevel, FieldMetadata(alias="httpsLevel"), pydantic.Field(alias="httpsLevel")
    ]
    https_links: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="httpsLinks"), pydantic.Field(alias="httpsLinks")
    ] = None
    webhook_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webhookURL"), pydantic.Field(alias="webhookURL")
    ] = None
    integration_ga: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="integrationGA"), pydantic.Field(alias="integrationGA")
    ] = None
    integration_fb: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="integrationFB"), pydantic.Field(alias="integrationFB")
    ] = None
    integration_tt: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="integrationTT"), pydantic.Field(alias="integrationTT")
    ] = None
    integration_adroll: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="integrationAdroll"), pydantic.Field(alias="integrationAdroll")
    ] = None
    integration_gtm: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="integrationGTM"), pydantic.Field(alias="integrationGTM")
    ] = None
    client_storage: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="clientStorage"),
        pydantic.Field(alias="clientStorage"),
    ] = None
    case_sensitive: typing_extensions.Annotated[
        bool, FieldMetadata(alias="caseSensitive"), pydantic.Field(alias="caseSensitive")
    ]
    increment_counter: typing_extensions.Annotated[
        str, FieldMetadata(alias="incrementCounter"), pydantic.Field(alias="incrementCounter")
    ]
    robots: PostDomainsResponseRobots
    ssl_cert_expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="sslCertExpirationDate"),
        pydantic.Field(alias="sslCertExpirationDate"),
    ] = None
    ssl_cert_installed_success: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sslCertInstalledSuccess"),
        pydantic.Field(alias="sslCertInstalledSuccess"),
    ] = None
    domain_registration_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="domainRegistrationId"), pydantic.Field(alias="domainRegistrationId")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="UserId"), pydantic.Field(alias="UserId")
    ] = None
    export_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="exportEnabled"), pydantic.Field(alias="exportEnabled")
    ]
    enable_conversion_tracking: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableConversionTracking"), pydantic.Field(alias="enableConversionTracking")
    ]
    qr_scan_tracking: typing_extensions.Annotated[
        bool, FieldMetadata(alias="qrScanTracking"), pydantic.Field(alias="qrScanTracking")
    ]
    dns_config_deprecated: typing_extensions.Annotated[
        bool, FieldMetadata(alias="dnsConfigDeprecated"), pydantic.Field(alias="dnsConfigDeprecated")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
