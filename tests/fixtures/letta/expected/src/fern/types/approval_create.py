

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_create_approvals_item import ApprovalCreateApprovalsItem
from .approval_create_type import ApprovalCreateType


class ApprovalCreate(UniversalBaseModel):
    """
    Input to approve or deny a tool call request
    """

    type: typing.Optional[ApprovalCreateType] = pydantic.Field(default=None)
    """
    The message type to be created.
    """

    approvals: typing.Optional[typing.List[ApprovalCreateApprovalsItem]] = pydantic.Field(default=None)
    """
    The list of approval responses
    """

    approve: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the tool has been approved
    """

    approval_request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The message ID of the approval request
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional explanation for the provided approval status
    """

    group_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The multi-agent group that the message was sent in
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
