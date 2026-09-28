

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
from .otoroshi_models_service_descriptor_auth_config_ref import OtoroshiModelsServiceDescriptorAuthConfigRef
from .otoroshi_models_service_descriptor_client_validator_ref import OtoroshiModelsServiceDescriptorClientValidatorRef
from .otoroshi_models_service_descriptor_issue_cert_ca import OtoroshiModelsServiceDescriptorIssueCertCa
from .otoroshi_models_service_descriptor_matching_root import OtoroshiModelsServiceDescriptorMatchingRoot
from .otoroshi_models_target import OtoroshiModelsTarget


class OtoroshiModelsServiceDescriptor(UniversalBaseModel):
    """
    ???
    """

    build_mode: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="buildMode"), pydantic.Field(alias="buildMode", description="???")
    ] = None
    """
    ???
    """

    hosts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    private_app: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="privateApp"), pydantic.Field(alias="privateApp", description="???")
    ] = None
    """
    ???
    """

    local_scheme: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="localScheme"), pydantic.Field(alias="localScheme", description="???")
    ] = None
    """
    ???
    """

    auth_config_ref: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef],
        FieldMetadata(alias="authConfigRef"),
        pydantic.Field(alias="authConfigRef", description="???"),
    ] = None
    """
    ???
    """

    issue_cert_ca: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa],
        FieldMetadata(alias="issueCertCA"),
        pydantic.Field(alias="issueCertCA", description="???"),
    ] = None
    """
    ???
    """

    root: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    additional_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="additionalHeaders"),
        pydantic.Field(alias="additionalHeaders", description="???"),
    ] = None
    """
    ???
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    client_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="clientConfig"), pydantic.Field(alias="clientConfig")
    ] = None
    matching_root: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot],
        FieldMetadata(alias="matchingRoot"),
        pydantic.Field(alias="matchingRoot", description="???"),
    ] = None
    """
    ???
    """

    force_https: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="forceHttps"), pydantic.Field(alias="forceHttps", description="???")
    ] = None
    """
    ???
    """

    local_host: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="localHost"), pydantic.Field(alias="localHost", description="???")
    ] = None
    """
    ???
    """

    send_otoroshi_headers_back: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sendOtoroshiHeadersBack"),
        pydantic.Field(alias="sendOtoroshiHeadersBack", description="???"),
    ] = None
    """
    ???
    """

    health_check: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="healthCheck"), pydantic.Field(alias="healthCheck")
    ] = None
    strictly_private: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="strictlyPrivate"),
        pydantic.Field(alias="strictlyPrivate", description="???"),
    ] = None
    """
    ???
    """

    detect_api_key_sooner: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="detectApiKeySooner"),
        pydantic.Field(alias="detectApiKeySooner", description="???"),
    ] = None
    """
    ???
    """

    allow_http10: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowHttp10"),
        pydantic.Field(alias="allowHttp10", description="???"),
    ] = None
    """
    ???
    """

    subdomain: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    paths: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    strip_path: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="stripPath"), pydantic.Field(alias="stripPath", description="???")
    ] = None
    """
    ???
    """

    sec_com_algo_challenge_oto_to_back: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsAlgoSettings],
        FieldMetadata(alias="secComAlgoChallengeOtoToBack"),
        pydantic.Field(alias="secComAlgoChallengeOtoToBack", description="???"),
    ] = None
    """
    ???
    """

    api_key_constraints: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="apiKeyConstraints"), pydantic.Field(alias="apiKeyConstraints")
    ] = None
    env: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    x_forwarded_headers: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="xForwardedHeaders"),
        pydantic.Field(alias="xForwardedHeaders", description="???"),
    ] = None
    """
    ???
    """

    transformer_refs: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="transformerRefs"),
        pydantic.Field(alias="transformerRefs", description="???"),
    ] = None
    """
    ???
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    gzip: typing.Optional[typing.Any] = None
    send_info_token: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sendInfoToken"),
        pydantic.Field(alias="sendInfoToken", description="???"),
    ] = None
    """
    ???
    """

    tcp_udp_tunneling: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="tcpUdpTunneling"),
        pydantic.Field(alias="tcpUdpTunneling", description="???"),
    ] = None
    """
    ???
    """

    remove_headers_out: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="removeHeadersOut"),
        pydantic.Field(alias="removeHeadersOut", description="???"),
    ] = None
    """
    ???
    """

    use_akka_http_client: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useAkkaHttpClient"),
        pydantic.Field(alias="useAkkaHttpClient", description="???"),
    ] = None
    """
    ???
    """

    maintenance_mode: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="maintenanceMode"),
        pydantic.Field(alias="maintenanceMode", description="???"),
    ] = None
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    remove_headers_in: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="removeHeadersIn"),
        pydantic.Field(alias="removeHeadersIn", description="???"),
    ] = None
    """
    ???
    """

    log_analytics_on_server: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="logAnalyticsOnServer"),
        pydantic.Field(alias="logAnalyticsOnServer", description="???"),
    ] = None
    """
    ???
    """

    sec_com_algo_info_token: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsAlgoSettings],
        FieldMetadata(alias="secComAlgoInfoToken"),
        pydantic.Field(alias="secComAlgoInfoToken", description="???"),
    ] = None
    """
    ???
    """

    user_facing: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="userFacing"), pydantic.Field(alias="userFacing", description="???")
    ] = None
    """
    ???
    """

    transformer_config: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="transformerConfig"),
        pydantic.Field(alias="transformerConfig", description="???"),
    ] = None
    """
    ???
    """

    client_validator_ref: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef],
        FieldMetadata(alias="clientValidatorRef"),
        pydantic.Field(alias="clientValidatorRef", description="???"),
    ] = None
    """
    ???
    """

    security_excluded_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="securityExcludedPatterns"),
        pydantic.Field(alias="securityExcludedPatterns", description="???"),
    ] = None
    """
    ???
    """

    ip_filtering: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="ipFiltering"), pydantic.Field(alias="ipFiltering")
    ] = None
    targets: typing.Optional[typing.List[OtoroshiModelsTarget]] = pydantic.Field(default=None)
    """
    ???
    """

    redirection: typing.Optional[typing.Any] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    restrictions: typing.Optional[typing.Any] = None
    override_host: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="overrideHost"),
        pydantic.Field(alias="overrideHost", description="???"),
    ] = None
    """
    ???
    """

    access_validator: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="accessValidator"), pydantic.Field(alias="accessValidator")
    ] = None
    send_state_challenge: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sendStateChallenge"),
        pydantic.Field(alias="sendStateChallenge", description="???"),
    ] = None
    """
    ???
    """

    chaos_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="chaosConfig"), pydantic.Field(alias="chaosConfig")
    ] = None
    sec_com_info_token_version: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="secComInfoTokenVersion"),
        pydantic.Field(alias="secComInfoTokenVersion"),
    ] = None
    additional_headers_out: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="additionalHeadersOut"),
        pydantic.Field(alias="additionalHeadersOut", description="???"),
    ] = None
    """
    ???
    """

    sec_com_headers: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="secComHeaders"), pydantic.Field(alias="secComHeaders")
    ] = None
    matching_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="matchingHeaders"),
        pydantic.Field(alias="matchingHeaders", description="???"),
    ] = None
    """
    ???
    """

    sec_com_algo_challenge_back_to_oto: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsAlgoSettings],
        FieldMetadata(alias="secComAlgoChallengeBackToOto"),
        pydantic.Field(alias="secComAlgoChallengeBackToOto", description="???"),
    ] = None
    """
    ???
    """

    sec_com_use_same_algo: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="secComUseSameAlgo"),
        pydantic.Field(alias="secComUseSameAlgo", description="???"),
    ] = None
    """
    ???
    """

    use_new_ws_client: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useNewWSClient"),
        pydantic.Field(alias="useNewWSClient", description="???"),
    ] = None
    """
    ???
    """

    sec_com_excluded_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="secComExcludedPatterns"),
        pydantic.Field(alias="secComExcludedPatterns", description="???"),
    ] = None
    """
    ???
    """

    redirect_to_local: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="redirectToLocal"),
        pydantic.Field(alias="redirectToLocal", description="???"),
    ] = None
    """
    ???
    """

    enforce_secure_communication: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="enforceSecureCommunication"),
        pydantic.Field(alias="enforceSecureCommunication", description="???"),
    ] = None
    """
    ???
    """

    missing_only_headers_out: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="missingOnlyHeadersOut"),
        pydantic.Field(alias="missingOnlyHeadersOut", description="???"),
    ] = None
    """
    ???
    """

    sec_com_settings: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsAlgoSettings],
        FieldMetadata(alias="secComSettings"),
        pydantic.Field(alias="secComSettings", description="???"),
    ] = None
    """
    ???
    """

    handle_legacy_domain: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="handleLegacyDomain"),
        pydantic.Field(alias="handleLegacyDomain", description="???"),
    ] = None
    """
    ???
    """

    canary: typing.Optional[typing.Any] = None
    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    plugins: typing.Optional[typing.Any] = None
    sec_com_ttl: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="secComTtl"), pydantic.Field(alias="secComTtl", description="???")
    ] = None
    """
    ???
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    sec_com_version: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="secComVersion"), pydantic.Field(alias="secComVersion")
    ] = None
    pre_routing: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="preRouting"), pydantic.Field(alias="preRouting")
    ] = None
    groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    read_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="readOnly"), pydantic.Field(alias="readOnly", description="???")
    ] = None
    """
    ???
    """

    private_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="privatePatterns"),
        pydantic.Field(alias="privatePatterns", description="???"),
    ] = None
    """
    ???
    """

    targets_load_balancing: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="targetsLoadBalancing"),
        pydantic.Field(alias="targetsLoadBalancing"),
    ] = None
    cors: typing.Optional[typing.Any] = None
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    public_patterns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="publicPatterns"),
        pydantic.Field(alias="publicPatterns", description="???"),
    ] = None
    """
    ???
    """

    api: typing.Optional[typing.Any] = None
    missing_only_headers_in: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="missingOnlyHeadersIn"),
        pydantic.Field(alias="missingOnlyHeadersIn", description="???"),
    ] = None
    """
    ???
    """

    issue_cert: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="issueCert"), pydantic.Field(alias="issueCert", description="???")
    ] = None
    """
    ???
    """

    headers_verification: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="headersVerification"),
        pydantic.Field(alias="headersVerification", description="???"),
    ] = None
    """
    ???
    """

    jwt_verifier: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="jwtVerifier"), pydantic.Field(alias="jwtVerifier")
    ] = None
    lets_encrypt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="letsEncrypt"),
        pydantic.Field(alias="letsEncrypt", description="???"),
    ] = None
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
