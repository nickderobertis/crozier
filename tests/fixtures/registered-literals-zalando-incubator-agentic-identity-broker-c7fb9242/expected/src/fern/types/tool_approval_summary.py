

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_approval_summary_persistence import ToolApprovalSummaryPersistence
from .tool_approval_summary_status import ToolApprovalSummaryStatus


class ToolApprovalSummary(UniversalBaseModel):
    id: str
    tool_name: str
    arguments_hash: str
    tool_pattern: str = pydantic.Field()
    """
    Server-derived exact matcher for this approval's `tool_name`.
    """

    params_pattern: typing.Dict[str, str] = pydantic.Field()
    """
    Constrained argument names mapped to globs. Argument names absent from this object are unconstrained. An empty object matches any arguments.
    """

    status: ToolApprovalSummaryStatus
    persistence: typing.Optional[ToolApprovalSummaryPersistence] = None
    consumed: bool
    agent_session_id: typing.Optional[str] = None
    approved_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time at which the approval was granted; absent for pending and denied records.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
