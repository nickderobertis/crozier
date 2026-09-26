

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_credential_resolver_linked_principal_resolution_mode import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode,
)


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_IntegrationConnection(
    UniversalBaseModel
):
    kind: typing.Literal["integration_connection"] = "integration_connection"
    connection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    secret_type: typing_extensions.Annotated[str, FieldMetadata(alias="secretType"), pydantic.Field(alias="secretType")]
    slot_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="slotKey"), pydantic.Field(alias="slotKey")
    ] = None
    resolver_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resolverKey"), pydantic.Field(alias="resolverKey")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_LinkedPrincipal(
    UniversalBaseModel
):
    kind: typing.Literal["linked_principal"] = "linked_principal"
    provider_family: typing_extensions.Annotated[
        str, FieldMetadata(alias="providerFamily"), pydantic.Field(alias="providerFamily")
    ]
    integration_connection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationConnectionId"),
        pydantic.Field(alias="integrationConnectionId"),
    ] = None
    credential_kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="credentialKind"), pydantic.Field(alias="credentialKind")
    ] = None
    acting_user_required: typing_extensions.Annotated[
        bool, FieldMetadata(alias="actingUserRequired"), pydantic.Field(alias="actingUserRequired")
    ]
    resolution_mode: typing_extensions.Annotated[
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode,
        FieldMetadata(alias="resolutionMode"),
        pydantic.Field(alias="resolutionMode"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpToken(
    UniversalBaseModel
):
    kind: typing.Literal["mistle_mcp_token"] = "mistle_mcp_token"
    api_key_id: typing_extensions.Annotated[str, FieldMetadata(alias="apiKeyId"), pydantic.Field(alias="apiKeyId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpSetupAssistantToken(
    UniversalBaseModel
):
    kind: typing.Literal["mistle_mcp_setup_assistant_token"] = "mistle_mcp_setup_assistant_token"
    sandbox_profile_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sandboxProfileId"), pydantic.Field(alias="sandboxProfileId")
    ]
    sandbox_profile_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="sandboxProfileVersion"), pydantic.Field(alias="sandboxProfileVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpDesignerToken(
    UniversalBaseModel
):
    kind: typing.Literal["mistle_mcp_designer_token"] = "mistle_mcp_designer_token"
    designer_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="designerSessionId"), pydantic.Field(alias="designerSessionId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_PlatformOpenaiApiKey(
    UniversalBaseModel
):
    kind: typing.Literal["platform_openai_api_key"] = "platform_openai_api_key"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_PlatformLangfuseSecretKey(
    UniversalBaseModel
):
    kind: typing.Literal["platform_langfuse_secret_key"] = "platform_langfuse_secret_key"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver = typing_extensions.Annotated[
    typing.Union[
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_IntegrationConnection,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_LinkedPrincipal,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpToken,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpSetupAssistantToken,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_MistleMcpDesignerToken,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_PlatformOpenaiApiKey,
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver_PlatformLangfuseSecretKey,
    ],
    pydantic.Field(discriminator="kind"),
]
