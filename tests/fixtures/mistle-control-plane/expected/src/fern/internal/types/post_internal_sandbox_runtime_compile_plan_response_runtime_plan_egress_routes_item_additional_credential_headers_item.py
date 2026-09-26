

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item_additional_credential_headers_item_credential_resolver import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItemCredentialResolver,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItem(
    UniversalBaseModel
):
    header: str
    credential_resolver: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItemCredentialResolver,
        FieldMetadata(alias="credentialResolver"),
        pydantic.Field(alias="credentialResolver"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
