

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolApprovalPolicyAction_AllowSession(UniversalBaseModel):
    type: typing.Literal["allow_session"] = "allow_session"
    expire_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ToolApprovalPolicyAction = ToolApprovalPolicyAction_AllowSession
