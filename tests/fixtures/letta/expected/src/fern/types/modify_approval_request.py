

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModifyApprovalRequest(UniversalBaseModel):
    """
    Request body for modifying tool approval requirements.
    """

    requires_approval: bool = pydantic.Field()
    """
    Whether the tool requires approval before execution
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
