

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_decision import ApprovalDecision


class UserToolApprovalEvent(UniversalBaseModel):
    approval: ApprovalDecision
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    thread_id: str = pydantic.Field()
    """
    Thread that owns the pending tool call.
    """

    tool_call_id: str = pydantic.Field()
    """
    Tool call id being approved or denied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
