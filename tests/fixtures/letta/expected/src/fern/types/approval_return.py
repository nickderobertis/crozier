

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_return_type import ApprovalReturnType


class ApprovalReturn(UniversalBaseModel):
    type: typing.Optional[ApprovalReturnType] = pydantic.Field(default=None)
    """
    The message type to be created.
    """

    tool_call_id: str = pydantic.Field()
    """
    The ID of the tool call that corresponds to this approval
    """

    approve: bool = pydantic.Field()
    """
    Whether the tool has been approved
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional explanation for the provided approval status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
