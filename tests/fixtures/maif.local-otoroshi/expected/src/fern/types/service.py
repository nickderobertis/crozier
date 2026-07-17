

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .canary import Canary
from .chaos_config import ChaosConfig
from .client_config import ClientConfig
from .cors_settings import CorsSettings
from .exposed_api import ExposedApi
from .gzip import Gzip
from .health_check import HealthCheck
from .ip_filtering import IpFiltering
from .redirection_settings import RedirectionSettings
from .service_jwt_verifier import ServiceJwtVerifier
from .service_sec_com_settings import ServiceSecComSettings
from .statsd_config import StatsdConfig
from .target import Target


class Service(UniversalBaseModel):
    """
    An otoroshi service descriptor. Represent a forward HTTP call on a domain to another location with some optional api management mecanism
    """

    canary: typing_extensions.Annotated[
        typing.Optional[Canary], FieldMetadata(alias="Canary"), pydantic.Field(alias="Canary")
    ] = None
    additional_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="additionalHeaders"),
        pydantic.Field(
            alias="additionalHeaders",
            description="Specify headers that will be added to each client request. Useful to add authentication",
        ),
    ] = None
    """
    Specify headers that will be added to each client request. Useful to add authentication
    """

    api: typing.Optional[ExposedApi] = None
    auth_config_ref: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="authConfigRef"),
        pydantic.Field(alias="authConfigRef", description="A reference to a global auth module config"),
    ] = None
    """
    A reference to a global auth module config
    """

    build_mode: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="buildMode"),
        pydantic.Field(alias="buildMode", description="Display a construction page when a user try to use the service"),
    ]
    """
    Display a construction page when a user try to use the service
    """

    chaos_config: typing_extensions.Annotated[
        typing.Optional[ChaosConfig], FieldMetadata(alias="chaosConfig"), pydantic.Field(alias="chaosConfig")
    ] = None
    client_config: typing_extensions.Annotated[
        typing.Optional[ClientConfig], FieldMetadata(alias="clientConfig"), pydantic.Field(alias="clientConfig")
    ] = None
    client_validator_ref: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientValidatorRef"),
        pydantic.Field(alias="clientValidatorRef", description="A reference to validation authority"),
    ] = None
    """
    A reference to validation authority
    """

    cors: typing.Optional[CorsSettings] = None
    domain: str = pydantic.Field()
    """
    The domain on which the service is available.
    """

    enabled: bool = pydantic.Field()
    """
    Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist
    """

    enforce_secure_communication: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="enforceSecureCommunication"),
        pydantic.Field(
            alias="enforceSecureCommunication",
            description="When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside",
        ),
    ]
    """
    When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside
    """

    env: str = pydantic.Field()
    """
    The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'
    """

    force_https: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="forceHttps"),
        pydantic.Field(alias="forceHttps", description="Will force redirection to https:// if not present"),
    ]
    """
    Will force redirection to https:// if not present
    """

    groups: typing.List[str] = pydantic.Field()
    """
    Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group
    """

    gzip: typing.Optional[Gzip] = None
    headers_verification: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="headersVerification"),
        pydantic.Field(alias="headersVerification", description="Specify headers that will be verified after routing."),
    ] = None
    """
    Specify headers that will be verified after routing.
    """

    health_check: typing_extensions.Annotated[
        typing.Optional[HealthCheck], FieldMetadata(alias="healthCheck"), pydantic.Field(alias="healthCheck")
    ] = None
    id: str = pydantic.Field()
    """
    A unique random string to identify your service
    """

    ip_filtering: typing_extensions.Annotated[
        typing.Optional[IpFiltering], FieldMetadata(alias="ipFiltering"), pydantic.Field(alias="ipFiltering")
    ] = None
    jwt_verifier: typing_extensions.Annotated[
        typing.Optional[ServiceJwtVerifier], FieldMetadata(alias="jwtVerifier"), pydantic.Field(alias="jwtVerifier")
    ] = None
    local_host: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localHost"),
        pydantic.Field(alias="localHost", description="The host used localy, mainly localhost:xxxx"),
    ] = None
    """
    The host used localy, mainly localhost:xxxx
    """

    local_scheme: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localScheme"),
        pydantic.Field(alias="localScheme", description="The scheme used localy, mainly http"),
    ] = None
    """
    The scheme used localy, mainly http
    """

    maintenance_mode: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="maintenanceMode"),
        pydantic.Field(
            alias="maintenanceMode", description="Display a maintainance page when a user try to use the service"
        ),
    ]
    """
    Display a maintainance page when a user try to use the service
    """

    matching_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="matchingHeaders"),
        pydantic.Field(
            alias="matchingHeaders",
            description="Specify headers that MUST be present on client request to route it. Useful to implement versioning",
        ),
    ] = None
    """
    Specify headers that MUST be present on client request to route it. Useful to implement versioning
    """

    matching_root: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="matchingRoot"),
        pydantic.Field(alias="matchingRoot", description="The root path on which the service is available"),
    ] = None
    """
    The root path on which the service is available
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Just a bunch of random properties
    """

    name: str = pydantic.Field()
    """
    The name of your service. Only for debug and human readability purposes
    """

    override_host: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="overrideHost"),
        pydantic.Field(alias="overrideHost", description="Host header will be overriden with Host of the target"),
    ] = None
    """
    Host header will be overriden with Host of the target
    """

    private_app: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="privateApp"),
        pydantic.Field(
            alias="privateApp",
            description="When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain",
        ),
    ]
    """
    When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain
    """

    private_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="privatePatterns"),
        pydantic.Field(
            alias="privatePatterns",
            description="If you define a public pattern that is a little bit too much, you can make some of public URL private again",
        ),
    ] = None
    """
    If you define a public pattern that is a little bit too much, you can make some of public URL private again
    """

    public_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="publicPatterns"),
        pydantic.Field(
            alias="publicPatterns",
            description="By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'",
        ),
    ] = None
    """
    By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'
    """

    redirect_to_local: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="redirectToLocal"),
        pydantic.Field(
            alias="redirectToLocal",
            description="If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests",
        ),
    ] = None
    """
    If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests
    """

    redirection: typing.Optional[RedirectionSettings] = None
    root: str = pydantic.Field()
    """
    Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar
    """

    sec_com_excluded_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="secComExcludedPatterns"),
        pydantic.Field(alias="secComExcludedPatterns", description="URI patterns excluded from secured communications"),
    ] = None
    """
    URI patterns excluded from secured communications
    """

    sec_com_settings: typing_extensions.Annotated[
        typing.Optional[ServiceSecComSettings],
        FieldMetadata(alias="secComSettings"),
        pydantic.Field(alias="secComSettings"),
    ] = None
    send_otoroshi_headers_back: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sendOtoroshiHeadersBack"),
        pydantic.Field(
            alias="sendOtoroshiHeadersBack",
            description="When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...",
        ),
    ] = None
    """
    When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...
    """

    statsd_config: typing_extensions.Annotated[
        typing.Optional[StatsdConfig], FieldMetadata(alias="statsdConfig"), pydantic.Field(alias="statsdConfig")
    ] = None
    subdomain: str = pydantic.Field()
    """
    The subdomain on which the service is available
    """

    targets: typing.List[Target] = pydantic.Field()
    """
    The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures
    """

    transformer_ref: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transformerRef"),
        pydantic.Field(alias="transformerRef", description="A reference to a request transformer"),
    ] = None
    """
    A reference to a request transformer
    """

    user_facing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="userFacing"),
        pydantic.Field(
            alias="userFacing",
            description="The fact that this service will be seen by users and cannot be impacted by the Snow Monkey",
        ),
    ] = None
    """
    The fact that this service will be seen by users and cannot be impacted by the Snow Monkey
    """

    x_forwarded_headers: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="xForwardedHeaders"),
        pydantic.Field(alias="xForwardedHeaders", description="Send X-Forwarded-* headers"),
    ] = None
    """
    Send X-Forwarded-* headers
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
