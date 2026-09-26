

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_credential_resolver_linked_principal_resolution_mode import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode,
)


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipal(
    UniversalBaseModel
):
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
