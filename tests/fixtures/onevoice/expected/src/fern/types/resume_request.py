

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resume_request_whitelist_mode import ResumeRequestWhitelistMode
from .tool_floor import ToolFloor


class ResumeRequest(UniversalBaseModel):
    business_approvals: typing.Optional[typing.Dict[str, ToolFloor]] = None
    project_approval_overrides: typing.Optional[typing.Dict[str, ToolFloor]] = None
    active_integrations: typing.Optional[typing.List[str]] = None
    whitelist_mode: typing.Optional[ResumeRequestWhitelistMode] = None
    allowed_tools: typing.Optional[typing.List[str]] = None
    model: typing.Optional[str] = None
    tier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
