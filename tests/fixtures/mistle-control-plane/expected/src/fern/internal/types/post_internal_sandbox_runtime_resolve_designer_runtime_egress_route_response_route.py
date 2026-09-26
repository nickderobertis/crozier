

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_additional_credential_headers_item import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAdditionalCredentialHeadersItem,
)
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_auth_injection import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAuthInjection,
)
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_credential_resolver import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver,
)
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_match import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteMatch,
)
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route_upstream import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteUpstream,
)


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRoute(UniversalBaseModel):
    egress_rule_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="egressRuleId"), pydantic.Field(alias="egressRuleId")
    ]
    binding_id: typing_extensions.Annotated[str, FieldMetadata(alias="bindingId"), pydantic.Field(alias="bindingId")]
    family_id: typing_extensions.Annotated[str, FieldMetadata(alias="familyId"), pydantic.Field(alias="familyId")]
    variant_id: typing_extensions.Annotated[str, FieldMetadata(alias="variantId"), pydantic.Field(alias="variantId")]
    match: PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteMatch
    upstream: PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteUpstream
    auth_injection: typing_extensions.Annotated[
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAuthInjection,
        FieldMetadata(alias="authInjection"),
        pydantic.Field(alias="authInjection"),
    ]
    additional_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="additionalHeaders"),
        pydantic.Field(alias="additionalHeaders"),
    ] = None
    additional_credential_headers: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAdditionalCredentialHeadersItem
            ]
        ],
        FieldMetadata(alias="additionalCredentialHeaders"),
        pydantic.Field(alias="additionalCredentialHeaders"),
    ] = None
    credential_resolver: typing_extensions.Annotated[
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolver,
        FieldMetadata(alias="credentialResolver"),
        pydantic.Field(alias="credentialResolver"),
    ]
    request_middleware: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="requestMiddleware"),
        pydantic.Field(alias="requestMiddleware"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
