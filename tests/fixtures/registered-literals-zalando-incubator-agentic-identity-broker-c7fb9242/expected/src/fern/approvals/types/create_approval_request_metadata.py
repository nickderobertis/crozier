

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateApprovalRequestMetadata(UniversalBaseModel):
    mcp_session_id: typing.Optional[str] = None
    agent_session_id: typing.Optional[str] = None
    tool_invocation_id: typing.Optional[str] = None
    description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
