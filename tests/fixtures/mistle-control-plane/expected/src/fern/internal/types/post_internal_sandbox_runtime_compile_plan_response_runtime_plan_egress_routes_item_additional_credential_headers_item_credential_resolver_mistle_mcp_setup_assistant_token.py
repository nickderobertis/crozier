

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItemCredentialResolverMistleMcpSetupAssistantToken(
    UniversalBaseModel
):
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
