

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_additional_credential_headers_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_auth_injection import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_credential_resolver import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemCredentialResolver,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_match import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemMatch,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_upstream import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemUpstream,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItem(UniversalBaseModel):
    egress_rule_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="egressRuleId"), pydantic.Field(alias="egressRuleId")
    ]
    binding_id: typing_extensions.Annotated[str, FieldMetadata(alias="bindingId"), pydantic.Field(alias="bindingId")]
    family_id: typing_extensions.Annotated[str, FieldMetadata(alias="familyId"), pydantic.Field(alias="familyId")]
    variant_id: typing_extensions.Annotated[str, FieldMetadata(alias="variantId"), pydantic.Field(alias="variantId")]
    match: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemMatch
    upstream: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemUpstream
    auth_injection: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAuthInjection,
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
                PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItem
            ]
        ],
        FieldMetadata(alias="additionalCredentialHeaders"),
        pydantic.Field(alias="additionalCredentialHeaders"),
    ] = None
    credential_resolver: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemCredentialResolver,
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
