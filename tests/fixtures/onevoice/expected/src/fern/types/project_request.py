

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_request_approval_overrides_value import ProjectRequestApprovalOverridesValue
from .project_request_whitelist_mode import ProjectRequestWhitelistMode


class ProjectRequest(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    system_prompt: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="systemPrompt"), pydantic.Field(alias="systemPrompt")
    ] = None
    whitelist_mode: typing_extensions.Annotated[
        typing.Optional[ProjectRequestWhitelistMode],
        FieldMetadata(alias="whitelistMode"),
        pydantic.Field(alias="whitelistMode"),
    ] = None
    allowed_tools: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="allowedTools"), pydantic.Field(alias="allowedTools")
    ] = None
    approval_overrides: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, ProjectRequestApprovalOverridesValue]],
        FieldMetadata(alias="approvalOverrides"),
        pydantic.Field(alias="approvalOverrides"),
    ] = None
    quick_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="quickActions"), pydantic.Field(alias="quickActions")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
