

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .suspend_user_response_suspension_suspended_by import SuspendUserResponseSuspensionSuspendedBy


class SuspendUserResponseSuspension(UniversalBaseModel):
    full_suspend_reason: str
    suspend_reason: str
    suspended_at: str
    suspended_by: SuspendUserResponseSuspensionSuspendedBy
    suspended_till: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
