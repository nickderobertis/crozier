

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateWorkflowApprovalRequestUser(UniversalBaseModel):
    """
    The Ironclad user approving the workflow. The user must be currently assigned as the approver.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Ironclad user's email address.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The mechanism of identifying the Ironclad user's account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
