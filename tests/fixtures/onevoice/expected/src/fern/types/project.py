

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_approval_overrides_value import ProjectApprovalOverridesValue
from .project_whitelist_mode import ProjectWhitelistMode


class Project(UniversalBaseModel):
    id: str
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    name: str
    description: typing.Optional[str] = None
    system_prompt: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="systemPrompt"), pydantic.Field(alias="systemPrompt")
    ] = None
    whitelist_mode: typing_extensions.Annotated[
        ProjectWhitelistMode, FieldMetadata(alias="whitelistMode"), pydantic.Field(alias="whitelistMode")
    ]
    allowed_tools: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="allowedTools"), pydantic.Field(alias="allowedTools")
    ]
    approval_overrides: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, ProjectApprovalOverridesValue]],
        FieldMetadata(alias="approvalOverrides"),
        pydantic.Field(alias="approvalOverrides"),
    ] = None
    quick_actions: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="quickActions"), pydantic.Field(alias="quickActions")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
